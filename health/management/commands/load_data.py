# from django.core.management.base import BaseCommand
# import csv
# from django.db import connections
#
#
# class Command (BaseCommand):
#     help = 'Load data from CSV into the database'
#
#     def handle(self, *args, **kwargs):
#         file_path = "C:/Users/Flash-Tech/.cache/kagglehub/datasets/cleaned_merged_heart_dataset.csv"
#
#         self.create_table_from_csv (file_path)
#         self.load_data_to_db (file_path)
#
#     def create_table_from_csv(self, file_path):
#         with open (file_path, 'r') as file:
#             reader = csv.DictReader (file)
#             columns = reader.fieldnames  # استخراج أسماء الأعمدة من الملف
#
#             # بناء استعلام SQL لإنشاء الجدول بناءً على الأعمدة
#             column_definitions = ", ".join ([f'"{column}" text' for column in columns])
#             create_table_query = f"""
#             CREATE TABLE IF NOT EXISTS "cleaned_merged_heart_dataset" (
#                 {column_definitions}
#             );
#             """
#
#             # الاتصال بقاعدة البيانات
#             with connections['default'].cursor () as cursor:
#                 cursor.execute (create_table_query)
#                 connections['default'].commit ()
#                 self.stdout.write (self.style.SUCCESS (f"تم إنشاء الجدول بناءً على الأعمدة: {columns}"))
#
#     def load_data_to_db(self, file_path):
#         with open (file_path, 'r') as file:
#             reader = csv.DictReader (file)
#             columns = reader.fieldnames  # استخراج أسماء الأعمدة من الملف
#
#             # بناء استعلام SQL لإدخال البيانات
#             insert_query = f"""
#             INSERT INTO "cleaned_merged_heart_dataset"
#             ({', '.join ([f'"{column}"' for column in columns])})
#             VALUES ({', '.join (['%s' for _ in columns])})
#             """
#
#             # الاتصال بقاعدة البيانات
#             with connections['default'].cursor () as cursor:
#                 for row in reader:
#                     try:
#                         cursor.execute (insert_query, [row[column] for column in columns])
#                     except Exception as e:
#                         self.stderr.write (f"خطأ في إدخال البيانات: {e}")
#                         continue  # متابعة باقي السطور في حالة حدوث خطأ
#                 connections['default'].commit ()
#                 self.stdout.write (self.style.SUCCESS ("تم إدخال البيانات بنجاح"))

