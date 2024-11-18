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

from django.contrib import admin
from .models import (
    # AiModels,  # تم تعديل AIModel إلى AiModels
    HealthData,
    Disease,
    Diagnosis,
    Medication,
    XRayTest,
    MedicalProcedure,
    MedicalAdviceFollowUp,
)


# تسجيل النموذج AiModels في واجهة الإدارة
# @admin.register (AiModels)
# class AiModelsAdmin (admin.ModelAdmin):
#     list_display = ('name', 'description')  # عرض الأعمدة المناسبة في واجهة الإدارة
#     search_fields = ('name',)  # تفعيل البحث باستخدام اسم النموذج


# تسجيل النماذج الأخرى في واجهة الإدارة
admin.site.register (HealthData)
admin.site.register (Disease)
admin.site.register (Diagnosis)
admin.site.register (Medication)
admin.site.register (XRayTest)
admin.site.register (MedicalProcedure)
admin.site.register (MedicalAdviceFollowUp)

try:
    from .models import AiModels
except ImportError as e:
    print(f"Error importing AiModels: {e}")
