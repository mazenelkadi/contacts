from .session import isValidSession
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.template import loader
from django.shortcuts import render
from .forms import UserContactForm
from urllib import parse
from .session import isValidSession, delete_session
from .service import get_user_contacts, save_details, delete_user_contact
from .models import UserContact

def index(request):
    context = {
        'error': None,
        'session': False
    }
    session_valid = isValidSession(request)
    if session_valid:
        context['session'] = True
        context['username'] = request.session['username']
        user = User.objects.get(username=context['username'])
        context['contacts'] = get_user_contacts(user)
        template = loader.get_template('contacts/contacts.html')
        return HttpResponse(template.render(context, request))
    else:
        if request.method == 'POST':
            form_query = request.body.decode('utf-8')
            form_dict = parse.parse_qs(form_query)
            form_keys = form_dict.keys()
            if "username" not in form_keys or "password" not in form_keys:
                context['message'] = 'Enter username and password'
                context['error'] = True
            else:
                username = form_dict['username'][0]
                password = form_dict['password'][0]
                user = authenticate(username=username, password=password)
                if user is not None:
                    request.session['username'] = username
                    request.session.set_expiry(1800)
                    return HttpResponseRedirect("/contacts")
                else:
                    context['message'] = 'Please check username and password'
                    context['error'] = True
        template = loader.get_template('contacts/login.html')
        return HttpResponse(template.render(context, request))




@require_http_methods(["GET", "POST"])
def add_new_contact(request):
    context = {
        'error': None,
        'session': False
    }
    session_valid = isValidSession(request)
    if session_valid:
        context['session'] = True
        context['username'] = request.session['username']
        user = User.objects.get(username=context['username'])

        form = UserContactForm()  # Initialize the form here
        context['form'] = form  # Add form to context

        if request.method == 'POST':
            form = UserContactForm(request.POST)
            if form.is_valid():
                if save_details(form, user):
                    return HttpResponseRedirect("/contacts")
            else:
                # Handle form errors here
                return HttpResponseRedirect("/contacts/add")

        template = loader.get_template('contacts/add_contact.html')
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect("/contacts")


def delete_contact(request, contact_id):
    context = {
        'error': None,
        'session': False
    }
    session_valid = isValidSession(request)
    if session_valid and contact_id:
        context['session'] = True
        context['username'] = request.session['username']
        user = User.objects.get(username=context['username'])
        delete_user_contact(user, contact_id)  # Pass contact_id directly
    return HttpResponseRedirect('/contacts')



@require_http_methods(["GET", "POST"])
def edit_contact(request, contact_id):
    # Replace with your session validation logic
    session_valid = isValidSession(request)
    if session_valid:
        user = User.objects.get(username=request.session['username'])
        try:
            contact = UserContact.objects.get(id=contact_id, user=user)
        except UserContact.DoesNotExist:
            return HttpResponse("Contact not found", status=404)

        if request.method == 'POST':
            form = UserContactForm(request.POST, instance=contact)
            if form.is_valid():
                form.save()
                contact.refresh_from_db()
                return HttpResponseRedirect("/contacts")
        else:
            form = UserContactForm(instance=contact)

        # Extract choices from the form fields
        phone_choices = form.fields['phone_type'].choices
        email_choices = form.fields['email_type'].choices
        date_choices = form.fields['occasion'].choices
        relation_choices = form.fields['relation'].choices

        return render(request, 'contacts/edit_contact.html', {
            'form': form,
            'contact': contact,
            'phone': phone_choices,
            'email': email_choices,
            'date': date_choices,
            'relation': relation_choices
        })
    else:
        return HttpResponseRedirect("/contacts")




def logout(request):
    delete_session(request)
    return HttpResponseRedirect("/contacts")
