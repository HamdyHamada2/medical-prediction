# from django.contrib import admin
# from .models import HealthData
#
# admin.site.register(HealthData)


from django.contrib import admin
from .models import Disease, Diagnosis, Medication, XRayTest, MedicalProcedure, MedicalAdviceFollowUp, AIModel

admin.site.register(Disease)
admin.site.register(Diagnosis)
admin.site.register(Medication)
admin.site.register(XRayTest)
admin.site.register(MedicalProcedure)
admin.site.register(MedicalAdviceFollowUp)
admin.site.register(AIModel)
