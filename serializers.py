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

#
# from rest_framework import serializers
# from .models import HealthData
#
#
# def validate_disease(value):
#     if not value:
#         raise serializers.ValidationError ("Disease field cannot be empty")
#     return value
#
#
# class HealthDataSerializer (serializers.ModelSerializer):
#     # إذا كنت ترغب في إضافة تنسيق مخصص لحقل التاريخ، يمكنك إلغاء التعليق عن السطر التالي وضبطه حسب الحقل الموجود
#     date = serializers.DateTimeField (format='%Y-%m-%d %H:%M:%S', required=False)  # مثال على التنسيق المخصص
#
#     class Meta:
#         model = HealthData
#         fields = '__all__'  # جلب كل الحقول من HealthData
#
#     # مثال على التحقق من صحة حقل معين


# from rest_framework import serializers
# from .models import HealthData, AiModels, AIModel
#
#
# # وظيفة للتحقق من صحة حقل المرض
# def validate_disease(value):
#     if not value:
#         raise serializers.ValidationError("Disease field cannot be empty")
#     return value
#
#
# # Serializer لنموذج HealthData
# class HealthDataSerializer(serializers.ModelSerializer):
#     # إذا كنت ترغب في إضافة تنسيق مخصص لحقل التاريخ، يمكنك إلغاء التعليق عن السطر التالي وضبطه حسب الحقل الموجود
#     date = serializers.DateTimeField(
#         format="%Y-%m-%d %H:%M:%S", required=False
#     )  # مثال على التنسيق المخصص
#
#     # إضافة التحقق المخصص على حقل المرض
#     disease = serializers.CharField(validators=[validate_disease])
#
#     class Meta:
#         model = HealthData
#         fields = "__all__"  # جلب كل الحقول من HealthData
#
#
# # Serializer لنموذج AiModels
# class AiModelsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AiModels
#         fields = "__all__"
#
#
# # Serializer لنموذج AIModel
# class AIModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AIModel
#         fields = "__all__"


from rest_framework import serializers
from .models import HealthData, AiModels, AIModel
from rest_framework.views import APIView


# وظيفة للتحقق من صحة حقل المرض
def validate_disease(value):
    if not value:
        raise serializers.ValidationError ("Disease field cannot be empty")
    return value


# Serializer لنموذج HealthData
class HealthDataSerializer (serializers.ModelSerializer):
    # إذا كنت ترغب في إضافة تنسيق مخصص لحقل التاريخ، يمكنك إلغاء التعليق عن السطر التالي وضبطه حسب الحقل الموجود
    date = serializers.DateTimeField (format="%Y-%m-%d %H:%M:%S", required=False)

    # إضافة التحقق المخصص على حقل المرض
    disease = serializers.CharField (validators=[validate_disease])

    class Meta:
        model = HealthData
        fields = "__all__"


# Serializer لنموذج AiModels
class AiModelsSerializer (serializers.ModelSerializer):
    class Meta:
        model = AiModels
        fields = "__all__"


# Serializer لنموذج AIModel
class AIModelSerializer (serializers.ModelSerializer):
    class Meta:
        model = AIModel
        fields = "__all__"


class LoginSerializer (serializers.Serializer):
    username = serializers.CharField ()
    password = serializers.CharField ()


class LoginView (APIView):
    def post(self, request):
        serializer = LoginSerializer (data=request.data)
        if serializer.is_valid ():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            # نفس المنطق السابق للتحقق من صحة بيانات الاعتماد
        else:
            return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
