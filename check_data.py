import os
import django
import json

# تعيين ملف إعدادات Django
os.environ.setdefault ('DJANGO_SETTINGS_MODULE', 'Baymax.settings')
django.setup ()

from health.models import HealthData, ImportedFile


def check_uploaded_data():
    invalid_data = []

    # جلب جميع السجلات من HealthData
    all_data = HealthData.objects.all ()

    for record in all_data:
        try:
            # التحقق من صحة JSON
            json_data = json.loads (json.dumps (record.data))
        except json.JSONDecodeError:
            invalid_data.append (record.id)
            print (f"السجل {record.id} يحتوي على بيانات غير صالحة")

    if invalid_data:
        print (f"عدد السجلات غير الصالحة: {len (invalid_data)}")
    else:
        print ("كل السجلات صالحة ولا يوجد أخطاء.")


def list_imported_files():
    imported_files = ImportedFile.objects.all ()
    if imported_files.exists ():
        print ("الملفات التي تم استيرادها مسبقاً:")
        for file_record in imported_files:
            print (f"- {file_record.filename}")
    else:
        print ("لا يوجد ملفات تم استيرادها.")


if __name__ == "__main__":
    print ("التحقق من صحة البيانات:")
    check_uploaded_data ()
    print ("\nعرض الملفات المستوردة:")
    list_imported_files ()
