from django.core.management.base import BaseCommand
import csv
from django.db import connections


class Command(BaseCommand):
    help = "Load data from CSV into the database"

    def handle(self, *args, **kwargs):
        file_path = "C:/Users/Flash-Tech/.cache/kagglehub/datasets/cleaned_merged_heart_dataset.csv"

        self.create_table_from_csv(file_path)
        self.load_data_to_db(file_path)

    def create_table_from_csv(self, file_path):
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            columns = reader.fieldnames  # استخراج أسماء الأعمدة من الملف

            # بناء استعلام SQL لإنشاء الجدول بناءً على الأعمدة
            column_definitions = ", ".join([f'"{column}" text' for column in columns])
            create_table_query = f"""
            CREATE TABLE IF NOT EXISTS "cleaned_merged_heart_dataset" (
                {column_definitions}
            );
            """

            # الاتصال بقاعدة البيانات
            with connections["default"].cursor() as cursor:
                cursor.execute(create_table_query)
                connections["default"].commit()
                self.stdout.write(
                    self.style.SUCCESS(f"تم إنشاء الجدول بناءً على الأعمدة: {columns}")
                )

    def load_data_to_db(self, file_path):
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            columns = reader.fieldnames  # استخراج أسماء الأعمدة من الملف

            # بناء استعلام SQL لإدخال البيانات
            insert_query = f"""
            INSERT INTO "cleaned_merged_heart_dataset"
            ({', '.join ([f'"{column}"' for column in columns])})
            VALUES ({', '.join (['%s' for _ in columns])})
            """

            # الاتصال بقاعدة البيانات
            with connections["default"].cursor() as cursor:
                for row in reader:
                    try:
                        cursor.execute(
                            insert_query, [row[column] for column in columns]
                        )
                    except Exception as e:
                        self.stderr.write(f"خطأ في إدخال البيانات: {e}")
                        continue  # متابعة باقي السطور في حالة حدوث خطأ
                connections["default"].commit()
                self.stdout.write(self.style.SUCCESS("تم إدخال البيانات بنجاح"))
