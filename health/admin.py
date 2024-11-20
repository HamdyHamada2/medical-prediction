# from django.contrib import admin
# from .models import HealthData
#
# admin.site.register(HealthData)


# from django.contrib import admin
# from .models import Disease, Diagnosis, Medication, XRayTest, MedicalProcedure, MedicalAdviceFollowUp, AIModel
# from .models import HealthData
#
#
# # تسجيل النماذج في واجهة الإدارة
# admin.site.register(HealthData)
# admin.site.register(Disease)
# admin.site.register(Diagnosis)
# admin.site.register(Medication)
# admin.site.register(XRayTest)
# admin.site.register(MedicalProcedure)
# admin.site.register(MedicalAdviceFollowUp)
# admin.site.register(AIModel)

# from django.contrib import admin
# from .models import (
#     # AiModels,  # تم تعديل AIModel إلى AiModels
#     HealthData,
#     Disease,
#     Diagnosis,
#     Medication,
#     XRayTest,
#     MedicalProcedure,
#     MedicalAdviceFollowUp,
# )
#
#
# # تسجيل النموذج AiModels في واجهة الإدارة
# # @admin.register (AiModels)
# # class AiModelsAdmin (admin.ModelAdmin):
# #     list_display = ('name', 'description')  # عرض الأعمدة المناسبة في واجهة الإدارة
# #     search_fields = ('name',)  # تفعيل البحث باستخدام اسم النموذج
#
#
# # تسجيل النماذج الأخرى في واجهة الإدارة
# admin.site.register (HealthData)
# admin.site.register (Disease)
# admin.site.register (Diagnosis)
# admin.site.register (Medication)
# admin.site.register (XRayTest)
# admin.site.register (MedicalProcedure)
# admin.site.register (MedicalAdviceFollowUp)
#
# try:
#     from .models import AiModels
# except ImportError as e:
#     print(f"Error importing AiModels: {e}")


# from import_export import resources
# from import_export.admin import ExportMixin
# from django.contrib import admin
# from .models import (
#     HealthData,
#     Disease,
#     Diagnosis,
#     Medication,
#     XRayTest,
#     MedicalProcedure,
#     MedicalAdviceFollowUp,
# )
#
# # استيراد وتسجيل HealthData مع دعم الاستيراد والتصدير
# class HealthDataResource(resources.ModelResource):
#     class Meta:
#         model = HealthData
#
# class HealthDataAdmin(ExportMixin, admin.ModelAdmin):
#     resource_class = HealthDataResource
#
# admin.site.register(HealthData, HealthDataAdmin)
#
# # تسجيل النماذج الأخرى في واجهة الإدارة
# # admin.site.register(HealthData)
# admin.site.register(Disease)
# admin.site.register(Diagnosis)
# admin.site.register(Medication)
# admin.site.register(XRayTest)
# admin.site.register(MedicalProcedure)
# admin.site.register(MedicalAdviceFollowUp)
#
# # محاولة استيراد نموذج AiModels في حال كان موجودًا
# try:
#     from .models import AiModels
# except ImportError as e:
#     print(f"Error importing AiModels: {e}")


from django import forms
from django.contrib import admin, messages
from django.core.exceptions import ValidationError
from django.db import transaction
from import_export.admin import ExportMixin, ImportMixin
from import_export import resources
import pandas as pd
from .models import HealthData, Disease, Diagnosis, Medication, XRayTest, MedicalProcedure, MedicalAdviceFollowUp, \
    AiModels
import logging
from django.urls import path
from django.template.response import TemplateResponse

# إعداد نظام تسجيل الأخطاء
logger = logging.getLogger (__name__)


# تعريف Resource للنموذج HealthData لدعم التصدير والاستيراد
class HealthDataResource (resources.ModelResource):
    class Meta:
        model = HealthData


# تعريف دالة لفحص حجم الملف
def validate_file_size(file):
    max_size = 100 * 1024 * 1024  # 100MB
    if file.size > max_size:
        raise ValidationError ("حجم الملف يجب ألا يتجاوز 100 ميغابايت.")


# نموذج تحميل الملفات
class UploadCSVForm (forms.Form):
    csv_file = forms.FileField (label="اختر ملف CSV", required=True)


