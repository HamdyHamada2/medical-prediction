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

# from django.db import models
#
#
# class HealthData (models.Model):
#     age = models.IntegerField (default=50)  # العمر مع قيمة افتراضية
#     sex = models.IntegerField ()  # الجنس، 0 أو 1
#     cp = models.IntegerField ()  # نوع الألم في الصدر، مع قيم محددة
#     trestbps = models.FloatField (default=50)  # ضغط الدم عند الراحة
#     chol = models.FloatField (default=50)  # مستوى الكوليسترول
#     fbs = models.IntegerField (default=0)  # مستوى السكر في الدم بعد الصيام، 0 أو 1
#     restecg = models.IntegerField ()  # تخطيط القلب أثناء الراحة، مع قيم محددة
#     thalachh = models.FloatField (default=50)  # معدل ضربات القلب القصوى
#     exang = models.IntegerField (default=0)  # ألم في الصدر عند المجهود، 0 أو 1
#     oldpeak = models.FloatField (default=50)  # الانخفاض في ST في الراحة
#     slope = models.IntegerField ()  # ميل المقاطع النهائية في اختبار الجهد
#     ca = models.IntegerField (default=0)  # عدد الأوعية الرئيسية المسدودة
#     thal = models.IntegerField ()  # نوع الثالاسيميا، مع قيم محددة
#     target = models.IntegerField (default=50)  # الهدف (مرض القلب أو لا)
#     glucose = models.FloatField (default=50)  # مستوى الجلوكوز
#     cholesterol = models.FloatField (default=50)  # مستوى الكوليسترول
#     hemoglobin = models.FloatField (default=50)  # مستوى الهيموجلوبين
#     heart_disease = models.CharField (max_length=255, blank=True, null=True)  # يمكن أن تكون فارغة
#     diabetes = models.CharField (max_length=255, blank=True, null=True)  # يمكن أن تكون فارغة
#     diabetes_boolean = models.BooleanField (default=False)  # 0 أو 1
#     diagnosis = models.CharField (max_length=255, blank=True, null=True)  # تشخيص الحالة
#     additional_field = models.CharField (max_length=255, blank=True, null=True)  # حقل إضافي
#
#     def __str__(self):
#         return f"Health Data {self.id}"
#
#
# class Symptom (models.Model):
#     name = models.CharField (max_length=100)
#     type = models.CharField (max_length=50, blank=True, null=True)
#
#     def __str__(self):
#         return self.name
#

