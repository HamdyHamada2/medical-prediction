from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# تحديد إعدادات Django
os.environ.setdefault ('DJANGO_SETTINGS_MODULE', 'Baymax.settings')


# تأجيل استيراد Celery داخل الدالة لتجنب الاستيراد الدائري
def create_celery_app():
    app = Celery ('Baymax')

    # تحميل إعدادات Celery من ملف settings.py
    app.config_from_object ('django.conf:settings', namespace='CELERY')

    # إعدادات الاتصال بـ Redis
    app.conf.update (
        CELERY_BROKER_URL='redis://localhost:6379/0',
        CELERY_ACCEPT_CONTENT=['json'],
        CELERY_TASK_SERIALIZER='json',
        CELERY_TIMEZONE='UTC'
    )

    # اكتشاف المهام بشكل تلقائي
    app.autodiscover_tasks ()

    return app


# إنشاء التطبيق
app = create_celery_app ()

# يمكنك إضافة هذه السطر لتشغيل تطبيق Celery قاصدًا إذا كان هذا هو المِلَفّ الرئيس
# (ولكن عادةً ما يتم استخدام مِلَفّ __init__.py في Django بشكل أكبر)