# from django.core.management.base import BaseCommand
# import os
# import pandas as pd
# from health.models import HealthData, AiModels, Diagnosis, Disease
# from django.db import models
# from django.core.exceptions import ValidationError
#
# # مسار مجلد الملفات
# UPLOAD_FOLDER = r'C:\Baymax\UPFile'
#
# # تعريف النماذج
# MODEL_MAPPING = {
#     'health': (HealthData, 'upload_to_health_data'),
#     'ai': (AiModels, 'upload_to_ai_models'),
#     'diagnosis': (Diagnosis, 'upload_to_diagnosis'),
#     'diseases': (Disease, 'upload_to_diseases'),
# }
#
# class Command(BaseCommand):
#     help = 'تحميل البيانات من الملفات وتخزينها في قاعدة البيانات'
#
#     def add_arguments(self, parser):
#         parser.add_argument(
#             '--files',
#             nargs='+',
#             type=str,
#             help='قائمة من مسارات الملفات التي تريد تحميلها'
#         )
#
#     def handle(self, *args, **options):
#         files = options['files']
#
#         if not files:
#             self.stdout.write(self.style.ERROR('يرجى تحديد الملفات لتحميلها باستخدام --files'))
#             return
#
#         for file_path in files:
#             try:
#                 file_name = os.path.basename(file_path)
#                 self.process_file(file_path, file_name)
#                 self.stdout.write(self.style.SUCCESS(f"تم رفع الملف بنجاح: {file_name}"))
#             except ValueError as e:
#                 self.stdout.write(self.style.ERROR(f"خطأ: {str(e)}"))
#             except Exception as e:
#                 self.stdout.write(self.style.ERROR(f"حدث خطأ أثناء رفع الملف {file_name}: {str(e)}"))
#
#     def process_file(self, file_path, file_name):
#         try:
#             if file_name.endswith('.csv'):
#                 df = pd.read_csv(file_path)
#             elif file_name.endswith('.xlsx'):
#                 df = pd.read_excel(file_path)
#             else:
#                 raise ValueError(f"Unsupported file type: {file_name}")
#
#             self.create_dynamic_fields(df)
#             df = self.clean_data(df)
#
#             # تحديد النموذج المناسب بناءً على اسم الملف
#             model_class, upload_function = self.get_model_choice(file_name)
#             upload_function(df)
#             report = self.generate_report(df, file_name, model_class.__name__)
#             self.stdout.write(report)
#         except Exception as e:
#             raise ValidationError(f"خطأ أثناء معالجة الملف {file_name}: {e}")
#
#     def create_dynamic_fields(self, df):
#         columns = df.columns
#         for column in columns:
#             if not hasattr(HealthData, column):
#                 column_type = df[column].dtype
#                 field = self.get_field_for_column_type(column_type)
#
#                 if field:
#                     field.contribute_to_class(HealthData, column)
#                     self.stdout.write(self.style.SUCCESS(f"تم إضافة العمود: {column}"))
#                 else:
#                     self.stdout.write(self.style.WARNING(f"النوع غير مدعوم للعمود: {column}"))
#             else:
#                 self.stdout.write(self.style.SUCCESS(f"العمود {column} موجود مسبقًا. سيتم إضافة البيانات فقط."))
#
#     def get_field_for_column_type(self, column_type):
#         if column_type == 'float64':
#             return models.FloatField(null=True, blank=True)
#         elif column_type == 'int64':
#             return models.IntegerField(null=True, blank=True)
#         elif column_type == 'bool':
#             return models.BooleanField(default=False)
#         elif column_type == 'datetime64[ns]':
#             return models.DateTimeField(null=True, blank=True)
#         elif column_type == 'object':
#             return models.CharField(max_length=255, blank=True, null=True)
#         else:
#             return None
#
#     def clean_data(self, df):
#         # معالجة الأعمدة المفقودة
#         missing_columns = [col for col in ['bp_diastolic', 'bp_limit', 'sg', 'al'] if col not in df.columns]
#         for column in missing_columns:
#             self.stdout.write(self.style.WARNING(f"العمود {column} غير موجود في البيانات. سيتم تخطيه أو استبداله بالقيم الافتراضية."))
#             if column == 'bp_diastolic':
#                 df['bp_diastolic'] = 0
#             else:
#                 df[column] = 0
#
#         df.fillna(0, inplace=True)
#         df = df[df['bp_diastolic'] > 0]  # تصفية البيانات
#         return df
#
#     def upload_to_health_data(self, df):
#         self.upload_to_model(df, HealthData)
#
#     def upload_to_ai_models(self, df):
#         fields_mapping = {
#             'model_name': 'model_name',
#             'accuracy': 'accuracy',
#             'parameters': 'parameters',
#         }
#         self.upload_to_model(df, AiModels, fields_mapping)
#
#     def upload_to_model(self, df, model_class, fields_mapping=None):
#         batch_size = 100
#         data_batch = []
#         for index, row in df.iterrows():
#             data = {column: row[column] for column in df.columns}
#             data_batch.append(data)
#             if len(data_batch) >= batch_size:
#                 self.save_batch_to_db(data_batch, model_class)
#                 data_batch = []
#         if data_batch:
#             self.save_batch_to_db(data_batch, model_class)
#
#     def save_batch_to_db(self, data_batch, model_class):
#         model_class.objects.bulk_create([model_class(**data) for data in data_batch])
#         self.stdout.write(self.style.SUCCESS(f"تم إدخال {len(data_batch)} سجل(s) بنجاح"))
#
#     def generate_report(self, df, file_name, model_name):
#         total_rows = len(df)
#         failed_rows = df.isnull().sum().sum()
#         report = (
#             f"تم رفع الملف: {file_name} إلى النموذج: {model_name}\n"
#             f"عدد الصفوف الكلية: {total_rows}\n"
#             f"عدد الأخطاء: {failed_rows}"
#         )
#         return report
#
#     def get_model_choice(self, file_name):
#         file_name_lower = file_name.lower()
#         if file_name.endswith('.csv') or file_name.endswith('.xlsx'):
#             if 'health' in file_name_lower:
#                 return MODEL_MAPPING['health']
#             elif 'ai' in file_name_lower:
#                 return MODEL_MAPPING['ai']
#             elif 'diagnosis' in file_name_lower:
#                 return MODEL_MAPPING['diagnosis']
#             elif 'diseases' in file_name_lower:
#                 return MODEL_MAPPING['diseases']
#             else:
#                 raise ValueError(f"Unknown file name format in file: {file_name}")
#         else:
#             raise ValueError(f"Unsupported file type: {file_name}")


import subprocess
from django.core.management.base import BaseCommand
import os
import pandas as pd
from health.models import HealthData, AiModels, Diagnosis, Disease
from django.db import models
from django.core.exceptions import ValidationError

# مسار مجلد الملفات
UPLOAD_FOLDER = r'C:\Baymax\UPFile'

# تعريف النماذج
MODEL_MAPPING = {
    'health': (HealthData, 'upload_to_health_data'),
    'ai': (AiModels, 'upload_to_ai_models'),
    'diagnosis': (Diagnosis, 'upload_to_diagnosis'),
    'diseases': (Disease, 'upload_to_diseases'),
}