# from django.db import models
# from django.contrib.auth.models import User
#
#
# # HealthData Model
# class HealthData (models.Model):
#     glucose = models.FloatField (default=50)
#     cholesterol = models.FloatField (default=50)
#     hemoglobin = models.FloatField (default=50)
#     heart_disease = models.CharField (max_length=255, blank=True, null=True)
#     diabetes = models.CharField (max_length=255, blank=True, null=True)
#     diabetes_boolean = models.BooleanField (default=False)
#     diagnosis = models.CharField (max_length=255, blank=True, null=True)
#     additional_field = models.CharField (max_length=255, blank=True, null=True)
#     bp_diastolic = models.FloatField (null=True, blank=True)
#     sg = models.CharField (max_length=50)
#     al = models.CharField (max_length=50)
#     age = models.IntegerField (default=50)
#     sex = models.IntegerField ()
#     cp = models.IntegerField ()
#     trestbps = models.FloatField (default=50)
#     chol = models.FloatField (default=50)
#     fbs = models.IntegerField (default=0)
#     restecg = models.IntegerField ()
#     thalachh = models.FloatField (default=50)
#     exang = models.IntegerField (default=0)
#     oldpeak = models.FloatField (default=50)
#     slope = models.IntegerField ()
#     ca = models.IntegerField (default=0)
#     thal = models.IntegerField ()
#     target = models.IntegerField (default=50)
#
#     def __str__(self):
#         return f"Health Data {self.id}"
#
#
# # Symptom Model
# class Symptom (models.Model):
#     name = models.CharField (max_length=100)
#     type = models.CharField (max_length=50, blank=True, null=True)
#
#     def __str__(self):
#         return self.name
#
#
# class UploadedFile (models.Model):
#     file = models.FileField (upload_to='uploads/')  # هنا يتم رفع الملفات إلى مجلد "uploads"
#     uploaded_at = models.DateTimeField (auto_now_add=True)
#
#     def __str__(self):
#         return self.file.name
#
#
# # Disease Model
# class Disease (models.Model):
#     name = models.CharField (max_length=100)
#     symptoms = models.ManyToManyField (Symptom, related_name='diseases')
#     diagnostic_methods = models.TextField (blank=True, null=True)
#     treatment = models.TextField (blank=True, null=True)
#     recommendations = models.TextField (blank=True, null=True)
#
#     def __str__(self):
#         return self.name
#
#
# # DiseaseSymptom Model
# class DiseaseSymptom (models.Model):
#     disease = models.ForeignKey (Disease, on_delete=models.CASCADE)
#     symptom = models.ForeignKey (Symptom, on_delete=models.CASCADE)
#     severity = models.CharField (
#         max_length=50,
#         choices=[('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe')]
#     )
#
#     def __str__(self):
#         return f"{self.disease.name} - {self.symptom.name} ({self.severity})"
#
#
# # Diagnosis Model
# class Diagnosis (models.Model):
#     health_data = models.ForeignKey (HealthData, on_delete=models.CASCADE, related_name='diagnoses')
#     disease = models.ForeignKey (Disease, on_delete=models.SET_NULL, null=True)
#     symptoms_entered = models.TextField ()
#     diagnostic_methods_used = models.TextField ()
#     final_diagnosis = models.CharField (max_length=255)
#     patient_advice = models.TextField ()
#
#     def __str__(self):
#         return f"Diagnosis of {self.disease.name if self.disease else 'Unknown Disease'}"
#
#
# # AiModels Model
# class AiModels (models.Model):
#     name = models.CharField (max_length=255)
#     description = models.TextField ()
#     accuracy = models.FloatField ()
#     model_file = models.FileField (upload_to='models/')
#
#     def __str__(self):
#         return self.name
#
#
# # Medication Model
# class Medication (models.Model):
#     name = models.CharField (max_length=100)
#     disease = models.ForeignKey (Disease, on_delete=models.CASCADE)
#     dosage = models.CharField (max_length=100)
#     side_effects = models.TextField ()
#     treatment_duration = models.CharField (max_length=100)
#     usage_instructions = models.TextField ()
#
#     def __str__(self):
#         return self.name
#
#
# # XRayTest Model
# class XRayTest (models.Model):
#     test_type = models.CharField (max_length=100)
#     test_date = models.DateTimeField ()
#     results = models.TextField ()
#     attachment = models.FileField (upload_to='xray_tests/')
#
#     def __str__(self):
#         return f"{self.test_type} on {self.test_date}"
#
#
# # MedicalProcedure Model
# class MedicalProcedure (models.Model):
#     name = models.CharField (max_length=100)
#     procedure_date = models.DateTimeField ()
#     responsible_doctor = models.CharField (max_length=255)
#     procedure_details = models.TextField ()
#
#     def __str__(self):
#         return self.name
#
#
# # MedicalAdviceFollowUp Model
# class MedicalAdviceFollowUp (models.Model):
#     advice = models.TextField ()
#     follow_up_date = models.DateTimeField ()
#     patient_instructions = models.TextField ()
#
#     def __str__(self):
#         return f"Advice for {self.follow_up_date}"
#
#
# # ImportedFile Model
# class ImportedFile (models.Model):
#     filename = models.CharField (max_length=255, unique=True)
#     upload_date = models.DateTimeField (auto_now_add=True)
#     file_data = models.FileField (upload_to='uploads/')
#     file_type = models.CharField (
#         max_length=50, blank=True, null=True,
#         choices=[('csv', 'CSV'), ('excel', 'Excel')]
#     )
#
#     def __str__(self):
#         return self.filename
#
#
# # EmailAddress Model
# class EmailAddress (models.Model):
#     email = models.EmailField (unique=True)
#     user = models.ForeignKey (User, on_delete=models.CASCADE, related_name='email_addresses')
#     created_at = models.DateTimeField (auto_now_add=True)
#
#     def __str__(self):
#         return self.email


