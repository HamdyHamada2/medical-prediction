# import pandas as pd
# import os
# from django.core.files.storage import FileSystemStorage
# from django.core.exceptions import ValidationError
# from myapp.models import HealthData, AiModels, Diagnosiss, Diseases  # استبدل بنماذجك الخاصة
#
# # تحديد المجلد الذي يحتوي على الملفات المرفوعة
# UPLOAD_FOLDER = r'C:\Baymax\UPFile'  # تم تحديث المسار هنا
#
#
# # النموذج لتحميل البيانات
# def upload_files_from_folder():
#     # قراءة جميع الملفات من المجلد المحدد
#     files = [f for f in os.listdir (UPLOAD_FOLDER) if f.endswith (('.csv', '.xlsx'))]
#
#     # معالجة كل ملف على حدة
#     for file_name in files:
#         file_path = os.path.join (UPLOAD_FOLDER, file_name)
#
#         # رفع البيانات ومعالجتها
#         with open (file_path, 'rb') as file:
#             try:
#                 process_file (file, file_name)
#                 print (f"تم رفع الملف بنجاح: {file_name}")
#             except Exception as e:
#                 print (f"حدث خطأ أثناء رفع الملف {file_name}: {str (e)}")
#
#
# # معالجة البيانات المرفوعة
# def process_file(file, file_name):
#     # تحديد نوع الملف (CSV أو Excel)
#     df = pd.read_csv (file) if file.name.endswith ('.csv') else pd.read_excel (file)
#
#     # تنظيف البيانات قبل رفعها
#     df = clean_data (df)
#
#     # رفع البيانات إلى النموذج المناسب
#     model_choice = get_model_choice (file_name)  # الحصول على النموذج المناسب بناءً على اسم الملف أو محتوياته
#     if model_choice == 'health':
#         upload_to_health_data (df)
#     elif model_choice == 'ai':
#         upload_to_ai_models (df)
#     elif model_choice == 'diagnosis':
#         upload_to_diagnosiss (df)
#     elif model_choice == 'diseases':
#         upload_to_diseases (df)
#
#     # تقرير النتائج
#     report = generate_report (df, file_name)
#     print (report)
#
#
# # تنظيف البيانات
# def clean_data(df):
#     # هنا يمكنك تطبيق إجراءات تنظيف مثل ملء القيم المفقودة
#     df.fillna ({
#         'bp_diastolic': 0, 'bp_limit': 120, 'sg': 1.0, 'al': 1.0
#         # أضف المزيد من القيم الافتراضية هنا حسب الحاجة
#     }, inplace=True)
#     # إزالة القيم غير الصالحة (على سبيل المثال الأعمار السلبية)
#     df = df[df['bp_diastolic'] > 0]
#     return df
#
#
# # رفع البيانات إلى نموذج HealthData
# def upload_to_health_data(df):
#     for index, row in df.iterrows ():
#         health_data = HealthData (
#             bp_diastolic=row.get ('bp_diastolic', None),
#             bp_limit=row.get ('bp_limit', None),
#             sg=row.get ('sg', None),
#             al=row.get ('al', None),
#             # إضافة باقي الأعمدة هنا
#         )
#         health_data.save ()
#
#
# # رفع البيانات إلى نموذج AiModels
# def upload_to_ai_models(df):
#     for index, row in df.iterrows ():
#         ai_model = AiModels (
#             # إضافة الأعمدة الخاصة بنموذج AiModels
#         )
#         ai_model.save ()
#
#
# # رفع البيانات إلى نموذج Diagnosiss
# def upload_to_diagnosiss(df):
#     for index, row in df.iterrows ():
#         diagnosis = Diagnosiss (
#             # إضافة الأعمدة الخاصة بنموذج Diagnosiss
#         )
#         diagnosis.save ()
#
#
# # رفع البيانات إلى نموذج Diseases
# def upload_to_diseases(df):
#     for index, row in df.iterrows ():
#         disease = Diseases (
#             # إضافة الأعمدة الخاصة بنموذج Diseases
#         )
#         disease.save ()
#
#
# # تقرير نتائج عملية الرفع
# def generate_report(df, file_name):
#     successful_rows = len (df)
#     failed_rows = df.isnull ().sum ().sum ()  # حساب البيانات المفقودة أو الأخطاء
#     report = f"الملف: {file_name} تم رفع {successful_rows} صفوف بنجاح. يوجد {failed_rows} صفوف تحتوي على بيانات مفقودة أو أخطاء."
#     return report
#
#
# # دالة لاختيار النموذج بناءً على محتويات الملف (أو الاسم)
# def get_model_choice(file_name):
#     # هنا يمكن إضافة منطق لاختيار النموذج بناءً على اسم الملف أو محتوياته
#     if 'health' in file_name.lower ():
#         return 'health'
#     elif 'ai' in file_name.lower ():
#         return 'ai'
#     elif 'diagnosis' in file_name.lower ():
#         return 'diagnosis'
#     elif 'disease' in file_name.lower ():
#         return 'diseases'
#     return 'health'  # القيمة الافتراضية
#
#
# # يمكنك استخدام هذه الدالة لرفع كل الملفات من المجلد:
# upload_files_from_folder ()
#
# import pandas as pd
# import os
# from django.core.exceptions import ValidationError
# from myapp.models import HealthData, AiModels, Diagnosiss, Diseases
#
# UPLOAD_FOLDER = r'C:\Baymax\UPFile'
#
# MODEL_MAPPING = {
#     'health': (HealthData, upload_to_health_data),
#     'ai': (AiModels, upload_to_ai_models),
#     'diagnosis': (Diagnosiss, upload_to_diagnosiss),
#     'diseases': (Diseases, upload_to_diseases),
# }
#
# REQUIRED_COLUMNS = ['bp_diastolic', 'bp_limit', 'sg', 'al']
#
#
# def upload_files_from_folder():
#     files = [f for f in os.listdir(UPLOAD_FOLDER) if f.endswith(('.csv', '.xlsx'))]
#     for file_name in files:
#         file_path = os.path.join(UPLOAD_FOLDER, file_name)
#         with open(file_path, 'rb') as file:
#             try:
#                 process_file(file, file_name)
#                 print(f"تم رفع الملف بنجاح: {file_name}")
#             except Exception as e:
#                 print(f"حدث خطأ أثناء رفع الملف {file_name}: {str(e)}")
#
#
# def process_file(file, file_name):
#     try:
#         df = pd.read_csv(file) if file.name.endswith('.csv') else pd.read_excel(file)
#         validate_columns(df)
#         df = clean_data(df)
#
#         model_class, upload_function = get_model_choice(file_name)
#         upload_function(df)
#         report = generate_report(df, file_name, model_class.__name__)
#         print(report)
#     except Exception as e:
#         raise ValidationError(f"خطأ أثناء معالجة الملف {file_name}: {e}")
#
#
# def validate_columns(df):
#     missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]
#     if missing_columns:
#         raise ValidationError(f"الأعمدة المفقودة: {missing_columns}")
#
#
# def clean_data(df):
#     df.fillna({
#         'bp_diastolic': 0,
#         'bp_limit': 120,
#         'sg': 1.0,
#         'al': 1.0
#     }, inplace=True)
#     df = df[df['bp_diastolic'] > 0]
#     return df
#
#
# def upload_to_health_data(df):
#     fields_mapping = {
#         'bp_diastolic': 'bp_diastolic',
#         'bp_limit': 'bp_limit',
#         'sg': 'sg',
#         'al': 'al'
#     }
#     upload_to_model(df, HealthData, fields_mapping)
#
#
# def upload_to_model(df, model_class, fields_mapping):
#     for index, row in df.iterrows():
#         data = {field: row.get(column, None) for column, field in fields_mapping.items()}
#         model_instance = model_class(**data)
#         model_instance.save()
#
#
# def generate_report(df, file_name, model_name):
#     total_rows = len(df)
#     failed_rows = df.isnull().sum().sum()
#     report = (
#         f"تم رفع الملف: {file_name} إلى النموذج: {model_name}\n"
#         f"عدد الصفوف الكلية: {total_rows}\n"
#         f"عدد الأخطاء: {failed_rows}"
#     )
#     return report
#
#
# upload_files_from_folder()
#


