from django import forms
from .models import UserContact


class UserContactForm(forms.ModelForm):
    prefix = forms.CharField(label="prefix", max_length=30, required=False)
    first_name = forms.CharField(label="firstname", max_length=30, required=False)
    last_name = forms.CharField(label="lastname", max_length=30, required=False)
    sur_name = forms.CharField(label="surname", max_length=30, required=False)
    suffix = forms.CharField(label="suffix", max_length=30, required=False)
    company_name = forms.CharField(label="company_name", max_length=40, required=False)
    phonenumber = forms.CharField(label="phonenumber", max_length=15, required=False)
    phone_type = forms.ChoiceField(label="phone_type", choices=UserContact.phone_choices, required=False, widget=forms.Select(attrs={'class': 'phone-choice-select'}))
    email = forms.CharField(label="email", max_length=50, required=False)
    email_type = forms.ChoiceField(label="email_type", choices=UserContact.common_choices, required=False, widget=forms.Select(attrs={'class': 'email-choice-select'}))
    address = forms.CharField(label="address", widget=forms.Textarea, required=False)
    address_type=forms.ChoiceField(label="address_type", choices=UserContact.common_choices, required=False, widget=forms.Select(attrs={'class': 'address-choice-select'}))
    occasion_date = forms.DateField(label="occasion_date", required=False)
    occasion=forms.ChoiceField(label="occasion", choices=UserContact.date_choices, required=False, widget=forms.Select(attrs={'class': 'select-anniversary-choice'}))
    relation = forms.ChoiceField(label="relationships", choices=UserContact.relations, required=False, widget=forms.Select(attrs={'class': 'select-relationship-choice'}))
    description = forms.CharField(label="description", max_length=200, required=False, widget=forms.Textarea)

    class Meta:
        model = UserContact
        fields = [
            'prefix', 'first_name', 'last_name', 'sur_name', 'suffix',
            'company_name', 'phonenumber', 'phone_type', 'email', 'email_type',
            'address', 'address_type', 'occasion_date', 'occasion', 'relation',
            'description'
        ]