# تخصيص إدارة HealthData مع دعم التصدير والاستيراد
class HealthDataAdmin (ExportMixin, ImportMixin, admin.ModelAdmin):
    resource_class = HealthDataResource
    import_export_args = {
        'import_resource_class': HealthDataResource
    }

    list_display = [  # تظل كما هي
        'heart_disease', 'diabetes', 'diagnosis', 'additional_field', 'bp_diastolic', 'bp_limit',
        'sg', 'al', 'class_value', 'rbc', 'su', 'pc', 'pcc', 'ba', 'bgr', 'bu', 'sod', 'sc',
        'pot', 'hemo', 'pcv', 'rbcc', 'wbcc', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane', 'grf',
        'stage', 'affected', 'age', 'sex', 'glucose', 'cholesterol', 'hemoglobin', 'cp', 'trestbps',
        'chol', 'fbs', 'restecg', 'thalachh', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target'
    ]
    search_fields = ['age', 'sex', 'glucose', 'cholesterol']
    list_filter = ['age', 'sex', 'heart_disease', 'diabetes']
    actions = ['import_csv']

    def import_csv(self, request, queryset):
        if 'csv_file' in request.FILES:
            csv_file = request.FILES['csv_file']
            try:
                validate_file_size (csv_file)
            except ValidationError as e:
                self.message_user (request, str (e), level='error')
                return

            try:
                df = pd.read_csv (csv_file)
            except Exception as e:
                self.message_user (request, f"حدث خطأ أثناء قراءة الملف: {str (e)}", level='error')
                return

            REQUIRED_COLUMNS = ['age', 'sex', 'glucose', 'cholesterol', 'hemoglobin']
            if not all (col in df.columns for col in REQUIRED_COLUMNS):
                self.message_user (request, "الملف مفقود بعض الأعمدة المطلوبة.", level='error')
                return

            if df.isnull ().values.any ():
                self.message_user (request, "الملف يحتوي على قيم مفقودة. يرجى التحقق من البيانات.", level='error')
                return

            data_to_create = []
            for index, row in df.iterrows ():
                if HealthData.objects.filter (age=row.get ('age'), sex=row.get ('sex'),
                                              glucose=row.get ('glucose')).exists ():
                    self.message_user (request,
                                       f"السجل مع age: {row.get ('age')} و sex: {row.get ('sex')} موجود بالفعل.",
                                       level='warning')
                    continue

                data_to_create.append (HealthData (
                    age=row.get ('age'),
                    sex=row.get ('sex'),
                    glucose=row.get ('glucose'),
                    cholesterol=row.get ('cholesterol'),
                    hemoglobin=row.get ('hemoglobin'),
                    # أكمل باقي الأعمدة حسب البيانات في ملف CSV
                ))

            with transaction.atomic ():
                HealthData.objects.bulk_create (data_to_create)

            self.message_user (request, f"تم استيراد البيانات بنجاح! تم إضافة {len (data_to_create)} سجلات.",
                               level='success')

    import_csv.short_description = "استيراد البيانات من ملف CSV"

    def get_urls(self):
        urls = super ().get_urls ()
        custom_urls = [
            path ('upload-csv/', self.admin_site.admin_view (self.upload_csv), name="upload_csv"),
        ]
        return custom_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
            form = UploadCSVForm (request.POST, request.FILES)
            if form.is_valid ():
                csv_file = request.FILES['csv_file']
                try:
                    if not csv_file.name.endswith ('.csv'):
                        raise ValidationError ("الملف يجب أن يكون من نوع CSV.")

                    # التعامل مع البيانات بشكل آمن هنا
                    # باقي المنطق كما هو
                except Exception as e:
                    logger.error (f"Error uploading CSV: {e}")
                    self.message_user (request, f"خطأ أثناء رفع الملف: {str (e)}", level=messages.ERROR)
            else:
                self.message_user (request, "صيغة الملف غير صحيحة.", level=messages.ERROR)

        form = UploadCSVForm ()
        return TemplateResponse (request, "admin/healthdata_changelist.html", {"form": form, "title": "رفع ملف CSV"})


# تسجيل النموذج في واجهة الإدارة مع دعم التصدير والاستيراد
admin.site.register (HealthData, HealthDataAdmin)
admin.site.register (Disease)
admin.site.register (Diagnosis)
admin.site.register (Medication)
admin.site.register (XRayTest)
admin.site.register (MedicalProcedure)
admin.site.register (MedicalAdviceFollowUp)

# محاولة استيراد AiModels إذا كان موجودًا
try:
    from .models import AiModels

    admin.site.register (AiModels)
except ImportError as e:
    print (f"Error importing AiModels: {e}")
