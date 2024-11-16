# from rest_framework import serializers
# from .models import HealthData
#
# class HealthDataSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HealthData
#         fields = '__all__'  # يمكنك استبداله بحقول محددة إذا لزم الأمر
#
#     # مثال على التحقق من صحة البيانات
#     def validate_disease(self, value):
#         if not value:
#             raise serializers.ValidationError("Disease field cannot be empty")
#         return value
#
#     # مثال على استخدام التنسيق المخصص
#     # date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')


from rest_framework import serializers
from .models import HealthData


def validate_disease(value):
    if not value:
        raise serializers.ValidationError ("Disease field cannot be empty")
    return value


class HealthDataSerializer (serializers.ModelSerializer):
    # إذا كنت ترغب في إضافة تنسيق مخصص لحقل التاريخ، يمكنك إلغاء التعليق عن السطر التالي وضبطه حسب الحقل الموجود
    date = serializers.DateTimeField (format='%Y-%m-%d %H:%M:%S', required=False)  # مثال على التنسيق المخصص

    class Meta:
        model = HealthData
        fields = '__all__'  # جلب كل الحقول من HealthData

    # مثال على التحقق من صحة حقل معين
