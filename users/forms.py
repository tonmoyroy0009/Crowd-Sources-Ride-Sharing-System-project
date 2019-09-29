from django import forms
from .models import Profile, Verify
from django.forms.widgets import DateInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget



class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2',)



class ProfileUpdateForm(forms.ModelForm):
    phone_number = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(
            attrs={'placeholder': _('Phone Number'), 'class': "form-control"}),
        label=_('Phone Number'),
        required=True,
        initial='+880'
    )
    class Meta:
        model = Profile
        fields = ('full_name', 'date_of_birth', 'profile_picture', 'phone_number', 'address',)
        widgets = {
            'date_of_birth': DateInput(attrs={'type': 'date'}),
        }


class ProfileVerifyForm(forms.ModelForm):
    class Meta:
        model = Verify
        fields = ('utility', 'nid', 'nid_front', 'nid_back', 'nid_selfie',)
        