import os
import pandas as pd
from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
from health.models import HealthData, AiModels, Diagnosiss, Diseases

UPLOAD_FOLDER = r'C:\Baymax\UPFile'

MODEL_MAPPING = {
    'health': (HealthData, 'upload_to_health_data'),
    'ai': (AiModels, 'upload_to_ai_models'),
    'diagnosis': (Diagnosiss, 'upload_to_diagnosiss'),
    'diseases': (Diseases, 'upload_to_diseases'),
}

REQUIRED_COLUMNS = ['bp_diastolic', 'bp_limit', 'sg', 'al']


class Command (BaseCommand):
    help = 'Uploads files from a folder and saves them to the database'

    def handle(self, *args, **kwargs):
        self.upload_files_from_folder ()

    def upload_files_from_folder(self):
        files = [f for f in os.listdir (UPLOAD_FOLDER) if f.endswith (('.csv', '.xlsx'))]
        for file_name in files:
            file_path = os.path.join (UPLOAD_FOLDER, file_name)
            with open (file_path, 'rb') as file:
                try:
                    self.process_file (file, file_name)
                    self.stdout.write (self.style.SUCCESS (f"تم رفع الملف بنجاح: {file_name}"))
                except Exception as e:
                    self.stdout.write (self.style.ERROR (f"حدث خطأ أثناء رفع الملف {file_name}: {str (e)}"))

    def process_file(self, file, file_name):
        try:
            df = pd.read_csv (file) if file.name.endswith ('.csv') else pd.read_excel (file)
            self.validate_columns (df)
            df = self.clean_data (df)

            model_class, upload_function = self.get_model_choice (file_name)
            upload_function (df)
            report = self.generate_report (df, file_name, model_class.__name__)
            self.stdout.write (report)
        except Exception as e:
            raise ValidationError (f"خطأ أثناء معالجة الملف {file_name}: {e}")

    def validate_columns(self, df):
        missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]
        if missing_columns:
            raise ValidationError (f"الأعمدة المفقودة: {missing_columns}")

    def clean_data(self, df):
        df.fillna ({
            'bp_diastolic': 0,
            'bp_limit': 120,
            'sg': 1.0,
            'al': 1.0
        }, inplace=True)
        df = df[df['bp_diastolic'] > 0]
        return df

    def upload_to_health_data(self, df):
        fields_mapping = {
            'bp_diastolic': 'bp_diastolic',
            'bp_limit': 'bp_limit',
            'sg': 'sg',
            'al': 'al'
        }
        self.upload_to_model (df, HealthData, fields_mapping)

    def upload_to_ai_models(self, df):
        fields_mapping = {
            'model_name': 'model_name',
            'accuracy': 'accuracy',
            'parameters': 'parameters',
        }
        self.upload_to_model (df, AiModels, fields_mapping)

    def upload_to_model(self, df, model_class, fields_mapping):
        for index, row in df.iterrows ():
            data = {field: row.get (column, None) for column, field in fields_mapping.items ()}
            model_instance = model_class (**data)
            model_instance.save ()

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
        if 'health' in file_name:
            return MODEL_MAPPING['health']
        elif 'ai' in file_name:
            return MODEL_MAPPING['ai']
        elif 'diagnosis' in file_name:
            return MODEL_MAPPING['diagnosis']
        elif 'diseases' in file_name:
            return MODEL_MAPPING['diseases']
        else:
            raise ValueError (f"Unknown file type: {file_name}")
