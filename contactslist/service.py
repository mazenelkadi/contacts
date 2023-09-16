from django.core.exceptions import ObjectDoesNotExist

from .models import UserContact

#get user


def get_user_contacts(user):
    if user is not None:
        try:
            all_users = UserContact.objects.filter(user=user)
            all_contacts = []
            for contact in all_users:
                contact_dict = {}
                contact_dict['id'] = contact.id
                contact_dict['prefix'] = contact.prefix
                contact_dict['first_name'] = contact.first_name
                contact_dict['last_name'] = contact.last_name
                contact_dict['suffix'] = contact.suffix
                contact_dict['phonenumber'] = contact.phonenumber
                contact_dict['phone_type'] = contact.phone_type
                contact_dict['company_name'] = contact.company_name
                contact_dict['email'] = contact.email
                contact_dict['email_type'] = contact.email_type
                contact_dict['address'] = contact.address
                contact_dict['address_type'] = contact.address_type
                contact_dict['occasion_date'] = contact.occasion_date
                contact_dict['occasion'] = contact.occasion
                contact_dict['relation'] = contact.relation
                contact_dict['description'] = contact.description
                all_contacts.append(contact_dict)
            return all_contacts
        except ObjectDoesNotExist:
            return []
    return []


#save user

def save_details(form, owner):
    if form.is_valid():  # Check if form is valid
        try:
            print("Form data:", form.cleaned_data)  # Debug print

            user = UserContact()
            user.prefix = form.cleaned_data.get('prefix', '')
            user.first_name = form.cleaned_data.get('first_name', '')
            user.last_name = form.cleaned_data.get('last_name', '')
            user.suffix = form.cleaned_data.get('suffix', '')
            user.sur_name = form.cleaned_data.get('sur_name', '')
            user.phonenumber = form.cleaned_data.get('phonenumber', '')
            user.phone_type = form.cleaned_data.get('phone_type', '')
            user.company_name = form.cleaned_data.get('company_name', '')
            user.email = form.cleaned_data.get('email', '')
            user.email_type = form.cleaned_data.get('email_type', '')
            user.address = form.cleaned_data.get('address', '')
            user.address_type = form.cleaned_data.get('address_type', '')
            user.occasion_date = form.cleaned_data.get('occasion_date', '') or None
            user.occasion = form.cleaned_data.get('occasion', '')
            user.relation = form.cleaned_data.get('relation', '')
            user.description = form.cleaned_data.get('description', '')
            user.user = owner
            user.save()

            print("Details saved successfully.")  # Debug print

            return True
        except Exception as e:  # Catch the exception
            print("Exception occurred:", e)  # Print the exception
            return False
    else:
        print("Form is not valid")  # Debug print
        return False

#delete user


def delete_user_contact(user, contact_id):
    try:
        contact = UserContact.objects.get(id=contact_id, user=user)
        contact.delete()
        return True
    except Exception as e:
        print(f"Exception occurred: {e}")
        return False


#edit user
def edit_contact_details(form, contact):
    if form.is_valid():
        try:
            contact.prefix = form.cleaned_data.get('prefix', '')
            contact.first_name = form.cleaned_data.get('first_name', '')
            contact.last_name = form.cleaned_data.get('last_name', '')
            contact.suffix = form.cleaned_data.get('suffix', '')
            contact.sur_name = form.cleaned_data.get('sur_name', '')
            contact.phonenumber = form.cleaned_data.get('phonenumber', '')
            contact.phone_type = form.cleaned_data.get('phone_type', '')
            contact.company_name = form.cleaned_data.get('company_name', '')
            contact.email = form.cleaned_data.get('email', '')
            contact.email_type = form.cleaned_data.get('email_type', '')
            contact.address = form.cleaned_data.get('address', '')
            contact.address_type = form.cleaned_data.get('address_type', '')
            contact.occasion_date = form.cleaned_data.get(
                'occasion_date', '') or None
            contact.occasion = form.cleaned_data.get('occasion', '')
            contact.relation = form.cleaned_data.get('relation', '')
            contact.description = form.cleaned_data.get('description', '')

            contact.save()
            return True
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False
    else:
        print("Form is not valid")
        return False
