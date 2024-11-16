# from django.db import models
# from django.contrib.auth.models import User
# from typing import Optional
#
#
# class HealthData (models.Model):
#     glucose = models.FloatField (default=0)  # تعيين قيمة افتراضية
#     cholesterol = models.FloatField (default=0)  # تعيين قيمة افتراضية
#     hemoglobin = models.FloatField (default=0)  # تعيين قيمة افتراضية
#     Heart_Disease = models.CharField (max_length=255, default='')
#     Diabetes = models.CharField (max_length=255, default='')
#     # Thalassemia = models.CharField ()
#     diabetes = models.BooleanField (default=False)  # تعيي)
#     diagnosis = models.CharField (max_length=255, blank=True, null=True)  # حقل تشخيصي
#     additional_field = models.CharField (max_length=255, blank=True, null=True)  # حقل إضافي
#
#     def __str__(self):
#         return f"Health Data {self.id}"
#
#     # def __str__(self) -> str:
#     #     return f"HealthData (ID: {self.id}, Diagnosis: {self.diagnosis})"
#
#
# class Symptom (models.Model):
#     name: str = models.CharField (max_length=100)
#     type: Optional[str] = models.CharField (max_length=50, blank=True, null=True)
#
#     def __str__(self) -> str:
#         return self.name
#
#
# class Disease (models.Model):
#     name: str = models.CharField (max_length=100)
#     symptoms: Optional["Symptom"] = models.ManyToManyField (Symptom, related_name='diseases')
#
#     def __str__(self) -> str:
#         return self.name
#
#
# class DiseaseSymptom (models.Model):
#     disease: Disease = models.ForeignKey (Disease, on_delete=models.CASCADE)
#     symptom: Symptom = models.ForeignKey (Symptom, on_delete=models.CASCADE)
#     severity: str = models.CharField (
#         max_length=50,
#         choices=[('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe')]
#     )
#
#     def __str__(self) -> str:
#         return f"{self.disease.name} - {self.symptom.name} ({self.severity})"
#
#
# class ImportedFile (models.Model):
#     filename: str = models.CharField (max_length=255, unique=True)
#     upload_date: Optional[models.DateTimeField] = models.DateTimeField (auto_now_add=True)
#     file_data = models.FileField (upload_to='uploads/')
#     file_type: Optional[str] = models.CharField (
#         max_length=50, blank=True, null=True, choices=[('csv', 'CSV'), ('excel', 'Excel')]
#     )
#
#     def __str__(self) -> str:
#         return self.filename
#
#
# class EmailAddress (models.Model):
#     id: Optional[int] = models.BigAutoField (primary_key=True)
#     email: str = models.EmailField (unique=True)
#     user: User = models.ForeignKey (User, on_delete=models.CASCADE, related_name='email_addresses')
#     created_at: Optional[models.DateTimeField] = models.DateTimeField (auto_now_add=True)
#
#     def __str__(self) -> str:
#         return self.email


from django.db import models
from django.contrib.auth.models import User
from typing import Optional


class HealthData(models.Model):
    glucose = models.FloatField(default=0)
    cholesterol = models.FloatField(default=0)
    hemoglobin = models.FloatField(default=0)
    heart_disease = models.CharField(max_length=255, default='')
    diabetes = models.CharField(max_length=255, default='')
    diabetes_boolean = models.BooleanField(default=False)
    diagnosis = models.CharField(max_length=255, blank=True, null=True)
    additional_field = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Health Data {self.id}"


class Symptom(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Disease(models.Model):
    name = models.CharField(max_length=100)
    symptoms = models.ManyToManyField(Symptom, related_name='diseases')
    diagnostic_methods = models.TextField(blank=True, null=True)  # Methods for diagnosis
    treatment = models.TextField(blank=True, null=True)  # Treatment suggestions
    recommendations = models.TextField(blank=True, null=True)  # Patient recommendations

    def __str__(self):
        return self.name


class DiseaseSymptom(models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)
    severity = models.CharField(
        max_length=50,
        choices=[('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe')]
    )

    def __str__(self):
        return f"{self.disease.name} - {self.symptom.name} ({self.severity})"


class ImportedFile(models.Model):
    filename = models.CharField(max_length=255, unique=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    file_data = models.FileField(upload_to='uploads/')
    file_type = models.CharField(max_length=50, blank=True, null=True, choices=[('csv', 'CSV'), ('excel', 'Excel')])

    def __str__(self):
        return self.filename


class EmailAddress(models.Model):
    email = models.EmailField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='email_addresses')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Diagnosis(models.Model):
    health_data = models.ForeignKey(HealthData, on_delete=models.CASCADE, related_name='diagnoses')
    disease = models.ForeignKey(Disease, on_delete=models.SET_NULL, null=True)
    symptoms_entered = models.TextField()
    diagnostic_methods_used = models.TextField()
    final_diagnosis = models.CharField(max_length=255)
    patient_advice = models.TextField()

    def __str__(self):
        return f"Diagnosis of {self.disease.name if self.disease else 'Unknown Disease'}"


class Medication(models.Model):
    name = models.CharField(max_length=100)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    dosage = models.CharField(max_length=100)
    side_effects = models.TextField()
    treatment_duration = models.CharField(max_length=100)
    usage_instructions = models.TextField()

    def __str__(self):
        return self.name


class XRayTest(models.Model):
    test_type = models.CharField(max_length=100)
    test_date = models.DateTimeField()
    results = models.TextField()
    attachment = models.FileField(upload_to='xray_tests/')

    def __str__(self):
        return f"{self.test_type} on {self.test_date}"


class MedicalProcedure(models.Model):
    name = models.CharField(max_length=100)
    procedure_date = models.DateTimeField()
    responsible_doctor = models.CharField(max_length=255)
    procedure_details = models.TextField()

    def __str__(self):
        return self.name


class MedicalAdviceFollowUp(models.Model):
    advice = models.TextField()
    follow_up_date = models.DateTimeField()
    patient_instructions = models.TextField()

    def __str__(self):
        return f"Advice for {self.follow_up_date}"


class AIModel(models.Model):
    model_name = models.CharField(max_length=100)
    model_output = models.TextField()
    accuracy = models.FloatField()

    def __str__(self):
        return f"{self.model_name} Model"