# from django.db import models
# from django.contrib.auth.models import User
#
#
# # HealthData Model
# class HealthData(models.Model):
#     glucose = models.FloatField(default=50)
#     cholesterol = models.FloatField(default=50)
#     hemoglobin = models.FloatField(default=50)
#     heart_disease = models.CharField(max_length=255, blank=True, null=True)
#     diabetes = models.CharField(max_length=255, blank=True, null=True)
#     diabetes_boolean = models.BooleanField(default=False)
#     diagnosis = models.CharField(max_length=255, blank=True, null=True)
#     additional_field = models.CharField(max_length=255, blank=True, null=True)
#     bp_diastolic = models.FloatField(null=True, blank=True)
#     sg = models.CharField(max_length=50)
#     al = models.CharField(max_length=50)
#     age = models.IntegerField(default=50)
#     sex = models.IntegerField()
#     cp = models.IntegerField()
#     trestbps = models.FloatField(default=50)
#     chol = models.FloatField(default=50)
#     fbs = models.IntegerField(default=0)
#     restecg = models.IntegerField()
#     thalachh = models.FloatField(default=50)
#     exang = models.IntegerField(default=0)
#     oldpeak = models.FloatField(default=50)
#     slope = models.IntegerField()
#     ca = models.IntegerField(default=0)
#     thal = models.IntegerField()
#     target = models.IntegerField(default=50)
#
#     def __str__(self):
#         return f"Health Data {self.id}"
#
#
# # Symptom Model
# class Symptom(models.Model):
#     name = models.CharField(max_length=100)
#     type = models.CharField(max_length=50, blank=True, null=True)
#
#     def __str__(self):
#         return self.name
#
#
# # UploadedFile Model
# class UploadedFile(models.Model):
#     file = models.FileField(upload_to='uploads/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.file.name
#
#
# # Disease Model
# class Disease(models.Model):
#     name = models.CharField(max_length=100)
#     symptoms = models.ManyToManyField(Symptom, related_name='diseases')
#     diagnostic_methods = models.TextField(blank=True, null=True)
#     treatment = models.TextField(blank=True, null=True)
#     recommendations = models.TextField(blank=True, null=True)
#
#     def __str__(self):
#         return self.name
#
#
# # DiseaseSymptom Model
# class DiseaseSymptom(models.Model):
#     disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
#     symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)
#     severity = models.CharField(
#         max_length=50,
#         choices=[('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe')]
#     )
#
#     def __str__(self):
#         return f"{self.disease.name} - {self.symptom.name} ({self.severity})"
#
#
# # Diagnosis Model
# class Diagnosis(models.Model):
#     health_data = models.ForeignKey(HealthData, on_delete=models.CASCADE, related_name='diagnoses')
#     disease = models.ForeignKey(Disease, on_delete=models.SET_NULL, null=True)
#     symptoms_entered = models.TextField()
#     diagnostic_methods_used = models.TextField()
#     final_diagnosis = models.CharField(max_length=255)
#     patient_advice = models.TextField()
#
#     def __str__(self):
#         return f"Diagnosis of {self.disease.name if self.disease else 'Unknown Disease'}"
#
#
# # AIModels Model (دمج النموذجين)
# class AiModels(models.Model):
#     # تعريف الحقول هنا
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     # أي حقول أخرى قد تحتاجها
#
#     def __str__(self):
#         return self.name
#
#
# # Medication Model
# class Medication(models.Model):
#     name = models.CharField(max_length=100)
#     disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
#     dosage = models.CharField(max_length=100)
#     side_effects = models.TextField()
#     treatment_duration = models.CharField(max_length=100)
#     usage_instructions = models.TextField()
#
#     def __str__(self):
#         return self.name
#
#
# # XRayTest Model
# class XRayTest(models.Model):
#     test_type = models.CharField(max_length=100)
#     test_date = models.DateTimeField()
#     results = models.TextField()
#     attachment = models.FileField(upload_to='xray_tests/')
#
#     def __str__(self):
#         return f"{self.test_type} on {self.test_date}"
#
#
# # MedicalProcedure Model
# class MedicalProcedure(models.Model):
#     name = models.CharField(max_length=100)
#     procedure_date = models.DateTimeField()
#     responsible_doctor = models.CharField(max_length=255)
#     procedure_details = models.TextField()
#
#     def __str__(self):
#         return self.name
#
#
# # MedicalAdviceFollowUp Model
# class MedicalAdviceFollowUp(models.Model):
#     advice = models.TextField()
#     follow_up_date = models.DateTimeField()
#     patient_instructions = models.TextField()
#
#     def __str__(self):
#         return f"Advice for {self.follow_up_date}"
#
#
# # ImportedFile Model
# class ImportedFile(models.Model):
#     filename = models.CharField(max_length=255, unique=True)
#     upload_date = models.DateTimeField(auto_now_add=True)
#     file_data = models.FileField(upload_to='uploads/')
#     file_type = models.CharField(
#         max_length=50, blank=True, null=True,
#         choices=[('csv', 'CSV'), ('excel', 'Excel')]
#     )
#
#     def __str__(self):
#         return self.filename
#
#
# # EmailAddress Model
# class EmailAddress(models.Model):
#     email = models.EmailField(unique=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='email_addresses')
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.email


