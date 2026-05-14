from django.contrib import admin
from django.utils.html import format_html
from .models import Patience_Details, Prescriptions, Ward, MedLab, Dashboard


# ───────────────────────── PATIENT ─────────────────────────
@admin.register(Patience_Details)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'first_name', 'last_name', 'email', 'phone_number', 'age')
    search_fields = ('user_id', 'first_name', 'last_name', 'email')
    readonly_fields = ('user_id',)


# ───────────────────────── PRESCRIPTIONS ─────────────────────────
@admin.register(Prescriptions)
class PrescriptionsAdmin(admin.ModelAdmin):
    list_display = ('patient', 'drug_name', 'dosage')
    list_filter = ('patient',)
    search_fields = ('patient__first_name', 'patient__last_name', 'drug_name')
    autocomplete_fields = ['patient']


# ───────────────────────── WARD ─────────────────────────
@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    list_display = (
        'patient', 'ward_number', 'bed_number',
        'ward_category', 'is_visible_to_user',
    )
    list_filter = ('ward_category', 'is_visible_to_user')
    search_fields = ('patient__first_name', 'patient__last_name', 'patient__user_id')
    list_editable = ('is_visible_to_user',)
    autocomplete_fields = ['patient']


# ───────────────────────── MEDLAB ─────────────────────────
@admin.register(MedLab)
class MedLabAdmin(admin.ModelAdmin):
    list_display = (
        'patient', 'lab_service', 'report_date',
        'result_uploaded', 'visible_to_patient',
    )
    list_filter = ('lab_service', 'visible_to_patient')
    search_fields = ('patient__first_name', 'patient__last_name', 'patient__user_id')
    list_editable = ('visible_to_patient',)
    autocomplete_fields = ['patient']
    readonly_fields = ('result_preview',)

    @admin.display(boolean=True)
    def result_uploaded(self, obj):
        return obj.test_results is not None

    def result_preview(self, obj):
        if obj.test_results:
            return format_html(
                '<img src="{}" style="max-width:300px;" />',
                obj.test_results.url
            )
        return "No Image"


# ───────────────────────── DASHBOARD ─────────────────────────
@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    list_display = ('patient', 'last_login')
    readonly_fields = ('last_login',)