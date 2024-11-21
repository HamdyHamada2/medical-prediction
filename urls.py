# from django.urls import path, include
# from django.contrib import admin
# from django.shortcuts import redirect
# from rest_framework.schemas import get_schema_view
# from rest_framework.permissions import AllowAny
#
# urlpatterns = [
#     # مسار لوحة التحكم
#     path('admin/', admin.site.urls),
#
#     # مسار تطبيق health
#     path('health-data/', include('health.urls')),  # تضمين مسارات تطبيق health
#
#     # مسار مخطط OpenAPI
#     path('schema/', get_schema_view(
#         permission_classes=[AllowAny],
#     ), name='openapi-schema'),
#
#     # إعادة توجيه الصفحة الرئيسية إلى health-data
#     path('', lambda request: redirect('health_data_list')),  # إعادة توجيه الصفحة الرئيسية إلى health_data_list
#     # path ('', lambda request: redirect (reverse ('health_data_list'))),  # إعادة التوجيه إلى health_data_list
#
# ]
# -------------------------------------------------------------------
#
# from django.urls import path, include
# from django.contrib import admin
# from django.shortcuts import redirect
#
# urlpatterns = [
#     # مسار لوحة التحكم
#     path('admin/', admin.site.urls),
#
#     path ('health/', include ('health.urls')),  # تأكد أن 'health' هو اسم تطبيقك
#
#     # مسار تطبيق health مع تعريف namespace
#     path('health/', include(('health.urls', 'health'), namespace='health')),
#
#     # إعادة توجيه الصفحة الرئيسية إلى health_data_list_create
#     path('', lambda request: redirect('health:health_data_list_create')),
#
# ]

# from django.contrib import admin
# from django.urls import path, include
# from django.shortcuts import redirect
# from django.conf import settings
# from django.conf.urls.static import static
#
# urlpatterns = [
#                   # مسار لوحة التحكم
#                   path ('admin/', admin.site.urls),
#
#                   # مسار تطبيق health
#                   path ('health/', include (('health.urls', 'health'), namespace='health')),
#                   path ('health/', include ('health.urls')),  # التأكد من تضمين تطبيق health
#
#                   # إعادة توجيه الصفحة الرئيسية إلى health_data_list_create
#                   path ('', lambda request: redirect ('health:health_data_list_create')),
#               ] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from health import views

urlpatterns = [
    # مسار لوحة التحكم
    path("admin/", admin.site.urls),
    # مسار تطبيق health
    path("health/", include(("health.urls", "health"), namespace="health")),
    path("health/", include("health.urls")),  # التأكد من تضمين تطبيق health
    # إعادة توجيه الصفحة الرئيسية إلى health_data_list_create
    path("", lambda request: redirect("health:health_data_list_create")),
    # مسار رفع الملفات
    path("upload/", views.upload_files_view, name="upload_file"),
]

# إذا كان التطبيق في وضع التطوير (DEBUG=True)، يمكنك تقديم الملفات الوسائطية
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# from django.urls import path, include
# from django.contrib import admin
# from django.shortcuts import redirect
#
# urlpatterns = [
#     # مسار لوحة التحكم
#     path('admin/', admin.site.urls),
#
#     # مسار تطبيق health مع تعريف namespace
#     path('health/', include(('health.urls', 'health'), namespace='health')),
#
#     # إعادة توجيه الصفحة الرئيسية إلى health_data_list_create
#     path('', lambda request: redirect('health:health_data_list_create')),
# ]
