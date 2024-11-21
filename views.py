# from typing import Hashable
# from django.http import HttpResponse, JsonResponse
# from django.shortcuts import render, redirect
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.forms import AuthenticationForm
# from .forms import CustomSignupForm, LoginForm
# from .models import HealthData, ImportedFile
# from .serializers import HealthDataSerializer
# from django.views.generic import ListView
# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page
# from celery.result import AsyncResult
# from health.tasks import add
# import json
# import pandas as pd
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import filters, permissions, viewsets
#
#
# # معالج الاستثناءات المخصص
# def custom_exception_handler(exc, context):
#     response = exception_handler(exc, context)
#     if response is not None:
#         response.data['status_code'] = response.status_code
#     return response
#
#
# # تطبيق الـ cache على الـ API لمدة 15 دقيقة
# @method_decorator(cache_page(60 * 15), name='dispatch')  # 15 دقيقة تخزين مؤقت
# class HealthDataViewSet(viewsets.ModelViewSet):
#     """
#     ViewSet لعرض البيانات الطبية مثل الأعراض والأمراض.
#     يشمل الفلترة والتخزين المؤقت.
#     """
#     queryset = HealthData.objects.all()
#     serializer_class = HealthDataSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#     # إضافة الفلترة باستخدام DjangoFilterBackend
#     filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
#     filterset_fields = ['symptoms', 'disease']  # الحقول التي تريد تمكين الفلترة عليها
#     ordering_fields = ['symptoms', 'disease']  # الحقول التي يمكن ترتيبها
#     ordering = ['symptoms']  # ترتيب البيانات افتراضيًا حسب الأعراض
#
#     # تخصيص طريقة GET لاسترجاع البيانات بناءً على ID
#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()  # سيقوم بجلب العنصر بناءً على ID
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)
#
#     # إضافة استثناءات مخصصة للـ ViewSet
#     def get_exception_handler(self):
#         return custom_exception_handler
#
#
# # عرض البيانات عبر API
# def get(request):
#     # ضع هنا المنطق الخاص بتوقع الحالات الصحية أو البيانات التي تريد عرضها
#     data = {"message": "Hello, world!"}
#     return Response(data, status=status.HTTP_200_OK)
#
#
# # عرض الصفحة الرئيسية
# def home_view(request):
#     return HttpResponse("Welcome to the Health Prediction API!")
#
#
# def predict_view(request):
#     return HttpResponse("Prediction Results")
#
#
# # اختبار التخزين المؤقت
# def test_cache(request):
#     return HttpResponse("Cache Test Successful!")
#
#
# # اختبار مهمة Celery
# def test_task(request):
#     result = add.delay(10, 20)  # إرسال المهمة بشكل غير متزامن
#     return JsonResponse({"task_id": result.id, "status": "Task is running"})
#
#
# # الحصول على حالة المهمة
# def get_task_status(request, task_id):
#     result = AsyncResult(task_id)
#     if result.ready():
#         return JsonResponse({"task_id": task_id, "status": "Completed", "result": result.result})
#     else:
#         return JsonResponse({"task_id": task_id, "status": "In Progress"})
#
#
# # إضافة الأعداد باستخدام GET أو POST
# def add_numbers(request):
#     if request.method == 'GET':
#         try:
#             a = int(request.GET.get('a', 0))
#             b = int(request.GET.get('b', 0))
#             result = a + b
#             return JsonResponse({'result': result})
#
#         except ValueError:
#             return JsonResponse({'error': 'Invalid input. Please provide valid integers for a and b in the query '
#                                           'string.'}, status=400)
#
#     elif request.method == 'POST':
#         try:
#             data = request.data  # استخدم request.data في DRF
#             a = int(data.get('a', 0))
#             b = int(data.get('b', 0))
#             result = a + b
#             return JsonResponse({'result': result})
#
# except ValueError: return JsonResponse({'error': 'Invalid input. Please provide valid integers for a and b in the
# POST body.'}, status=400)
#
#     else:
#         return JsonResponse({'error': 'Only GET and POST requests are allowed.'}, status=405)
#
#
# def my_view(request):
#     # استدعاء المهمة
#     result = add.delay(4, 6)
#     return JsonResponse({'task_id': result.id})
#
#
# # صفحة تسجيل الدخول
# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 form.add_error(None, 'Invalid login credentials')
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})
#
#
# # تسجيل الخروج
# def logout_view(request):
#     logout(request)
#     return redirect('login')
#
#
# # دالة لتحميل البيانات من ملفات CSV
# def import_data_from_csv(file_path):
#     df = pd.read_csv(file_path)
#
#     # تمر عبر كل صف في الملف
#     IND: Hashable
#     for IND, row in df.iterrows():
#         row_data = row.to_dict()
#         # تحويل البيانات إلى JSON بشكل صحيح
#         row_data_json = json.dumps(row_data)
#
#         # استخراج التشخيص (تأكد من وجود الحقل)
#         diagnosis = row_data.pop('diagnosis', '')
#
#         # إضافة البيانات إلى HealthData
#         health_data = HealthData.objects.create(
#             data=row_data_json,
#             diagnosis=diagnosis
#         )
#
#         print(f"Data added for row {IND + 1}: {row_data} with diagnosis: {diagnosis}")
#
#
# # نموذج لتحميل الملفات المستوردة
# def import_file(request):
#     if request.method == 'POST' and request.FILES['file']:
#         uploaded_file = request.FILES['file']
#
#         # حفظ الملف في المجلد المناسب
#         imported_file = ImportedFile.objects.create(
#             filename=uploaded_file.name,
#             file_data=uploaded_file,
#             file_type='csv'  # افتراض أن نوع الملف هو CSV
#         )
#
#         # استيراد البيانات من CSV
#         import_data_from_csv(imported_file.file_data.path)
#
#         return redirect('home')
#     return render(request, 'import_file.html')
#
#
# # عرض البيانات عبر HTML
# class HealthDataHTMLView(ListView):
#     model = HealthData
#     template_name = 'health/health_data_list.html'
#     context_object_name = 'health_data_list'
#
#
# # صفحة التسجيل
# def signup_view(request):
#     if request.method == 'POST':
#         form = CustomSignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#     else:
#         form = CustomSignupForm()
#     return render(request, 'signup.html', {'form': form})
#
#
# # نقطة النهاية لعرض البيانات الطبية
# def get(request):
#     data = {"message": "Health prediction data will be shown here."}
#     return Response(data, status=status.HTTP_200_OK)
#
# #
# # class HealthPredictionAPIView(APIView):
# #     pass
#
#
#