class Command (BaseCommand):
    help = 'تحميل البيانات من الملفات وتخزينها في قاعدة البيانات'

    def add_arguments(self, parser):
        parser.add_argument (
            '--files',
            nargs='+',
            type=str,
            help='قائمة من مسارات الملفات التي تريد تحميلها'
        )

    def handle(self, *args, **options):
        files = options['files']

        if not files:
            self.stdout.write (self.style.ERROR ('يرجى تحديد الملفات لتحميلها باستخدام --files'))
            return

        for file_path in files:
            try:
                file_name = os.path.basename (file_path)
                self.process_file (file_path, file_name)
                self.stdout.write (self.style.SUCCESS (f"تم رفع الملف بنجاح: {file_name}"))
            except ValueError as e:
                self.stdout.write (self.style.ERROR (f"خطأ: {str (e)}"))
            except Exception as e:
                self.stdout.write (self.style.ERROR (f"حدث خطأ أثناء رفع الملف {file_name}: {str (e)}"))

    def process_file(self, file_path, file_name):
        try:
            if file_name.endswith ('.csv'):
                df = pd.read_csv (file_path)
            elif file_name.endswith ('.xlsx'):
                df = pd.read_excel (file_path)
            else:
                raise ValueError (f"Unsupported file type: {file_name}")

            self.create_dynamic_fields (df)
            df = self.clean_data (df)

            # تحديد النموذج المناسب بناءً على اسم الملف
            model_class, upload_function = self.get_model_choice (file_name)
            upload_function = getattr (self, upload_function)  # استدعاء الوظيفة الديناميكية
            upload_function (df)
            report = self.generate_report (df, file_name, model_class.__name__)
            self.stdout.write (report)
        except Exception as e:
            raise ValidationError (f"خطأ أثناء معالجة الملف {file_name}: {e}")

    def create_dynamic_fields(self, df):
        columns = df.columns
        for column in columns:
            if not hasattr (HealthData, column):
                column_type = df[column].dtype
                field = self.get_field_for_column_type (column_type)

                if field:
                    field.contribute_to_class (HealthData, column)
                    self.stdout.write (self.style.SUCCESS (f"تم إضافة العمود: {column}"))
                else:
                    self.stdout.write (self.style.WARNING (f"النوع غير مدعوم للعمود: {column}"))
            else:
                self.stdout.write (self.style.SUCCESS (f"العمود {column} موجود مسبقًا. سيتم إضافة البيانات فقط."))

        # إضافة الترحيلات
        self.create_migrations_and_migrate ()

    def create_migrations_and_migrate(self):
        subprocess.run (["python", "manage.py", "make migrations"])
        subprocess.run (["python", "manage.py", "migrate"])

    def get_field_for_column_type(self, column_type):
        if column_type == 'float64':
            return models.FloatField (null=True, blank=True)
        elif column_type == 'int64':
            return models.IntegerField (null=True, blank=True)
        elif column_type == 'bool':
            return models.BooleanField (default=False)
        elif column_type == 'datetime64[ns]':
            return models.DateTimeField (null=True, blank=True)
        elif column_type == 'object':
            return models.CharField (max_length=255, blank=True, null=True)
        else:
            return None

    def clean_data(self, df):
        # معالجة الأعمدة المفقودة
        df.fillna (0, inplace=True)
        return df

    def upload_to_health_data(self, df):
        for _, row in df.iterrows ():
            try:
                record_data = {}
                for column in df.columns:
                    if hasattr (HealthData, column):
                        record_data[column] = row.get (column)

                HealthData.objects.create (**record_data)
            except Exception as e:
                self.stdout.write (self.style.ERROR (f"خطأ في السطر: {row} - {e}"))

    def generate_report(self, df, file_name, model_name):
        total_rows = len (df)
        failed_rows = df.isnull ().sum ().sum ()
        report = (
            f"تم رفع الملف: {file_name} إلى النموذج: {model_name}\n"
            f"عدد الصفوف الكلية: {total_rows}\n"
            f"عدد الأخطاء: {failed_rows}"
        )
        return report

    def get_model_choice(self, file_name):
        file_name_lower = file_name.lower ()
        if 'health' in file_name_lower or 'breast-cancer' in file_name_lower:
            return MODEL_MAPPING['health']
        elif 'ai' in file_name_lower:
            return MODEL_MAPPING['ai']
        elif 'diagnosis' in file_name_lower:
            return MODEL_MAPPING['diagnosis']
        elif 'diseases' in file_name_lower:
            return MODEL_MAPPING['diseases']
        else:
            raise ValueError (f"Unknown file name format in file: {file_name}")


# الآن إضافة النموذج الخاص بك
class HealthData (models.Model):
    # سيتم إضافة الحقول هنا بناءً على الأعمدة في CSV
    pass


# إنشاء الحقول في النموذج بناءً على الأعمدة من CSV
def create_dynamic_fields_for_health_data():
    df = pd.read_csv ("path_to_your_file.csv")
    fields = {}
    for column in df.columns:
        fields[column] = models.FloatField ()  # اختر نوع الحقل المناسب مثل FloatField أو IntegerField

    # إنشاء النموذج باستخدام الحقول الديناميكية
    HealthData._meta.local_fields = fields


create_dynamic_fields_for_health_data ()


def load_health_data():
    df = pd.read_csv ("path_to_your_file.csv")
    for index, row in df.iterrows ():
        health_data = HealthData (**row.to_dict ())  # تحويل كل صف إلى قاموس
        health_data.save ()
