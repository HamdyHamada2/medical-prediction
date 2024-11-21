from celery import shared_task


@shared_task
def import_data_task(file_path):
    import_data_from_csv(file_path)
