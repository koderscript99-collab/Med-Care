from django.urls import path
from . import views

urlpatterns = [
    # ── Public ──────────────────────────────────────────
    path('',                   views.home,                name='home'),
    path('patience-register/', views.Patience_Details,    name='patience_register'),
    path('login/',             views.login_view,          name='login'),
    path('logout/',            views.logout_view,         name='logout'),
    path('success/',           views.success,             name='success'),
    path('uid/',               views.uid,                 name='uid'),

    # ── Patient Portal (session-protected) ──────────────
    path('dashboard/',         views.dashboard,           name='dashboard'),
    path('prescriptions/',     views.prescriptions_view,  name='prescriptions'),
    path('medlab/',            views.medlab,              name='medlab'),
    path('ward/',              views.wardview,            name='ward'),
]