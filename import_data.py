# هنا كود قراءه الاعمده من الملفات
# import csv
# import pandas as pd
# import os
#
#
# def read_file(file_path):
#     # الحصول على الامتداد من اسم الملف
#     file_extension = os.path.splitext (file_path)[1].lower ()
#
#     if file_extension == '.csv':
#         # قراءة ملف CSV باستخدام csv.DictReader
#         with open (file_path, newline='', encoding='utf-8') as csvfile:
#             reader = csv.DictReader (csvfile)
#             for row in reader:
#                 print (row)  # طباعة البيانات من كل صف
#     elif file_extension in ['.xls', '.xlsx']:
#         # قراءة ملف Excel باستخدام pandas
#         df = pd.read_excel (file_path)
#         for index, row in df.iterrows ():
#             print (row.to_dict ())  # طباعة البيانات من كل صف كقاموس
#     else:
#         print (f"Unsupported file type: {file_extension}")
#
#
# if __name__ == "__main__":
#     # أدخل هنا مسار الملف الخاص بك
#     file_path = r'C:\Baymax\UPFile\ckd-dataset-v2.csv'  # استبدل بالمسار الفعلي للملف
#     read_file (file_path)

# ==========================================================================================
# كود رفع الداتا

# import os
# import sys
# import django
# import csv
# import pandas as pd
#
# # إضافة المجلد الجذر إلى المسار
# sys.path.append (os.path.abspath (os.path.join (os.path.dirname (__file__), '..')))
#
# # تعيين إعدادات Django
# os.environ.setdefault ('DJANGO_SETTINGS_MODULE', 'Baymax.settings')
#
# # استدعاء إعدادات Django
# django.setup ()
#
# # استيراد النموذج
# from health.models import HealthData
#
#
# def read_file(file_path):
#     file_extension = os.path.splitext (file_path)[1].lower ()
#
#     if file_extension == '.csv':
#         # قراءة ملف CSV باستخدام csv.DictReader
#         with open (file_path, newline='', encoding='utf-8') as csvfile:
#             reader = csv.DictReader (csvfile)
#             health_data_objects = []
#             for row in reader:
#                 # تحويل البيانات إلى كائن من النموذج HealthData
#                 health_data = HealthData (
#                     glucose=row['Glucose'],
#                     cholesterol=row['Cholesterol'],
#                     hemoglobin=row['Hemoglobin'],
#                     bp_diastolic=row['bp (Diastolic)'],
#                     bp_limit=row['bp limit'],
#                     sg=row['sg'],
#                     al=row['al'],
#                     class_value=row['class'],
#                     rbc=row['rbc'],
#                     su=row['su'],
#                     pc=row['pc'],
#                     pcc=row['pcc'],
#                     ba=row['ba'],
#                     bgr=row['bgr'],
#                     bu=row['bu'],
#                     sod=row['sod'],
#                     sc=row['sc'],
#                     pot=row['pot'],
#                     hemo=row['hemo'],
#                     pcv=row['pcv'],
#                     rbcc=row['rbcc'],
#                     wbcc=row['wbcc'],
#                     htn=row['htn'],
#                     dm=row['dm'],
#                     cad=row['cad'],
#                     appet=row['appet'],
#                     pe=row['pe'],
#                     ane=row['ane'],
#                     grf=row['grf'],
#                     stage=row['stage'],
#                     affected=row['affected'],
#                     age=row['age']
#                 )
#                 health_data_objects.append (health_data)
#
#             # إدخال البيانات دفعة واحدة باستخدام bulk_create
#             HealthData.objects.bulk_create (health_data_objects)
#             print (f"تم إضافة {len (health_data_objects)} سجلات إلى قاعدة البيانات.")
#
#     else:
#         print (f"نوع الملف غير مدعوم: {file_extension}")
#
#
# def import_data_from_csv(file_path):
#     # تحميل البيانات من ملف CSV باستخدام pandas
#     data = pd.read_csv (file_path)
#
#     health_data_objects = []
#     for index, row in data.iterrows ():
#         # تحويل البيانات إلى كائن من النموذج HealthData
#         health_data = HealthData (
#             glucose=row['Glucose'],
#             cholesterol=row['Cholesterol'],
#             hemoglobin=row['Hemoglobin'],
#             bp_diastolic=row['bp (Diastolic)'],
#             bp_limit=row['bp limit'],
#             sg=row['sg'],
#             al=row['al'],
#             class_value=row['class'],
#             rbc=row['rbc'],
#             su=row['su'],
#             pc=row['pc'],
#             pcc=row['pcc'],
#             ba=row['ba'],
#             bgr=row['bgr'],
#             bu=row['bu'],
#             sod=row['sod'],
#             sc=row['sc'],
#             pot=row['pot'],
#             hemo=row['hemo'],
#             pcv=row['pcv'],
#             rbcc=row['rbcc'],
#             wbcc=row['wbcc'],
#             htn=row['htn'],
#             dm=row['dm'],
#             cad=row['cad'],
#             appet=row['appet'],
#             pe=row['pe'],
#             ane=row['ane'],
#             grf=row['grf'],
#             stage=row['stage'],
#             affected=row['affected'],
#             age=row['age']
#         )
#         health_data_objects.append (health_data)
#
#     # إدخال البيانات دفعة واحدة باستخدام bulk_create
#     HealthData.objects.bulk_create (health_data_objects)
#     print (f"تم إضافة {len (health_data_objects)} سجلات إلى قاعدة البيانات.")
#
#
# if __name__ == "__main__":
#     # مسار ملف CSV
#     file_path = 'C:\\Baymax\\UPFile\\ckd-dataset-v2.csv'  # تأكد من المسار الصحيح للملف
#     read_file (file_path)  # استخدام الدالة الخاصة بالـ CSV
#     import_data_from_csv (file_path)  # إذا كنت تريد استخدام pandas لإدخال البيانات