# from django.db import models
# from django.core.management.base import BaseCommand
# import pandas as pd
# from django.contrib.auth.models import User
#
#
# # HealthData Model
# class HealthData (models.Model):
#     glucose = models.FloatField (default=50)
#     cholesterol = models.FloatField (default=50)
#     hemoglobin = models.FloatField (default=50)
#     heart_disease = models.CharField (max_length=255, blank=True, null=True)
#     diabetes = models.CharField (max_length=255, blank=True, null=True)
#     diabetes_boolean = models.BooleanField (default=False)
#     diagnosis = models.CharField (max_length=255, blank=True, null=True)
#     additional_field = models.CharField (max_length=255, blank=True, null=True)
#     bp_diastolic = models.FloatField (null=True, blank=True)
#     sg = models.CharField (max_length=50)
#     al = models.CharField (max_length=50)
#     age = models.IntegerField (default=50)
#     sex = models.IntegerField ()
#     cp = models.IntegerField ()
#     trestbps = models.FloatField (default=50)
#     chol = models.FloatField (default=50)
#     fbs = models.IntegerField (default=0)
#     restecg = models.IntegerField ()
#     thalachh = models.FloatField (default=50)
#     exang = models.IntegerField (default=0)
#     oldpeak = models.FloatField (default=50)
#     slope = models.IntegerField ()
#     ca = models.IntegerField (default=0)
#     thal = models.IntegerField ()
#     target = models.IntegerField (default=50)
#
#     def __str__(self):
#         return f"Health Data {self.id}"
#
#
# # Symptom Model
# class Symptom (models.Model):
#     name = models.CharField (max_length=100)
#     type = models.CharField (max_length=50, blank=True, null=True)
#
#     def __str__(self):
#         return self.name
#
#
# # UploadedFile Model
# class UploadedFile (models.Model):
#     file = models.FileField (upload_to='uploads/')
#     uploaded_at = models.DateTimeField (auto_now_add=True)
#
#     def __str__(self):
#         return self.file.name
#
#
# # Disease Model
# class Disease (models.Model):
#     name = models.CharField (max_length=100)
#     symptoms = models.ManyToManyField (Symptom, related_name='diseases')
#     diagnostic_methods = models.TextField (blank=True, null=True)
#     treatment = models.TextField (blank=True, null=True)
#     recommendations = models.TextField (blank=True, null=True)
#
#     def __str__(self):
#         return self.name
#
#
# # DiseaseSymptom Model
# class DiseaseSymptom (models.Model):
#     disease = models.ForeignKey (Disease, on_delete=models.CASCADE)
#     symptom = models.ForeignKey (Symptom, on_delete=models.CASCADE)
#     severity = models.CharField (
#         max_length=50,
#         choices=[('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe')]
#     )
#
#     def __str__(self):
#         return f"{self.disease.name} - {self.symptom.name} ({self.severity})"
#
#
# # Diagnosis Model
# class Diagnosis (models.Model):
#     health_data = models.ForeignKey (HealthData, on_delete=models.CASCADE, related_name='diagnoses')
#     disease = models.ForeignKey (Disease, on_delete=models.SET_NULL, null=True)
#     symptoms_entered = models.TextField ()
#     diagnostic_methods_used = models.TextField ()
#     final_diagnosis = models.CharField (max_length=255)
#     patient_advice = models.TextField ()
#
#     def __str__(self):
#         return f"Diagnosis of {self.disease.name if self.disease else 'Unknown Disease'}"
#
#
# # AIModels Model
# class AiModels (models.Model):
#     name = models.CharField (max_length=255)
#     description = models.TextField ()
#
#     def __str__(self):
#         return self.name
#
#
# # Medication Model
# class Medication (models.Model):
#     name = models.CharField (max_length=100)
#     disease = models.ForeignKey (Disease, on_delete=models.CASCADE)
#     dosage = models.CharField (max_length=100)
#     side_effects = models.TextField ()
#     treatment_duration = models.CharField (max_length=100)
#     usage_instructions = models.TextField ()
#
#     def __str__(self):
#         return self.name
#
#
# # XRayTest Model
# class XRayTest (models.Model):
#     test_type = models.CharField (max_length=100)
#     test_date = models.DateTimeField ()
#     results = models.TextField ()
#     attachment = models.FileField (upload_to='xray_tests/')
#
#     def __str__(self):
#         return f"{self.test_type} on {self.test_date}"
#
#
# # MedicalProcedure Model
# class MedicalProcedure (models.Model):
#     name = models.CharField (max_length=100)
#     procedure_date = models.DateTimeField ()
#     responsible_doctor = models.CharField (max_length=255)
#     procedure_details = models.TextField ()
#
#     def __str__(self):
#         return self.name
#
#
# # MedicalAdviceFollowUp Model
# class MedicalAdviceFollowUp (models.Model):
#     advice = models.TextField ()
#     follow_up_date = models.DateTimeField ()
#     patient_instructions = models.TextField ()
#
#     def __str__(self):
#         return f"Advice for {self.follow_up_date}"
#
#
# # ImportedFile Model
# class ImportedFile (models.Model):
#     filename = models.CharField (max_length=255, unique=True)
#     upload_date = models.DateTimeField (auto_now_add=True)
#     file_data = models.FileField (upload_to='uploads/')
#     file_type = models.CharField (
#         max_length=50, blank=True, null=True,
#         choices=[('csv', 'CSV'), ('excel', 'Excel')]
#     )
#
#     def __str__(self):
#         return self.filename
#
#
# # EmailAddress Model
# class EmailAddress (models.Model):
#     email = models.EmailField (unique=True)
#     user = models.ForeignKey (User, on_delete=models.CASCADE, related_name='email_addresses')
#     created_at = models.DateTimeField (auto_now_add=True)
#
#     def __str__(self):
#         return self.email
#
#
# # Command to Load Data Dynamically into HealthData Model
# class Command (BaseCommand):
#     help = 'Load data and dynamically create fields in model'
#
#     def handle(self, *args, **kwargs):
#         file_path = 'path_to_file.csv'  # ضع المسار الفعلي للملف هنا
#         df = pd.read_csv (file_path)
#
#         # إنشاء الحقول ديناميكيًا بناءً على الأعمدة في الملف
#         self.create_dynamic_fields (df)
#
#     def create_dynamic_fields(self, df):
#         columns = df.columns
#
#         for column in columns:
#             if not hasattr (HealthData, column):  # تأكد من عدم وجود الحقل مسبقًا
#                 column_type = df[column].dtype
#
#                 if column_type == 'float64':
#                     field = models.FloatField (null=True, blank=True)
#                 elif column_type == 'int64':
#                     field = models.IntegerField (null=True, blank=True)
#                 elif column_type == 'bool':
#                     field = models.BooleanField (default=False)
#                 elif column_type == 'datetime64[ns]':  # دعم لـ DateTime
#                     field = models.DateTimeField (null=True, blank=True)
#                 elif column_type == 'object':  # نصوص أو تواريخ
#                     field = models.CharField (max_length=255, blank=True, null=True)
#                 else:
#                     field = models.CharField (max_length=255, blank=True, null=True)
#
#                 field.contribute_to_class (HealthData, column)
#
#         self.stdout.write (self.style.SUCCESS ("تم إنشاء الحقول ديناميكيًا"))

