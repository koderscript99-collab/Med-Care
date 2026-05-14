from django import forms
from .models import (
    Patience_Details,
    Prescriptions,
    MedLab,
    Ward,
)


class Patience_DetailsForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Patience_Details
        fields = '__all__'


class PrescriptionsForm(forms.ModelForm):
    class Meta:
        model = Prescriptions
        fields = '__all__'


class MedLabUserForm(forms.ModelForm):
    class Meta:
        model = MedLab
        exclude = ['patient']


class MedLabAdminForm(forms.ModelForm):
    class Meta:
        model = MedLab
        fields = '__all__'


class WardAdminForm(forms.ModelForm):
    class Meta:
        model = Ward
        fields = '__all__'