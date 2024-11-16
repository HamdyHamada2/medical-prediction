from django.db import models
from django.contrib.auth.models import User
from typing import Optional


class HealthData (models.Model):
    glucose = models.FloatField (default=0)  # تعيين قيمة افتراضية
    cholesterol = models.FloatField (default=0)  # تعيين قيمة افتراضية
    hemoglobin = models.FloatField (default=0)  # تعيين قيمة افتراضية
    Heart_Disease = models.CharField (max_length=255, default='')
    Diabetes = models.CharField (max_length=255, default='')
    # Thalassemia = models.CharField ()
    diabetes = models.BooleanField (default=False)  # تعيي)
    diagnosis = models.CharField (max_length=255, blank=True, null=True)  # حقل تشخيصي
    additional_field = models.CharField (max_length=255, blank=True, null=True)  # حقل إضافي

    def __str__(self):
        return f"Health Data {self.id}"

    # def __str__(self) -> str:
    #     return f"HealthData (ID: {self.id}, Diagnosis: {self.diagnosis})"


class Symptom (models.Model):
    name: str = models.CharField (max_length=100)
    type: Optional[str] = models.CharField (max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Disease (models.Model):
    name: str = models.CharField (max_length=100)
    symptoms: Optional["Symptom"] = models.ManyToManyField (Symptom, related_name='diseases')

    def __str__(self) -> str:
        return self.name


class DiseaseSymptom (models.Model):
    disease: Disease = models.ForeignKey (Disease, on_delete=models.CASCADE)
    symptom: Symptom = models.ForeignKey (Symptom, on_delete=models.CASCADE)
    severity: str = models.CharField (
        max_length=50,
        choices=[('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe')]
    )

    def __str__(self) -> str:
        return f"{self.disease.name} - {self.symptom.name} ({self.severity})"


class ImportedFile (models.Model):
    filename: str = models.CharField (max_length=255, unique=True)
    upload_date: Optional[models.DateTimeField] = models.DateTimeField (auto_now_add=True)
    file_data = models.FileField (upload_to='uploads/')
    file_type: Optional[str] = models.CharField (
        max_length=50, blank=True, null=True, choices=[('csv', 'CSV'), ('excel', 'Excel')]
    )

    def __str__(self) -> str:
        return self.filename


class EmailAddress (models.Model):
    id: Optional[int] = models.BigAutoField (primary_key=True)
    email: str = models.EmailField (unique=True)
    user: User = models.ForeignKey (User, on_delete=models.CASCADE, related_name='email_addresses')
    created_at: Optional[models.DateTimeField] = models.DateTimeField (auto_now_add=True)

    def __str__(self) -> str:
        return self.email
