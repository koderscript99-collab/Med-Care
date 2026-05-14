<<<<<<< HEAD
from django.contrib import admin
from django.utils.html import format_html
from .models import Patience_Details, Prescriptions, Ward, MedLab, Dashboard


# ─────────────────────────────────────────────────────────────────────────────
#  PATIENT
# ─────────────────────────────────────────────────────────────────────────────
@admin.register(Patience_Details)
class PatientAdmin(admin.ModelAdmin):
    list_display  = ('user_id', 'first_name', 'last_name', 'email', 'phone_number', 'age')
    search_fields = ('user_id', 'first_name', 'last_name', 'email')
    readonly_fields = ('user_id',)





@admin.register(Prescriptions)
class PrescriptionsAdmin(admin.ModelAdmin):
    list_display  = ('patient', 'drug_name', 'dosage')
    list_filter   = ('patient',)
    search_fields = ('patient__first_name', 'patient__last_name', 'drug_name')
    autocomplete_fields = ['patient']   # fast patient lookup


# ─────────────────────────────────────────────────────────────────────────────
#  WARD  — admin assigns ward to a patient; flip is_visible_to_user when ready
# ─────────────────────────────────────────────────────────────────────────────
@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    list_display  = (
        'patient', 'ward_number', 'bed_number',
        'ward_category', 'is_visible_to_user',
    )
    list_filter   = ('ward_category', 'is_visible_to_user')
    search_fields = ('patient__first_name', 'patient__last_name', 'patient__user_id', 'ward_number')
    list_editable = ('is_visible_to_user',)   # flip visibility without opening the record
    autocomplete_fields = ['patient']

    fieldsets = (
        ('Patient', {
            'fields': ('patient',)
        }),
        ('Ward Details', {
            'fields': ('ward_number', 'bed_number', 'ward_category')
        }),
        ('Guardian', {
            'fields': ('guardians_name', 'contact_number')
        }),
        ('Medical Report', {
            'fields': ('report',)
        }),
        ('Visibility', {
            'fields': ('is_visible_to_user',),
            'description': 'Tick this box when the information is ready for the patient to see on their dashboard.'
        }),
    )


# ─────────────────────────────────────────────────────────────────────────────
#  MEDLAB  — patient requests, admin uploads image result and controls visibility
# ─────────────────────────────────────────────────────────────────────────────
@admin.register(MedLab)
class MedLabAdmin(admin.ModelAdmin):
    list_display  = (
        'patient', 'lab_service', 'report_date',
        'result_uploaded', 'visible_to_patient',
    )
    list_filter   = ('lab_service', 'visible_to_patient')
    search_fields = ('patient__first_name', 'patient__last_name', 'patient__user_id')
    list_editable = ('visible_to_patient',)   # flip visibility inline
    autocomplete_fields = ['patient']
    readonly_fields = ('result_preview',)

    fieldsets = (
        ('Patient', {
            'fields': ('patient',)
        }),
        ('Test Details', {
            'fields': ('lab_service', 'report_date')
        }),
        ('Result Image', {
            'fields': ('test_results', 'result_preview'),
            'description': 'Upload an image of the lab result (JPG, PNG). '
                           'After uploading, tick "Visible to patient" so it appears on their dashboard.'
        }),
        ('Visibility', {
            'fields': ('visible_to_patient',)
        }),
    )

    @admin.display(boolean=True, description='Result uploaded')
    def result_uploaded(self, obj):
        return obj.has_result()

    @admin.display(description='Preview')
    def result_preview(self, obj):
        if obj.test_results:
            return format_html(
                '<img src="{}" style="max-width:320px;max-height:320px;border-radius:8px;" />',
                obj.test_results.url
            )
        return '—'


# ─────────────────────────────────────────────────────────────────────────────
#  DASHBOARD
# ─────────────────────────────────────────────────────────────────────────────
@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    list_display  = ('patient', 'last_login')
=======
from django.contrib import admin
from django.utils.html import format_html
from .models import Patience_Details, Prescriptions, Ward, MedLab, Dashboard