#
# from typing import Hashable
# from django.http import JsonResponse, HttpResponse
# from django.shortcuts import render, redirect
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth import login, authenticate, logout
# from .forms import CustomSignupForm, LoginForm
# from .models import HealthData, ImportedFile
# from .serializers import HealthDataSerializer
# from django.views.generic import ListView
# import json
# import pandas as pd
# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page
#
#
# # from rest_framework.decorators import api_view
#
#
# # معالج الاستثناءات المخصص
# def custom_exception_handler(exc, context):
#     response = exception_handler (exc, context)
#     if response is not None:
#         response.data['status_code'] = response.status_code
#     return response
#
#
# # تطبيق الـ cache على الـ API لمدة 15 دقيقة
# @method_decorator (cache_page (60 * 15), name='dispatch')  # 15 دقيقة تخزين مؤقت
# class HealthDataViewSet (APIView):
#     """
#     API View لعرض البيانات الطبية مثل الأعراض والأمراض.
#     يشمل الفلترة والتخزين المؤقت.
#     """
#
#     def get(self, request, *args, **kwargs):
#         health_data = HealthData.objects.all ()
#         serializer = HealthDataSerializer (health_data, many=True)
#         return Response (serializer.data)
#
#
# # تحميل البيانات من ملف CSV
# def import_data_from_csv(file_path):
#     df = pd.read_csv (file_path)
#     for index, row in df.iterrows ():
#         row_data = row.to_dict ()
#         diagnosis = row_data.pop ('diagnosis', '')
#         health_data = HealthData.objects.create (
#             data=json.dumps (row_data),
#             diagnosis=diagnosis
#         )
#         print (f"Data added for row {index + 1}: {row_data} with diagnosis: {diagnosis}")
#
#
# # نموذج لتحميل الملفات المستوردة
# def import_file(request):
#     if request.method == 'POST' and request.FILES['file']:
#         uploaded_file = request.FILES['file']
#         file_path = uploaded_file.name
#         # استيراد البيانات من CSV
#         import_data_from_csv (file_path)
#         return JsonResponse ({'status': 'File imported successfully'})
#     return render (request, 'import_file.html')
#
#
# # صفحة تسجيل الدخول
# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm (request.POST)
#         if form.is_valid ():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate (request, username=username, password=password)
#             if user is not None:
#                 login (request, user)
#                 return redirect ('home')
#             else:
#                 form.add_error (None, 'Invalid login credentials')
#     else:
#         form = LoginForm ()
#     return render (request, 'login.html', {'form': form})
#
#
# # صفحة التسجيل
# def signup_view(request):
#     if request.method == 'POST':
#         form = CustomSignupForm (request.POST)
#         if form.is_valid ():
#             form.save ()
#             username = form.cleaned_data.get ('username')
#             password = form.cleaned_data.get ('password1')
#             user = authenticate (username=username, password=password)
#             if user is not None:
#                 login (request, user)
#                 return redirect ('home')
#     else:
#         form = CustomSignupForm ()
#     return render (request, 'signup.html', {'form': form})
#
#
# # صفحة عرض البيانات الطبية عبر API
# class HealthDataAPIView (APIView):
#     """
#     API view لاسترجاع البيانات الطبية.
#     """
#
#     def get(self, request, *args, **kwargs):
#         health_data = HealthData.objects.all ()
#         serializer = HealthDataSerializer (health_data, many=True)
#         return Response (serializer.data)
#
#
# # صفحة للتنبؤ بالحالة الصحية بناءً على البيانات
# def post(request, *args, **kwargs):
#     # منطق التنبؤ بالحالة الصحية بناءً على البيانات المرسلة
#     data = request.data
#     # على سبيل المثال:
#     result = {"prediction": "Healthy"}  # يجب أن يتم تغيير هذا بناءً على بياناتك الفعلية
#     return JsonResponse (result)
#
#
# class HealthPredictionAPIView (APIView):
#     """
#     API view للتنبؤ بالحالة الصحية بناءً على البيانات المرسلة.
#     """
#
#
# # @api_view (['POST'])
# # def create_health_data(request):
# #     if request.method == 'POST':
# #         # تأكد من أن البيانات التي وصلت سليمة
# #         print (request.data)  # لعرض البيانات التي استقبلها السيرفر
# #
# #         # إنشاء الـserializer
# #         serializer = HealthDataSerializer (data=request.data)
# #
# #         # تحقق مما إذا كانت البيانات صالحة
# #         if serializer.is_valid ():
# #             serializer.save ()  # حفظ البيانات في قاعدة البيانات
# #             return Response (serializer.data, status=status.HTTP_201_CREATED)
# #         else:
# #             return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# # عرض الصفحة الرئيسية
# def home_view(request):
#     return HttpResponse ("Welcome to the Health Prediction API!")
#
#
# # عرض البيانات عبر HTML
# class HealthDataHTMLView (ListView):
#     model = HealthData
#     template_name = 'health/health_data_list.html'
#     context_object_name = 'health_data_list'

