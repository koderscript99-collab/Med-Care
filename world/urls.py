
from django.urls import path
from . import views

urlpatterns = [
    # ── Public ──────────────────────────────────────────
    path('',              views.home,             name='home'),
    path('patience-register/', views.Patience_Details, name='patience_register'),   # added for home.html
    path('login/',        views.login_view,        name='login'),
    path('logout/',       views.logout_view,       name='logout'),
    path('success/',      views.success,           name='success'),
    path('save/',         views.save,              name='save'),
    path('uid/',          views.uid,               name='uid'),
    path('dashboard/',    views.dashboard,         name='dashboard'),   # moved to patient portal section

    # ── Patient portal (session-protected) ──────────────
    path('dashboard/',    views.dashboard,         name='dashboard'),   # was dashboard_view
    path('prescriptions/',views.prescriptions_view,name='prescriptions'), # was Prescriptions
    path('medlab/',        views.medlab,      name='medlab'),       # was MedLab
    path('ward/',          views.wardview,       name='ward'),
    path('medlab-submit/', views.medlab_submit, name='medlab_submit'),



    # ── Add these to your urls.py urlpatterns list ───────────────────────────────


    # Custom Admin Panel
]








from django.urls import path
from . import views

urlpatterns = [
    # ── Public ──────────────────────────────────────────
    path('',              views.home,             name='home'),
    path('patience-register/', views.Patience_Details, name='patience_register'),   # added for home.html
    path('login/',        views.login_view,        name='login'),
    path('logout/',       views.logout_view,       name='logout'),
    path('success/',      views.success,           name='success'),
    path('save/',         views.save,              name='save'),
    path('uid/',          views.uid,               name='uid'),
    path('dashboard/',    views.dashboard,         name='dashboard'),   # moved to patient portal section

    # ── Patient portal (session-protected) ──────────────
    path('dashboard/',    views.dashboard,         name='dashboard'),   # was dashboard_view
    path('prescriptions/',views.prescriptions_view,name='prescriptions'), # was Prescriptions
    path('medlab/',        views.medlab,      name='medlab'),       # was MedLab
    path('ward/',          views.wardview,       name='ward'),
    path('medlab-submit/', views.medlab_submit, name='medlab_submit'),



    # ── Add these to your urls.py urlpatterns list ───────────────────────────────


    # Custom Admin Panel
]




