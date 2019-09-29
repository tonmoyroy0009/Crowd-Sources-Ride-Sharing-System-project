from django import forms
from .models import CashInOrOut, Transition, Payment


class CashForm(forms.ModelForm):
    class Meta:
        model = CashInOrOut
        fields = ('client', 'cash_in', 'cash_out')
        widgets = {
            'client': forms.HiddenInput()
        }


class TransitionForm(forms.ModelForm):
    class Meta:
        model = Transition
        fields = ('sender', 'receiver', 'amount')
        widgets = {
            'sender': forms.HiddenInput()
        }
