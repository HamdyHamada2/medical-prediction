<<<<<<< HEAD
import os
import django
import pandas as pd
import json

# إعداد Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Baymax.settings')
django.setup()

from health.models import HealthData, ImportedFile

# المسار الرئيسي للملفات
directory_path = r'C:\Users\Flash-Tech\.cache\kagglehub\datasets'

def import_data_from_csv(file_path):
    # قراءة البيانات من ملف CSV إلى DataFrame
    df = pd.read_csv(file_path)

    # تمر عبر كل صف في الملف
    for index, row in df.iterrows():
        # تحويل السطر إلى قاموس (dictionary)
        row_data = row.to_dict()

        # تحويل البيانات إلى JSON صالح
        row_data_json = json.dumps(row_data)  # تحويل البيانات إلى JSON

        # استخراج التشخيص إذا كان موجودًا
        diagnosis = row_data.pop('diagnosis', '')  # إزالة التشخيص من البيانات إذا كان موجودًا

        # إضافة البيانات إلى HealthData
        health_data = HealthData.objects.create(
            data=row_data_json,  # تخزين البيانات بتنسيق JSON صالح
            diagnosis=diagnosis
        )

        # طباعة رسالة لتأكيد إضافة البيانات
        print(f"Data added for row {index + 1}: {row_data} with diagnosis: {diagnosis}")

def import_all_csv_files():
    # المرور عبر جميع الملفات داخل المسار
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # التأكد من أن الملف بصيغة CSV
        if filename.endswith('.csv'):
            print(f'Importing data from {filename}...')
            import_data_from_csv(file_path)

    print("Data imported successfully from all CSV files!")

# دالة للتحقق من صحة البيانات
def validate_health_data():
    invalid_entries = []

    # البحث عن السجلات التي تحتوي على بيانات مفقودة أو غير صحيحة
    for entry in HealthData.objects.all():
        # تحقق من صحة الحقل 'diagnosis'
        if not entry.diagnosis:
            invalid_entries.append((entry.id, 'Missing diagnosis'))

        # تحقق من صحة الحقل 'data' كـ JSON صالح
        try:
            json_data = entry.data
            json.dumps(json_data)  # محاولة تحويل البيانات إلى JSON للتحقق من صحتها
        except (TypeError, json.JSONDecodeError):
            invalid_entries.append((entry.id, 'Invalid JSON in data'))

    # إذا تم العثور على سجلات غير صالحة، اعرضها
    if invalid_entries:
        print("Found invalid entries:")
        for entry in invalid_entries:
            print(f"Entry ID: {entry[0]}, Issue: {entry[1]}")
    else:
        print("All data entries are valid.")

# دالة لعرض أسماء الملفات المستوردة
def list_imported_files():
    files = ImportedFile.objects.all()
    if files:
        print("Imported files:")
        for file in files:
            print(f"- {file.filename}")
    else:
        print("No files have been imported yet.")

if __name__ == "__main__":
    # استيراد البيانات من ملفات CSV
    import_all_csv_files()

    # التحقق من البيانات في قاعدة البيانات
    validate_health_data()

    # عرض أسماء الملفات المستوردة
    list_imported_files()
=======
import os
import django
import pandas as pd
import json

# إعداد Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Baymax.settings')
django.setup()

from health.models import HealthData

# المسار الرئيسي للملفات
directory_path = r'C:\Users\Flash-Tech\.cache\kagglehub\datasets'

def import_data_from_csv(file_path):
    # قراءة البيانات من ملف CSV إلى DataFrame
    df = pd.read_csv(file_path)

    # تمر عبر كل صف في الملف
    for index, row in df.iterrows():
        # تحويل السطر إلى قاموس (dictionary)
        row_data = row.to_dict()

        # تحويل البيانات إلى JSON صالح
        row_data_json = json.dumps(row_data)  # تحويل البيانات إلى JSON

        # استخراج التشخيص إذا كان موجودًا
        diagnosis = row_data.pop('diagnosis', '')  # إزالة التشخيص من البيانات إذا كان موجودًا

        # إضافة البيانات إلى HealthData
        health_data = HealthData.objects.create(
            data=row_data_json,  # تخزين البيانات بتنسيق JSON صالح
            diagnosis=diagnosis
        )

        # طباعة رسالة لتأكيد إضافة البيانات
        print(f"Data added for row {index + 1}: {row_data} with diagnosis: {diagnosis}")

def import_all_csv_files():
    # المرور عبر جميع الملفات داخل المسار
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # التأكد من أن الملف بصيغة CSV
        if filename.endswith('.csv'):
            print(f'Importing data from {filename}...')
            import_data_from_csv(file_path)

    print("Data imported successfully from all CSV files!")

if __name__ == "__main__":
    import_all_csv_files()


# import django
# import json
# from health.models import HealthData, ImportedFile
# import os
#
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Baymax.settings')
# django.setup ()
#
#
# # دالة للتحقق من صحة البيانات
# def validate_health_data():
#     invalid_entries = []
#
#     # البحث عن السجلات التي تحتوي على بيانات مفقودة أو غير صحيحة
#     for entry in HealthData.objects.all ():
#         # تحقق من صحة الحقل 'diagnosis'
#         if not entry.diagnosis:
#             invalid_entries.append ((entry.id, 'Missing diagnosis'))
#
#         # تحقق من صحة الحقل 'data' كـ JSON صالح
#         try:
#             json_data = entry.data
#             json.dumps (json_data)  # محاولة تحويل البيانات إلى JSON للتحقق من صحتها
#         except (TypeError, json.JSONDecodeError):
#             invalid_entries.append ((entry.id, 'Invalid JSON in data'))
#
#     # إذا تم العثور على سجلات غير صالحة، اعرضها
#     if invalid_entries:
#         print ("Found invalid entries:")
#         for entry in invalid_entries:
#             print (f"Entry ID: {entry[0]}, Issue: {entry[1]}")
#     else:
#         print ("All data entries are valid.")
#
#
# # دالة لعرض أسماء الملفات المستوردة
# def list_imported_files():
#     files = ImportedFile.objects.all ()
#     if files:
#         print ("Imported files:")
#         for file in files:
#             print (f"- {file.filename}")
#     else:
#         print ("No files have been imported yet.")
#
#
# if __name__ == "__main__":
#     # التحقق من البيانات في قاعدة البيانات
#     validate_health_data ()
#
#     # عرض أسماء الملفات المستوردة
#     list_imported_files ()
>>>>>>> 2b2537fbf868847a9df0c4b2c78dedbea0eff6da