import sys
import pandas as pd
import django
import os

# إضافة المسار للمشروع
sys.path.append(r'C:\Baymax')

# التأكد من إعداد Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Baymax.settings")  # قم بتغيير 'Baymax.settings' إلى اسم ملف الإعدادات إذا كان مختلفًا
django.setup()

from health.models import HealthData  # تأكد من استيراد النموذج بشكل صحيح


# دالة لتنظيف القيم غير الصالحة
def clean_range_value(value):
    """تنظيف القيم غير الصالحة وتحويلها إلى قيمة صالحة أو None"""
    if value == 'discrete' or value == 'None' or value == 'NaN':
        return None  # تجاهل القيم غير الصالحة
    try:
        return float(value)  # حاول تحويل القيمة إلى رقم عشري
    except ValueError:
        print(f"القيمة غير صالحة: {value}")
        return None  # إذا فشل التحويل، قم بإرجاع None


# دالة لتنظيف بيانات العمر
def clean_age(value):
    """تنظيف البيانات الخاصة بعمر المريض"""
    if isinstance(value, str):
        if '<' in value:
            return None  # تجاهل القيم مثل "< 12"
        elif '-' in value:
            # استخراج العمر من النطاق
            try:
                start_age, end_age = value.split(' - ')
                return int(start_age)  # اختيار العمر الأصغر أو المتوسط
            except ValueError:
                return None
        else:
            try:
                return int(value)
            except ValueError:
                return None
    return value


# دالة لقراءة ملف CSV وإدخال البيانات إلى قاعدة البيانات
def read_file(file_path):
    data = pd.read_csv(file_path)
    health_data_objects = []

    # طباعة أسماء الأعمدة للتأكد من صحتها
    print(data.columns)

    for index, row in data.iterrows():
        # تنظيف القيم غير الصالحة في الأعمدة الأخرى
        age_value = clean_age(row['age'])
        if age_value is None:
            print(f"القيمة غير صالحة للـ age في السطر {index}. يتم تخطي السطر.")
            continue  # تخطي السطر إذا كانت القيمة غير صالحة

        # معالجة القيم غير الصالحة في 'sex'
        if pd.isnull(row['sex']) or row['sex'] not in ['m', 'f']:
            print(f"القيمة غير صالحة للـ sex في السطر {index}. يتم تعيين القيمة الافتراضية.")
            row['sex'] = 'f'  # تعيين القيمة الافتراضية للـ sex إذا كانت فارغة أو غير صالحة

        # إضافة باقي الأعمدة مع التحقق من القيم غير الصالحة
        health_data_objects.append(
            HealthData(
                bp_diastolic=clean_range_value(row.get('bp (Diastolic)', None)),
                bp_limit=row.get('bp limit', None),
                sg=row.get('sg', None),
                al=row.get('al', None),
                class_field=row.get('class', None),
                rbc=row.get('rbc', None),
                su=row.get('su', None),
                pc=row.get('pc', None),
                pcc=row.get('pcc', None),
                ba=row.get('ba', None),
                bgr=row.get('bgr', None),
                bu=row.get('bu', None),
                sod=row.get('sod', None),
                sc=row.get('sc', None),
                pot=row.get('pot', None),
                hemo=row.get('hemo', None),
                pcv=row.get('pcv', None),
                rbcc=row.get('rbcc', None),
                wbcc=row.get('wbcc', None),
                htn=row.get('htn', None),
                dm=row.get('dm', None),
                cad=row.get('cad', None),
                appet=row.get('appet', None),
                pe=row.get('pe', None),
                ane=row.get('ane', None),
                grf=row.get('grf', None),
                stage=row.get('stage', None),
                affected=row.get('affected', None),
                age=age_value,  # القيمة التي تم التحقق منها
                sex=row['sex'],  # القيمة التي تم التحقق منها
            )
        )

    # إدخال البيانات في قاعدة البيانات باستخدام bulk_create
    try:
        HealthData.objects.bulk_create(health_data_objects)
        print(f"تم إدخال {len(health_data_objects)} سجلًا بنجاح.")
    except Exception as e:
        print(f"حدث خطأ أثناء إدخال البيانات: {e}")


# تحديد مسار ملف CSV
file_path = 'C:\\Baymax\\UPFile\\ckd-dataset-v2.csv'  # تأكد من المسار الصحيح للملف

# استدعاء الدالة لقراءة البيانات
read_file(file_path)
