from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone
from django import forms

from .models import (
    Patience_Details as PatientModel,
    Prescriptions    as PrescriptionsModel,
    MedLab           as MedLabModel,
    Ward             as WardModel,
    Dashboard        as DashboardModel,
)
from .form import (
    Patience_DetailsForm,
    PrescriptionsForm,
    MedLabUserForm,
    MedLabAdminForm,
    WardAdminForm,
)
# ─────────────────────────────────────────────────────────────────────────────
#  HELPER
# ─────────────────────────────────────────────────────────────────────────────
def get_session_patient(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return None
    try:
        return PatientModel.objects.get(user_id=user_id)
    except PatientModel.DoesNotExist:
        return None


# ─────────────────────────────────────────────────────────────────────────────
#  HOME
# ─────────────────────────────────────────────────────────────────────────────
def home(request):
    return render(request, 'home.html')


# ─────────────────────────────────────────────────────────────────────────────
#  REGISTRATION
# ─────────────────────────────────────────────────────────────────────────────
def Patience_Details(request):

    form = Patience_DetailsForm(request.POST or None)
    if form.is_valid():
        patient = form.save(commit=False)
        patient.password = make_password(form.cleaned_data['password'])
        patient.save()
        send_mail(
            subject="Your MediCare Patient ID",
            message=(
                f"Hello {patient.first_name},\n\n"
                f"Registration successful!\n\n"
                f"Your Patient ID: {patient.user_id}\n\n"
                f"Use this with your password to log in.\n\nThank you for choosing MediCare."
            ),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[patient.email],
            fail_silently=False,
        )
        return redirect('success')
    return render(request, 'patience.html', {'form': form})


# ─────────────────────────────────────────────────────────────────────────────
#  LOGIN
# ─────────────────────────────────────────────────────────────────────────────
def login_view(request):
    if request.method == 'POST':
        user_id  = request.POST.get('pat_id', '').strip()
        password = request.POST.get('password', '')
        try:
            patient = PatientModel.objects.get(user_id=user_id)
        except PatientModel.DoesNotExist:
            return render(request, 'login.html', {'error': 'Patient ID not found.'})
        if not check_password(password, patient.password):
            return render(request, 'login.html', {'error': 'Incorrect password.'})
        request.session['user_id'] = patient.user_id
        # Update last-login tracker
        DashboardModel.objects.update_or_create(
            patient=patient,
            defaults={'last_login': timezone.now()},
        )
        return redirect('dashboard')
    return render(request, 'login.html')


# ─────────────────────────────────────────────────────────────────────────────
#  LOGOUT
# ─────────────────────────────────────────────────────────────────────────────
def logout_view(request):
    request.session.flush()
    return redirect('home')


def success(request):
    return render(request, 'success.html')

def uid(request):
    return render(request, 'uid.html')


# ─────────────────────────────────────────────────────────────────────────────
#  DASHBOARD
# ─────────────────────────────────────────────────────────────────────────────
def dashboard(request):
    patient = get_session_patient(request)
    if not patient:
        return redirect('login')

    ward_records  = WardModel.objects.filter(patient=patient, is_visible_to_user=True)
    lab_records   = MedLabModel.objects.filter(patient=patient, visible_to_patient=True).order_by('-report_date')
    prescriptions = PrescriptionsModel.objects.filter(patient=patient)
    dashboard_rec = DashboardModel.objects.filter(patient=patient).first()

    return render(request, 'dashboard.html', {
        'patient':       patient,
        'ward_records':  ward_records,
        'lab_records':   lab_records,
        'prescriptions': prescriptions,
        'dashboard':     dashboard_rec,
    })


# ─────────────────────────────────────────────────────────────────────────────
#  MESSAGES
# 


# ─────────────────────────────────────────────────────────────────────────────
#  MEDLAB
# ─────────────────────────────────────────────────────────────────────────────
def medlab(request):
    patient = get_session_patient(request)
    if not patient:
        return redirect('login')
    if request.method == 'POST':
        form = MedLabUserForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.patient = patient
            entry.save()
            return redirect('dashboard')
    else:
        form = MedLabUserForm()
    lab_records = MedLabModel.objects.filter(patient=patient, visible_to_patient=True).order_by('-report_date')
    return render(request, 'medlab_records.html', {'patient': patient, 'form': form, 'lab_records': lab_records})


# ─────────────────────────────────────────────────────────────────────────────
#  PRESCRIPTIONS
# ─────────────────────────────────────────────────────────────────────────────
def prescriptions_view(request):
    patient = get_session_patient(request)
    if not patient:
        return redirect('login')
    prescriptions = PrescriptionsModel.objects.filter(patient=patient)
    return render(request, 'prescriptions.html', {'patient': patient, 'prescriptions': prescriptions})


# ─────────────────────────────────────────────────────────────────────────────
#  WARD
# ─────────────────────────────────────────────────────────────────────────────
def wardview(request):
    patient = get_session_patient(request)
    if not patient:
        return redirect('login')
    ward_records = WardModel.objects.filter(patient=patient, is_visible_to_user=True)
    return render(request, 'ward.html', {'patient': patient, 'ward_records': ward_records})



def save(request):
    return render(request, 'save.html') 
def medlab_submit(request):
    return render(request, 'medlab_submit.html')
