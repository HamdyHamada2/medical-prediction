import os
import sys
import csv
from django.db import connections
from django.core.wsgi import get_wsgi_application

# تأكد من إضافة المسار الصحيح
sys.path.append('C:/Baymax')  # تأكد أن المسار يحتوي على مجلد المشروع

# تهيئة Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Baymax.settings")  # تأكد من اسم المشروع بالحروف الكبيرة
application = get_wsgi_application()

def create_table_from_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        columns = reader.fieldnames  # استخراج أسماء الأعمدة من الملف

        # بناء استعلام SQL لإنشاء الجدول بناءً على الأعمدة
        column_definitions = ", ".join([f'"{column}" text' for column in columns])
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS "ACPs_Breast_cancer" (
            {column_definitions}
        );
        """

        # الاتصال بقاعدة البيانات
        with connections['default'].cursor() as cursor:
            cursor.execute(create_table_query)
            connections['default'].commit()
            print("تم إنشاء الجدول بناءً على الأعمدة:", columns)


def load_data_to_db(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        columns = reader.fieldnames  # استخراج أسماء الأعمدة من الملف

        # بناء استعلام SQL لإدخال البيانات
        insert_query = f"""
        INSERT INTO "ACPs_Breast_cancer"
        ({', '.join([f'"{column}"' for column in columns])})
        VALUES ({', '.join(['%s' for _ in columns])})
        """

        # الاتصال بقاعدة البيانات
        with connections['default'].cursor() as cursor:
            for row in reader:
                try:
                    cursor.execute(insert_query, [row[column] for column in columns])
                except Exception as e:
                    print(f"خطأ في إدخال البيانات: {e}")
                    continue  # متابعة باقي السطور في حالة حدوث خطأ
            connections['default'].commit()
            print("تم إدخال البيانات بنجاح")

# def create_table_from_csv(file_path):
#     with open(file_path, 'r') as file:
#         csv_reader = csv.reader(file)
#         header = next(csv_reader)
#         print("تم إنشاء الجدول بناءً على الأعمدة:", header)
#
#         for row in csv_reader:
#             if len(row) == len(header):  # تأكد من أن السطر يحتوي على نفس عدد الأعمدة
#                 try:
#                     # عملية الإدخال في قاعدة البيانات هنا
#                     print("تم إدخال البيانات:", row)
#                 except Exception as e:
#                     print(f"خطأ في إدخال البيانات: {e}")
#             else:
#                 print(f"بيانات غير مكتملة في السطر: {row}")
#


# استخدام الدوال
file_path = "C:/Users/Flash-Tech/.cache/kagglehub/datasets/ACPs_Breast_cancer.csv"
create_table_from_csv(file_path)  # إنشاء الجدول بناءً على الأعمدة
load_data_to_db(file_path)  # تحميل البيانات


# import os
# import sys
# import csv
# from django.db import connections
# from django.core.wsgi import get_wsgi_application
#
# # تأكد من إضافة المسار الصحيح
# sys.path.append ('C:/Baymax')  # تأكد أن المسار يحتوي على مجلد المشروع
#
# # تهيئة Django
# os.environ.setdefault ("DJANGO_SETTINGS_MODULE", "Baymax.settings")  # تأكد من اسم المشروع بالحروف الكبيرة
# application = get_wsgi_application ()
#
#
# def create_table_from_csv(file_path):
#     with open (file_path, 'r') as file:
#         reader = csv.DictReader (file)
#         columns = reader.fieldnames  # استخراج أسماء الأعمدة من الملف
#
#         # تحديد نوع البيانات بناءً على الأعمدة
#         column_definitions = []
#         for column in columns:
#             # إذا كان العمود يحتوي على أرقام، قم باستخدام INTEGER
#             column_definitions.append (f'"{column}" TEXT')  # يمكن تعديل النوع هنا حسب الحاجة
#
#         # بناء استعلام SQL لإنشاء الجدول بناءً على الأعمدة
#         create_table_query = f"""
#         CREATE TABLE IF NOT EXISTS "cleaned_merged_heart_dataset" (
#             {', '.join (column_definitions)}
#         );
#         """
#
#         # الاتصال بقاعدة البيانات
#         with connections['default'].cursor () as cursor:
#             cursor.execute (create_table_query)
#             connections['default'].commit ()
#             print ("تم إنشاء الجدول بناءً على الأعمدة:", columns)
#
#
# def load_data_to_db(file_path):
#     with open (file_path, 'r') as file:
#         reader = csv.DictReader (file)
#         columns = reader.fieldnames  # استخراج أسماء الأعمدة من الملف
#
#         # بناء استعلام SQL لإدخال البيانات
#         insert_query = f"""
#         INSERT INTO "cleaned_merged_heart_dataset"
#         ({', '.join ([f'"{column}"' for column in columns])})
#         VALUES ({', '.join (['%s' for _ in columns])})
#         """
#
#         # الاتصال بقاعدة البيانات
#         with connections['default'].cursor () as cursor:
#             for row in reader:
#                 try:
#                     cursor.execute (insert_query, [row[column] for column in columns])
#                 except Exception as e:
#                     print (f"خطأ في إدخال البيانات: {e}")
#                     continue  # متابعة باقي السطور في حالة حدوث خطأ
#             connections['default'].commit ()
#             print ("تم إدخال البيانات بنجاح")
#
#
# # استخدام الدوال
# file_path = "C:/Users/Flash-Tech/.cache/kagglehub/datasets/cleaned_merged_heart_dataset.csv"
# create_table_from_csv (file_path)  # إنشاء الجدول بناءً على الأعمدة
# load_data_to_db (file_path)  # تحميل البيانات