# ----------------------------------------------------------
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from django.http import JsonResponse, HttpResponse
# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page
# from django.views.generic import ListView
# from .models import HealthData
# from .serializers import HealthDataSerializer
# import pandas as pd
# import json
#
#
# # نقطة الوصول المشتركة لـ GET وPOST
# @method_decorator (cache_page (60 * 15), name='dispatch')  # تخزين مؤقت لمدة 15 دقيقة
# class HealthDataListCreateView (APIView):
#     """
#     API View لاسترجاع وإنشاء البيانات الطبية مثل الأعراض والأمراض.
#     """
#
#     def get(self, request):
#         health_data = HealthData.objects.all ()
#         serializer = HealthDataSerializer (health_data, many=True)
#         return Response (serializer.data)
#
#     def post(self, request):
#         serializer = HealthDataSerializer (data=request.data)
#         if serializer.is_valid ():
#             serializer.save ()
#             return Response (serializer.data, status=status.HTTP_201_CREATED)
#         return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# # استيراد البيانات من ملف CSV
# def import_data_from_csv(file_path):
#     df = pd.read_csv (file_path)
#     for index, row in df.iterrows ():
#         row_data = row.to_dict ()
#         diagnosis = row_data.pop ('diagnosis', '')
#         health_data = HealthData.objects.create (**row_data, diagnosis=diagnosis)
#         print (f"Data added for row {index + 1}: {row_data} with diagnosis: {diagnosis}")
#
#
# def import_file(request):
#     if request.method == 'POST' and request.FILES['file']:
#         uploaded_file = request.FILES['file']
#         file_path = uploaded_file.name
#         import_data_from_csv (file_path)
#         return JsonResponse ({'status': 'File imported successfully'})
#     return render (request, 'import_file.html')
#
#
# # واجهة API للتنبؤ بالحالة الصحية
# class HealthPredictionAPIView (APIView):
#     def post(self, request):
#         data = request.data
#         # هنا يمكنك إضافة منطق التنبؤ بناءً على البيانات الفعلية
#         result = {"prediction": "Healthy"}  # مثال بسيط للتنبؤ
#         return JsonResponse (result)
#
#
# # عرض الصفحة الرئيسية
# def home_view(request):
#     return HttpResponse ("Welcome to the Health Prediction API!")
#
#
# # عرض البيانات الطبية في قالب HTML
# class HealthDataHTMLView (ListView):
#     model = HealthData
#     template_name = 'health/health_data_list.html'
#     context_object_name = 'health_data_list'
# -----------------------------------------------------------
# شغااااال
# from django.shortcuts import render
# from .models import HealthData
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from django.http import JsonResponse, HttpResponse
# from django.contrib.auth import login, authenticate
# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page
# from django.views.generic import ListView
# from .serializers import HealthDataSerializer
# import pandas as pd
# import json
#
#
# # عرض البيانات الطبية في قالب HTML
# def health_data_list(request):
#     data = HealthData.objects.all ()  # جلب البيانات من قاعدة البيانات
#     return render (request, 'health_data_list.html', {'data': data})
#
#
# # نقطة الوصول المشتركة لـ GET وPOST
# @method_decorator (cache_page (60 * 15), name='dispatch')  # تخزين مؤقت لمدة 15 دقيقة
# class HealthDataListCreateView (APIView):
#     """
#     API View لاسترجاع وإنشاء البيانات الطبية مثل الأعراض والأمراض.
#     """
#
#     def get(self, request):
#         health_data = HealthData.objects.all ()
#         serializer = HealthDataSerializer (health_data, many=True)
#         return Response (serializer.data)
#
#     def post(self, request):
#         serializer = HealthDataSerializer (data=request.data)
#         if serializer.is_valid ():
#             serializer.save ()
#             return Response (serializer.data, status=status.HTTP_201_CREATED)
#         return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# # استيراد البيانات من ملف CSV
# def import_data_from_csv(file_path):
#     df = pd.read_csv (file_path)
#     for index, row in df.iterrows ():
#         row_data = row.to_dict ()
#         diagnosis = row_data.pop ('diagnosis', '')
#         health_data = HealthData.objects.create (**row_data, diagnosis=diagnosis)
#         print (f"Data added for row {index + 1}: {row_data} with diagnosis: {diagnosis}")
#
#
# def import_file(request):
#     if request.method == 'POST' and request.FILES['file']:
#         uploaded_file = request.FILES['file']
#         file_path = uploaded_file.name
#         import_data_from_csv (file_path)
#         return JsonResponse ({'status': 'File imported successfully'})
#     return render (request, 'import_file.html')
#
#
# # واجهة API للتنبؤ بالحالة الصحية
# class HealthPredictionAPIView (APIView):
#     def post(self, request):
#         data = request.data
#         # هنا يمكنك إضافة منطق التنبؤ بناءً على البيانات الفعلية
#         result = {"prediction": "Healthy"}  # مثال بسيط للتنبؤ
#         return JsonResponse (result)
#
#
# # عرض الصفحة الرئيسية
# def home_view(request):
#     return HttpResponse ("Welcome to the Health Prediction API!")
#
#
# # عرض البيانات الطبية في قالب HTML باستخدام ListView
# class HealthDataHTMLView (ListView):
#     model = HealthData
#     template_name = 'health/health_data_list.html'
#     context_object_name = 'health_data_list'
# --------------------------------333