# from django.db import models
# from django.core.management.base import BaseCommand
# import pandas as pd
# from django.contrib.auth.models import User
#
#
# class HealthData (models.Model):
#     # الأعمدة التي تم إضافتها حديثًا
#     bp_diastolic = models.FloatField (null=True, blank=True)
#     bp_limit = models.CharField (max_length=100, blank=True, null=True)
#     sg = models.FloatField (null=True, blank=True)
#     al = models.CharField (max_length=100, blank=True, null=True)
#     class_value = models.CharField (max_length=100, blank=True, null=True)
#     rbc = models.CharField (max_length=100, blank=True, null=True)
#     su = models.CharField (max_length=100, blank=True, null=True)
#     pc = models.CharField (max_length=100, blank=True, null=True)
#     pcc = models.CharField (max_length=100, blank=True, null=True)
#     ba = models.CharField (max_length=100, blank=True, null=True)
#     bgr = models.FloatField (null=True, blank=True)
#     bu = models.FloatField (null=True, blank=True)
#     sod = models.FloatField (null=True, blank=True)
#     sc = models.FloatField (null=True, blank=True)
#     pot = models.FloatField (null=True, blank=True)
#     hemo = models.FloatField (null=True, blank=True)
#     pcv = models.FloatField (null=True, blank=True)
#     rbcc = models.FloatField (null=True, blank=True)
#     wbcc = models.FloatField (null=True, blank=True)
#     htn = models.CharField (max_length=100, blank=True, null=True)
#     dm = models.CharField (max_length=100, blank=True, null=True)
#     cad = models.CharField (max_length=100, blank=True, null=True)
#     appet = models.CharField (max_length=100, blank=True, null=True)
#     pe = models.CharField (max_length=100, blank=True, null=True)
#     ane = models.CharField (max_length=100, blank=True, null=True)
#     grf = models.CharField (max_length=100, blank=True, null=True)
#     stage = models.CharField (max_length=100, blank=True, null=True)
#     affected = models.CharField (max_length=100, blank=True, null=True)
#     age = models.IntegerField (null=True, blank=True)
#     sex = models.CharField (max_length=1, choices=[('m', 'Male'), ('f', 'Female')], default='f')
#
#     # الأعمدة القديمة التي كانت في النموذج الحالي
#     glucose = models.FloatField (default=50)
#     cholesterol = models.FloatField (default=50)
#     hemoglobin = models.FloatField (default=50)
#     heart_disease = models.CharField (max_length=255, blank=True, null=True)
#     diabetes = models.CharField (max_length=255, blank=True, null=True)
#     diabetes_boolean = models.BooleanField (default=False)
#     diagnosis = models.CharField (max_length=255, blank=True, null=True)
#     additional_field = models.CharField (max_length=255, blank=True, null=True)
#
#     # الأعمدة الطبية الخاصة بالقلب
#     cp = models.IntegerField ()
#     trestbps = models.FloatField (default=50)
#     chol = models.FloatField (default=50)
#     fbs = models.IntegerField (default=0)
#     restecg = models.IntegerField ()
#     thalachh = models.FloatField (default=50)
#     exang = models.IntegerField (default=0)
#     oldpeak = models.FloatField (default=50)
#     slope = models.IntegerField ()
#     ca = models.IntegerField (default=0)
#     thal = models.IntegerField ()
#     target = models.IntegerField (default=50)
#
#     def __str__(self):
#         return f"Health Data {self.id}"
#
#
# # باقي النماذج التي تتابعها
# class Symptom (models.Model):
#     name = models.CharField (max_length=100)
#     type = models.CharField (max_length=50, blank=True, null=True)
#
#     def __str__(self):
#         return self.name
#
#
# class UploadedFile (models.Model):
#     file = models.FileField (upload_to='uploads/')
#     uploaded_at = models.DateTimeField (auto_now_add=True)
#
#     def __str__(self):
#         return self.file.name
#
#
# class Disease (models.Model):
#     name = models.CharField (max_length=100)
#     symptoms = models.ManyToManyField (Symptom, related_name='diseases')
#     diagnostic_methods = models.TextField (blank=True, null=True)
#     treatment = models.TextField (blank=True, null=True)
#     recommendations = models.TextField (blank=True, null=True)
#
#     def __str__(self):
#         return self.name
#
#
# class DiseaseSymptom (models.Model):
#     disease = models.ForeignKey (Disease, on_delete=models.CASCADE)
#     symptom = models.ForeignKey (Symptom, on_delete=models.CASCADE)
#     severity = models.CharField (
#         max_length=50,
#         choices=[('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe')]
#     )
#
#     def __str__(self):
#         return f"{self.disease.name} - {self.symptom.name} ({self.severity})"
#
#
# class Diagnosis (models.Model):
#     health_data = models.ForeignKey (HealthData, on_delete=models.CASCADE, related_name='diagnoses')
#     disease = models.ForeignKey (Disease, on_delete=models.SET_NULL, null=True)
#     symptoms_entered = models.TextField ()
#     diagnostic_methods_used = models.TextField ()
#     final_diagnosis = models.CharField (max_length=255)
#     patient_advice = models.TextField ()
#
#     def __str__(self):
#         return f"Diagnosis of {self.disease.name if self.disease else 'Unknown Disease'}"
#
#
# class AiModels (models.Model):
#     name = models.CharField (max_length=255)
#     description = models.TextField ()
#
#     def __str__(self):
#         return self.name
#
#
# class Medication (models.Model):
#     name = models.CharField (max_length=100)
#     disease = models.ForeignKey (Disease, on_delete=models.CASCADE)
#     dosage = models.CharField (max_length=100)
#     side_effects = models.TextField ()
#     treatment_duration = models.CharField (max_length=100)
#     usage_instructions = models.TextField ()
#
#     def __str__(self):
#         return self.name
#
#
# class XRayTest (models.Model):
#     test_type = models.CharField (max_length=100)
#     test_date = models.DateTimeField ()
#     results = models.TextField ()
#     attachment = models.FileField (upload_to='xray_tests/')
#
#     def __str__(self):
#         return f"{self.test_type} on {self.test_date}"
#
#
# class MedicalProcedure (models.Model):
#     name = models.CharField (max_length=100)
#     procedure_date = models.DateTimeField ()
#     responsible_doctor = models.CharField (max_length=255)
#     procedure_details = models.TextField ()
#
#     def __str__(self):
#         return self.name
#
#
# class MedicalAdviceFollowUp (models.Model):
#     advice = models.TextField ()
#     follow_up_date = models.DateTimeField ()
#     patient_instructions = models.TextField ()
#
#     def __str__(self):
#         return f"Advice for {self.follow_up_date}"
#
#
# class ImportedFile (models.Model):
#     filename = models.CharField (max_length=255, unique=True)
#     upload_date = models.DateTimeField (auto_now_add=True)
#     file_data = models.FileField (upload_to='uploads/')
#     file_type = models.CharField (
#         max_length=50, blank=True, null=True,
#         choices=[('csv', 'CSV'), ('excel', 'Excel')]
#     )
#
#     def __str__(self):
#         return self.filename
#
#
# class EmailAddress (models.Model):
#     email = models.EmailField (unique=True)
#     user = models.ForeignKey (User, on_delete=models.CASCADE, related_name='email_addresses')
#     created_at = models.DateTimeField (auto_now_add=True)
#
#     def __str__(self):
#         return self.email
#
#
# # Command to Load Data Dynamically into HealthData Model
# class Command (BaseCommand):
#     help = 'Load data and dynamically create fields in model'
#
#     def handle(self, *args, **kwargs):
#         file_path = 'path_to_file.csv'  # ضع المسار الفعلي للملف هنا
#         df = pd.read_csv (file_path)
#
#         # إنشاء الحقول ديناميكيًا بناءً على الأعمدة في الملف
#         self.create_dynamic_fields (df)
#
#     def create_dynamic_fields(self, df):
#         columns = df.columns
#
#         for column in columns:
#             if not hasattr (HealthData, column):  # تأكد من عدم وجود الحقل مسبقًا
#                 column_type = df[column].dtype
#
#                 if column_type == 'float64':
#                     field = models.FloatField (null=True, blank=True)
#                 elif column_type == 'int64':
#                     field = models.IntegerField (null=True, blank=True)
#                 elif column_type == 'bool':
#                     field = models.BooleanField (default=False)
#                 elif column_type == 'object':
#                     field = models.CharField (max_length=255, blank=True, null=True)
#
#                 # إضافة الحقل إلى HealthData
#                 field.contribute_to_class (HealthData, column)
#
#         # الآن قم بحفظ التغييرات
#         self.stdout.write (self.style.SUCCESS (f'Successfully added dynamic fields for {len (columns)} columns.'))


