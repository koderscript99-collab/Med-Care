<<<<<<< HEAD
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
=======
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
>>>>>>> 96cd80d94f0b2a918a35f13e053a10dfab5481b2
        fields = '__all__'