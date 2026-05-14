import uuid
from django.db import models


# ─────────────────────────────────────────────────────────────────────────────
#  PATIENT
# ─────────────────────────────────────────────────────────────────────────────
class Patience_Details(models.Model):
    user_id = models.CharField(max_length=20, unique=True, blank=True, null=True)
    first_name    = models.CharField(max_length=100, blank=True)
    last_name     = models.CharField(max_length=100, blank=True)
    email         = models.EmailField(unique=True)
    age           = models.IntegerField()
    phone_number  = models.CharField(max_length=12)
    date_of_birth = models.DateField(null=True, blank=True)
    home_address  = models.CharField(max_length=100, blank=True)
    password      = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user_id = f"PAT-{uuid.uuid4().hex[:8]}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.user_id})"


# ─────────────────────────────────────────────────────────────────────────────
#  PRESCRIPTIONS  — linked to a patient, set by admin
# ─────────────────────────────────────────────────────────────────────────────
class Prescriptions(models.Model):
    patient   = models.ForeignKey(
        Patience_Details,
        on_delete=models.CASCADE,
        related_name='prescriptions',
        null=True, blank=True,          # null until migrated
    )
    drug_name = models.CharField(max_length=100)
    dosage    = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.drug_name} — {self.dosage}"


# ─────────────────────────────────────────────────────────────────────────────
#  WARD  — admin assigns, patient can only read
# ─────────────────────────────────────────────────────────────────────────────
class Ward(models.Model):
    WARD_CATEGORY_CHOICES = (
        ('General',   'General'),
        ('ICU',       'ICU'),
        ('Maternity', 'Maternity'),
        ('Pediatric', 'Pediatric'),
    )

    # Direct FK to patient — admin picks from dropdown
    patient      = models.ForeignKey(
        Patience_Details,
        on_delete=models.CASCADE,
        related_name='ward_records',
        null=True, blank=True,
    )
    ward_number   = models.CharField(max_length=10)
    bed_number    = models.IntegerField()
    ward_category = models.CharField(max_length=20, choices=WARD_CATEGORY_CHOICES, default='General')
    guardians_name = models.CharField(max_length=100, blank=True)
    contact_number = models.CharField(max_length=12, blank=True)
    report         = models.TextField(blank=True)

    # Admin flips this when info is ready for the patient to see
    is_visible_to_user = models.BooleanField(default=False)

    def __str__(self):
        name = self.patient.first_name if self.patient else "Unassigned"
        return f"{name} — Ward {self.ward_number} ({self.get_ward_category_display()})"


# ─────────────────────────────────────────────────────────────────────────────
#  MEDLAB  — patient requests, admin uploads result
# ─────────────────────────────────────────────────────────────────────────────
class MedLab(models.Model):
    LAB_SERVICE_CHOICES = (
        ('Blood Test', 'Blood Test'),
        ('X-ray',      'X-ray'),
        ('MRI',        'MRI'),
        ('CT Scan',    'CT Scan'),
        ('Ultrasound', 'Ultrasound'),
        ('ECG',        'ECG'),
        ('Urine Test', 'Urine Test'),
        ('Biopsy',     'Biopsy'),
    )

    patient     = models.ForeignKey(
        Patience_Details,
        on_delete=models.CASCADE,
        related_name='lab_records',
    )
    lab_service = models.CharField(max_length=20, choices=LAB_SERVICE_CHOICES)

    # Admin-only fields
    test_results       = models.ImageField(upload_to='test_results/', blank=True, null=True)
    report_date        = models.DateField(null=True, blank=True)
    visible_to_patient = models.BooleanField(default=False)   # admin flips after upload

    def has_result(self):
        return bool(self.test_results)

    def __str__(self):
        return f"{self.patient} — {self.get_lab_service_display()}"


# ─────────────────────────────────────────────────────────────────────────────
#  DASHBOARD  — login tracking
# ─────────────────────────────────────────────────────────────────────────────
class Dashboard(models.Model):
    patient    = models.OneToOneField(
        Patience_Details,
        on_delete=models.CASCADE,
        related_name='dashboard',
        null=True, blank=True,
    )
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient} — {self.last_login}"