import csv
import pandas as pd
from django.db import models
from django.core.management.base import BaseCommand
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class AIModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class HealthData(models.Model):
    # الأعمدة الطبية الأساسية
    glucose = models.FloatField(default=50)
    cholesterol = models.FloatField(default=50)
    hemoglobin = models.FloatField(default=50)

    # الأعمدة الجديدة
    bp_diastolic = models.FloatField(null=True, blank=True)
    bp_limit = models.CharField(max_length=100, blank=True, null=True)
    sg = models.FloatField(null=True, blank=True)
    al = models.CharField(max_length=100, blank=True, null=True)
    class_value = models.CharField(max_length=100, blank=True, null=True)
    rbc = models.CharField(max_length=100, blank=True, null=True)
    su = models.CharField(max_length=100, blank=True, null=True)
    pc = models.CharField(max_length=100, blank=True, null=True)
    pcc = models.CharField(max_length=100, blank=True, null=True)
    ba = models.CharField(max_length=100, blank=True, null=True)
    bgr = models.FloatField(null=True, blank=True)
    bu = models.FloatField(null=True, blank=True)
    sod = models.FloatField(null=True, blank=True)
    sc = models.FloatField(null=True, blank=True)
    pot = models.FloatField(null=True, blank=True)
    hemo = models.FloatField(null=True, blank=True)
    pcv = models.FloatField(null=True, blank=True)
    rbcc = models.FloatField(null=True, blank=True)
    wbcc = models.FloatField(null=True, blank=True)
    htn = models.CharField(max_length=100, blank=True, null=True)
    dm = models.CharField(max_length=100, blank=True, null=True)
    cad = models.CharField(max_length=100, blank=True, null=True)
    appet = models.CharField(max_length=100, blank=True, null=True)
    pe = models.CharField(max_length=100, blank=True, null=True)
    ane = models.CharField(max_length=100, blank=True, null=True)
    grf = models.CharField(max_length=100, blank=True, null=True)
    stage = models.CharField(max_length=100, blank=True, null=True)
    affected = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField(null=True, blank=True)
    sex = models.CharField(
        max_length=1, choices=[("m", "Male"), ("f", "Female")], default="f"
    )

    # الأعمدة الطبية الخاصة بالقلب
    cp = models.IntegerField()
    trestbps = models.FloatField(default=50)
    chol = models.FloatField(default=50)
    fbs = models.IntegerField(default=0)
    restecg = models.IntegerField()
    thalachh = models.FloatField(default=50)
    exang = models.IntegerField(default=0)
    oldpeak = models.FloatField(default=50)
    slope = models.IntegerField()
    ca = models.IntegerField(default=0)
    thal = models.IntegerField()
    target = models.IntegerField(default=50)

    # الحقول الخاصة بالصحة العامة
    heart_disease = models.BooleanField(default=False)
    diabetes = models.BooleanField(default=False)
    diagnosis = models.TextField(null=True, blank=True)
    additional_field = models.CharField(max_length=255, null=True, blank=True)

    # حقل لتحميل ملفات CSV
    csv_file = models.FileField(upload_to="csv_files/", blank=True, null=True)

    def __str__(self):
        return f"HealthData {self.id}"


