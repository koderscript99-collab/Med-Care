from django import forms
from .models import Patience_Details, Prescriptions, MedLab, Ward


# ── Patient Registration ──────────────────────────────────────────────────────
class Patience_DetailsForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Create a strong password'}),
        max_length=100,
    )

    class Meta:
        model  = Patience_Details
        fields = [
            'first_name', 'last_name', 'email',
            'age', 'phone_number', 'date_of_birth',
            'home_address', 'password',
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }


# ── Prescriptions (admin only — not patient-facing) ───────────────────────────
class PrescriptionsForm(forms.ModelForm):
    class Meta:
        model  = Prescriptions
        fields = '__all__'


# ── MedLab: patient picks a service, nothing else ────────────────────────────
class MedLabUserForm(forms.ModelForm):
    class Meta:
        model  = MedLab
        fields = ['lab_service']   # patient only picks the test type
        widgets = {
            'lab_service': forms.Select(attrs={'class': 'medlab-select'}),
        }


# ── MedLab: admin uploads result and controls visibility ──────────────────────
class MedLabAdminForm(forms.ModelForm):
    class Meta:
        model  = MedLab
        fields = '__all__'


# ── Ward: admin creates/edits ward records ────────────────────────────────────
class WardAdminForm(forms.ModelForm):
    class Meta:
        model  = Ward
        fields = '__all__'