# from rest_framework import generics, status, permissions
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework.authtoken.models import Token
# from django.http import JsonResponse
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate
# from .models import HealthData
# from .serializers import HealthDataSerializer  # تأكد من أنك أنشأت الـ serializer الخاص بـ HealthData
#
#
# # تسجيل مستخدم جديد باستخدام APIView
# class RegisterView(APIView):
#     permission_classes = [permissions.AllowAny]
#
#     def post(self, request):
#         username = request.data.get("username")
#         password = request.data.get("password")
#         email = request.data.get("email")
#
#         # التأكد من وجود البيانات المطلوبة
#         if not username or not password or not email:
#             return Response({"error": "Username, password and email are required."}, status=400)
#
#         # إنشاء المستخدم الجديد
#         try:
#             user = User.objects.create_user(username=username, password=password, email=email)
#             user.save()
#             return Response({"message": "User created successfully!"}, status=201)
#         except Exception as e:
#             return Response({"error": str(e)}, status=500)
#
#
# # تسجيل الدخول للمستخدم باستخدام APIView
# class LoginView(APIView):
#     permission_classes = [permissions.AllowAny]
#
#     def post(self, request):
#         username = request.data.get("username")
#         password = request.data.get("password")
#
#         # التحقق من صحة بيانات المستخدم
#         user = authenticate(username=username, password=password)
#
#         if user:
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({"token": token.key}, status=200)
#         else:
#             return Response({"error": "Invalid credentials."}, status=400)
#
#
# # دالة التسجيل باستخدام @api_view (اختياري: إذا أردت إبقاءها في شكل دالة وليس Class)
# @api_view(['POST'])
# def register(request):
#     try:
#         username = request.data['username']
#         password = request.data['password']
#         email = request.data['email']
#
#         user = User.objects.create_user(username=username, password=password, email=email)
#         user.save()
#
#         return JsonResponse({"message": "User created successfully!"}, status=201)
#     except KeyError:
#         return JsonResponse({"error": "Missing required fields"}, status=400)
#
#
# # عرض البيانات وإنشاء بيانات جديدة باستخدام HealthDataListCreateView
# class HealthDataListCreateView(generics.ListCreateAPIView):
#     queryset = HealthData.objects.all()
#     serializer_class = HealthDataSerializer
#
#
# # التنبؤ بالحالة الصحية بناءً على البيانات المرسلة باستخدام HealthPredictionAPIView
# class HealthPredictionAPIView(APIView):
#     def post(self, request):
#         # منطق التنبؤ الصحي
#         return Response({"message": "Health prediction logic goes here"}, status=200)


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status, permissions
# from django.contrib.auth import authenticate
# from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User
# from rest_framework import generics
# from .models import HealthData
# from .serializers import HealthDataSerializer
#
# # تسجيل مستخدم جديد باستخدام APIView
# class RegisterView(APIView):
#     permission_classes = [permissions.AllowAny]
#
#     def post(self, request):
#         # استخراج البيانات من الطلب
#         username = request.data.get("username")
#         password = request.data.get("password")
#         email = request.data.get("email")
#         fname = request.data.get("Fname")  # الاسم الأول
#         lname = request.data.get("Lname")  # الاسم الأخير
#
#         # التأكد من أن جميع الحقول المطلوبة موجودة
#         if not username or not password or not email or not fname or not lname:
#             return Response({"error": "Username, password, email, Fname, and Lname are required."},
#                              status=status.HTTP_400_BAD_REQUEST)
#
#         try:
#             # إنشاء المستخدم الجديد
#             user = User.objects.create_user(username=username, password=password, email=email)
#             # إضافة الاسم الأول والاسم الأخير
#             user.first_name = fname
#             user.last_name = lname
#             user.save()
#
#             return Response({"message": "User created successfully!"}, status=status.HTTP_201_CREATED)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#
# # تسجيل الدخول للمستخدم باستخدام APIView
# class LoginView(APIView):
#     permission_classes = [permissions.AllowAny]
#
#     def post(self, request):
#         username = request.data.get("username")
#         password = request.data.get("password")
#
#         # التحقق من بيانات المستخدم
#         user = authenticate(username=username, password=password)
#
#         if user:
#             # إنشاء أو جلب الـ Token الخاص بالمستخدم
#
#             # token, created = Token.objects.get_or_create(user=user)
#             # return Response({"token": token.key}, status=status.HTTP_200_OK)
#
#             # التحقق من الحقول الإضافية (إذا كنت بحاجة لذلك)
#             fname = user.first_name
#             lname = user.last_name
#             return Response ({
#                 "token": Token.objects.get_or_create (user=user)[0].key,
#                 "Fname": fname,
#                 "Lname": lname
#             }, status=status.HTTP_200_OK)
#
#         else:
#             return Response({"error": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST)
#
#
# # عرض البيانات وإنشاء بيانات جديدة باستخدام HealthDataListCreateView
# class HealthDataListCreateView(generics.ListCreateAPIView):
#     queryset = HealthData.objects.all()
#     serializer_class = HealthDataSerializer
#
#
# # التنبؤ بالحالة الصحية باستخدام HealthPredictionAPIView
# class HealthPredictionAPIView(APIView):
#     permission_classes = [permissions.AllowAny]
#
#     def post(self, request):
#         # منطق التنبؤ الصحي هنا
#         return Response({"message": "Health prediction logic goes here"}, status=status.HTTP_200_OK)


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status, permissions
# from django.contrib.auth import authenticate
# from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User
# from rest_framework import generics
# from django.db.models import Q  # للاستعلام باستخدام شروط متعددة
# from .models import HealthData
# from .serializers import HealthDataSerializer
#
#
# # تسجيل مستخدم جديد باستخدام APIView
# class RegisterView (APIView):
#     permission_classes = [permissions.AllowAny]
#
#     def post(self, request):
#         # استخراج البيانات من الطلب
#         username = request.data.get ("username")
#         password = request.data.get ("password")
#         email = request.data.get ("email")
#         fname = request.data.get ("Fname")  # الاسم الأول
#         lname = request.data.get ("Lname")  # الاسم الأخير
#
#         # التأكد من أن جميع الحقول المطلوبة موجودة
#         if not username or not password or not email or not fname or not lname:
#             return Response ({"error": "Username, password, email, Fname, and Lname are required."},
#                              status=status.HTTP_400_BAD_REQUEST)
#
#         try:
#             # إنشاء المستخدم الجديد
#             user = User.objects.create_user (username=username, password=password, email=email)
#             # إضافة الاسم الأول والاسم الأخير
#             user.first_name = fname
#             user.last_name = lname
#             user.save ()
#
#             return Response ({"message": "User created successfully!"}, status=status.HTTP_201_CREATED)
#         except Exception as e:
#             return Response ({"error": str (e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#
# # تسجيل الدخول للمستخدم باستخدام APIView (تسجيل الدخول عبر اسم المستخدم أو البريد الإلكتروني)
# class LoginView (APIView):
#     permission_classes = [permissions.AllowAny]
#
#     def post(self, request):
#         login_input = request.data.get ("login")  # يمكن أن يكون username أو email
#         password = request.data.get ("password")
#
#         if not login_input or not password:
#             return Response ({"error": "Login and password are required."},
#                              status=status.HTTP_400_BAD_REQUEST)
#
#         # جلب المستخدم باستخدام username أو email
#         try:
#             user = User.objects.filter (Q (username=login_input) | Q (email=login_input)).first ()
#
#             if user:
#                 # التحقق من كلمة المرور
#                 user = authenticate (username=user.username, password=password)
#                 if user:
#                     token, created = Token.objects.get_or_create (user=user)
#                     # إضافة معلومات المستخدم إلى الاستجابة
#                     return Response ({
#                         "token": token.key,
#                         "Fname": user.first_name,
#                         "Lname": user.last_name
#                     }, status=status.HTTP_200_OK)
#                 else:
#                     return Response ({"error": "Invalid password."}, status=status.HTTP_400_BAD_REQUEST)
#             else:
#                 return Response ({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
#
#         except Exception as e:
#             return Response ({"error": str (e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#
# # عرض البيانات وإنشاء بيانات جديدة باستخدام HealthDataListCreateView
# class HealthDataListCreateView (generics.ListCreateAPIView):
#     queryset = HealthData.objects.all ()
#     serializer_class = HealthDataSerializer
#
#
# # التنبؤ بالحالة الصحية باستخدام HealthPredictionAPIView
# class HealthPredictionAPIView (APIView):
#     permission_classes = [permissions.AllowAny]
#
#     def post(self, request):
#         # منطق التنبؤ الصحي هنا
#         return Response ({"message": "Health prediction logic goes here"}, status=status.HTTP_200_OK)


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status, permissions
# from django.contrib.auth import authenticate
# from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User
# from rest_framework import generics
# from django.db.models import Q
# from .models import HealthData
# from .serializers import HealthDataSerializer
# import pickle
#
#
# # تسجيل مستخدم جديد
# class RegisterView(APIView):
#     permission_classes = [permissions.AllowAny]
#
#     def post(self, request):
#         username = request.data.get("username")
#         password = request.data.get("password")
#         email = request.data.get("email")
#         fname = request.data.get("Fname")
#         lname = request.data.get("Lname")
#
#         # التحقق من الحقول المطلوبة
#         if not username or not password or not email or not fname or not lname:
#             return Response({
#                 "status": "error",
#                 "message": "All fields are required."
#             }, status=status.HTTP_400_BAD_REQUEST)
#
#         try:
#             if User.objects.filter(Q(username=username) | Q(email=email)).exists():
#                 return Response({
#                     "status": "error",
#                     "message": "Username or email already exists."
#                 }, status=status.HTTP_400_BAD_REQUEST)
#
#             user = User.objects.create_user(username=username, password=password, email=email)
#             user.first_name = fname
#             user.last_name = lname
#             user.save()
#
#             return Response({
#                 "status": "success",
#                 "message": "User registered successfully."
#             }, status=status.HTTP_201_CREATED)
#         except Exception as e:
#             return Response({
#                 "status": "error",
#                 "message": str(e)
#             }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#
# # تسجيل الدخول
# class LoginView(APIView):
#     permission_classes = [permissions.AllowAny]
#
#     def post(self, request):
#         login_input = request.data.get("login")
#         password = request.data.get("password")
#
#         if not login_input or not password:
#             return Response({
#                 "status": "error",
#                 "message": "Login and password are required."
#             }, status=status.HTTP_400_BAD_REQUEST)
#
#         try:
#             user = User.objects.filter(Q(username=login_input) | Q(email=login_input)).first()
#             if user:
#                 user = authenticate(username=user.username, password=password)
#                 if user:
#                     token, created = Token.objects.get_or_create(user=user)
#                     response = Response({
#                         "status": "success",
#                         "message": "Login successful",
#                         "data": {
#                             "Fname": user.first_name,
#                             "Lname": user.last_name
#                         }
#                     }, status=status.HTTP_200_OK)
#                     response.set_cookie(
#                         key='auth_token',
#                         value=token.key,
#                         httponly=True,
#                         secure=True,
#                         samesite='Lax'
#                     )
#                     return response
#                 else:
#                     return Response({
#                         "status": "error",
#                         "message": "Invalid password."
#                     }, status=status.HTTP_400_BAD_REQUEST)
#             else:
#                 return Response({
#                     "status": "error",
#                     "message": "User not found."
#                 }, status=status.HTTP_404_NOT_FOUND)
#         except Exception as e:
#             return Response({
#                 "status": "error",
#                 "message": str(e)
#             }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#
# # عرض وإنشاء بيانات صحية
# class HealthDataListCreateView(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = HealthData.objects.all()
#     serializer_class = HealthDataSerializer
#
#
# # التنبؤ بالحالة الصحية
# class HealthPredictionAPIView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#
#     def post(self, request):
#         model_path = "path/to/your/model.pkl"
#         try:
#             with open(model_path, "rb") as model_file:
#                 model = pickle.load(model_file)
#
#             input_data = request.data.get("features")
#             if not input_data:
#                 return Response({
#                     "status": "error",
#                     "message": "Features are required for prediction."
#                 }, status=status.HTTP_400_BAD_REQUEST)
#
#             # تحقق من أن البيانات المدخلة بصيغة صحيحة
#             if not isinstance(input_data, list) or len(input_data) == 0:
#                 return Response({
#                     "status": "error",
#                     "message": "Invalid input format for features."
#                 }, status=status.HTTP_400_BAD_REQUEST)
#
#             prediction = model.predict([input_data])
#
#             return Response({
#                 "status": "success",
#                 "prediction": prediction[0]
#             }, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({
#                 "status": "error",
#                 "message": str(e)
#             }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from .models import HealthData
from .serializers import HealthDataSerializer
from rest_framework import generics