# نموذج XRayTest
class XRayTest(models.Model):
    test_name = models.CharField(max_length=255)
    result = models.TextField()
    date_conducted = models.DateField()
    patient = models.ForeignKey(HealthData, on_delete=models.CASCADE)

    def __str__(self):
        return self.test_name


# نموذج MedicalProcedure
class MedicalProcedure(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date_performed = models.DateField()
    patient = models.ForeignKey(HealthData, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# دالة لاستيراد البيانات من ملف CSV
def import_csv_data(file_path):
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            HealthData.objects.create(
                glucose=row.get("Glucose", 0),
                cholesterol=row.get("Cholesterol", 0),
                hemoglobin=row.get("Hemoglobin", 0),
                bp_diastolic=row.get("Bp diastolic", 0),
                bp_limit=row.get("Bp limit", 0),
                target=row.get("Target", ""),
                diagnosis=row.get("Diagnosis", ""),
            )


# Signal to Process CSV on Upload
@receiver(post_save, sender=HealthData)
def process_csv_on_upload(sender, instance, created, **kwargs):
    if created and instance.csv_file:
        import_csv_data(instance.csv_file.path)


# نموذج Medication
class Medication(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    dose = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


# نماذج أخرى
class Symptom(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Diagnosis(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Disease(models.Model):
    name = models.CharField(max_length=100)
    symptoms = models.ManyToManyField(Symptom, related_name="diseases")
    diagnostic_methods = models.TextField(blank=True, null=True)
    treatment = models.TextField(blank=True, null=True)
    recommendations = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class AiModels(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# نموذج MedicalAdviceFollowUp
class MedicalAdviceFollowUp(models.Model):
    patient = models.ForeignKey(HealthData, on_delete=models.CASCADE)
    advice = models.TextField()
    date_given = models.DateField()

    def __str__(self):
        return f"Advice for {self.patient.id} on {self.date_given}"


# Command to Load Data Dynamically into HealthData Model
class Command(BaseCommand):
    help = "تحميل البيانات وإنشاء الحقول الديناميكية في نموذج HealthData"

    def handle(self, *args, **kwargs):
        file_path = "path_to_file.csv"  # ضع المسار الفعلي للملف هنا
        df = pd.read_csv(file_path)

        # إنشاء الحقول ديناميكيًا بناءً على الأعمدة في الملف
        self.create_dynamic_fields(df)

    def create_dynamic_fields(self, df):
        columns = df.columns

        for column in columns:
            if not hasattr(HealthData, column):  # تأكد من عدم وجود الحقل مسبقًا
                column_type = df[column].dtype

                if column_type == "float64":
                    field = models.FloatField(null=True, blank=True)
                elif column_type == "object":
                    field = models.CharField(max_length=255, blank=True, null=True)
                else:
                    field = models.CharField(max_length=255, blank=True, null=True)

                # إضافة الحقل بشكل ديناميكي إلى نموذج HealthData
                field.contribute_to_class(HealthData, column)

        # حفظ النموذج بعد تعديل الحقول
        HealthData.objects.create(**df.iloc[0].to_dict())
