from __future__ import absolute_import, unicode_literals

# التأكد من تحميل celery عند تشغيل أي شيء من هذا المجلد
from .celery import app as celery_app

__all__ = ('celery_app',)