# دالة لتسجيل الدخول عبر HTML Template
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate (request, username=username, password=password)

        if user is not None:
            login (request, user)
            return redirect ('home')  # إعادة توجيه المستخدم إلى الصفحة الرئيسية بعد تسجيل الدخول
        else:
            return render (request, 'home.html', {'error': 'بيانات الدخول غير صحيحة'})

    return render (request, 'home.html')  # إذا كانت الطلبات من نوع GET، سيتم عرض صفحة تسجيل الدخول


# دالة لعرض الصفحة الرئيسية
def home_view(request):
    return render (request, 'home.html')


# دالة لتسجيل الدخول عبر API
class LoginView (APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get ('username')
        password = request.data.get ('password')

        if not username or not password:
            return Response ({
                "status": "error",
                "message": "Both username and password are required."
            }, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate (request, username=username, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create (user=user)
            return Response ({
                "status": "success",
                "message": "Login successful",
                "token": token.key
            }, status=status.HTTP_200_OK)
        else:
            return Response ({
                "status": "error",
                "message": "Invalid credentials."
            }, status=status.HTTP_400_BAD_REQUEST)


# تسجيل مستخدم جديد
class RegisterView (APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get ("username")
        password = request.data.get ("password")
        email = request.data.get ("email")
        fname = request.data.get ("Fname")
        lname = request.data.get ("Lname")

        # التحقق من الحقول المطلوبة
        if not username or not password or not email or not fname or not lname:
            return Response ({
                "status": "error",
                "message": "All fields are required."
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            if User.objects.filter (username=username).exists () or User.objects.filter (email=email).exists ():
                return Response ({
                    "status": "error",
                    "message": "Username or email already exists."
                }, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.create_user (username=username, password=password, email=email)
            user.first_name = fname
            user.last_name = lname
            user.save ()

            return Response ({
                "status": "success",
                "message": "User registered successfully."
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response ({
                "status": "error",
                "message": str (e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# API لعرض بيانات الصحة
class HealthDataListCreateView (generics.ListCreateAPIView):
    queryset = HealthData.objects.all ()
    serializer_class = HealthDataSerializer


# API للتنبؤ بالحالة الصحية
class HealthPredictionAPIView (APIView):
    def post(self, request, *args, **kwargs):
        # استلام البيانات من الطلب
        data = request.data
        # منطق التنبؤ بالحالة الصحية (تحديثه حسب المشروع)
        prediction_result = {"message": "Prediction logic not implemented yet"}
        return Response (prediction_result, status=status.HTTP_200_OK)
