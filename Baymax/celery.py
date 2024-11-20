# baymax/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# تحديد إعدادات Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Baymax.settings')

app = Celery('Baymax')

# تحميل إعدادات Celery من ملف settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
# اكتشاف المهام بشكل تلقائي
app.autodiscover_tasks()