# ─────────────────────────────────────────────────────────────────────────────
#  PATIENT
# ─────────────────────────────────────────────────────────────────────────────
@admin.register(Patience_Details)
class PatientAdmin(admin.ModelAdmin):
    list_display  = ('user_id', 'first_name', 'last_name', 'email', 'phone_number', 'age')
    search_fields = ('user_id', 'first_name', 'last_name', 'email')
    readonly_fields = ('user_id',)





@admin.register(Prescriptions)
class PrescriptionsAdmin(admin.ModelAdmin):
    list_display  = ('patient', 'drug_name', 'dosage')
    list_filter   = ('patient',)
    search_fields = ('patient__first_name', 'patient__last_name', 'drug_name')
    autocomplete_fields = ['patient']   # fast patient lookup


# ─────────────────────────────────────────────────────────────────────────────
#  WARD  — admin assigns ward to a patient; flip is_visible_to_user when ready
# ─────────────────────────────────────────────────────────────────────────────
@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    list_display  = (
        'patient', 'ward_number', 'bed_number',
        'ward_category', 'is_visible_to_user',
    )
    list_filter   = ('ward_category', 'is_visible_to_user')
    search_fields = ('patient__first_name', 'patient__last_name', 'patient__user_id', 'ward_number')
    list_editable = ('is_visible_to_user',)   # flip visibility without opening the record
    autocomplete_fields = ['patient']

    fieldsets = (
        ('Patient', {
            'fields': ('patient',)
        }),
        ('Ward Details', {
            'fields': ('ward_number', 'bed_number', 'ward_category')
        }),
        ('Guardian', {
            'fields': ('guardians_name', 'contact_number')
        }),
        ('Medical Report', {
            'fields': ('report',)
        }),
        ('Visibility', {
            'fields': ('is_visible_to_user',),
            'description': 'Tick this box when the information is ready for the patient to see on their dashboard.'
        }),
    )


# ─────────────────────────────────────────────────────────────────────────────
#  MEDLAB  — patient requests, admin uploads image result and controls visibility
# ─────────────────────────────────────────────────────────────────────────────
@admin.register(MedLab)
class MedLabAdmin(admin.ModelAdmin):
    list_display  = (
        'patient', 'lab_service', 'report_date',
        'result_uploaded', 'visible_to_patient',
    )
    list_filter   = ('lab_service', 'visible_to_patient')
    search_fields = ('patient__first_name', 'patient__last_name', 'patient__user_id')
    list_editable = ('visible_to_patient',)   # flip visibility inline
    autocomplete_fields = ['patient']
    readonly_fields = ('result_preview',)

    fieldsets = (
        ('Patient', {
            'fields': ('patient',)
        }),
        ('Test Details', {
            'fields': ('lab_service', 'report_date')
        }),
        ('Result Image', {
            'fields': ('test_results', 'result_preview'),
            'description': 'Upload an image of the lab result (JPG, PNG). '
                           'After uploading, tick "Visible to patient" so it appears on their dashboard.'
        }),
        ('Visibility', {
            'fields': ('visible_to_patient',)
        }),
    )

    @admin.display(boolean=True, description='Result uploaded')
    def result_uploaded(self, obj):
        return obj.has_result()

    @admin.display(description='Preview')
    def result_preview(self, obj):
        if obj.test_results:
            return format_html(
                '<img src="{}" style="max-width:320px;max-height:320px;border-radius:8px;" />',
                obj.test_results.url
            )
        return '—'


# ─────────────────────────────────────────────────────────────────────────────
#  DASHBOARD
# ─────────────────────────────────────────────────────────────────────────────
@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    list_display  = ('patient', 'last_login')
>>>>>>> 96cd80d94f0b2a918a35f13e053a10dfab5481b2
    readonly_fields = ('last_login',)