import glob

from os import path, rename, remove
from datetime import datetime

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

LIMIT = 10

def get_excel_files_paths(dir_path):
    excel_files_paths = glob.glob('{}/*.xlsx'.format(dir_path))
    return excel_files_paths

def replace_in_use(file):
    if path.exists('raw_excels/in_use.xlsx'):
        rename('raw_excels/in_use.xlsx', 'raw_excels/in_use_before_{}.xlsx'.format(datetime.now()))
        excel_path = default_storage.save('raw_excels/in_use.xlsx', file)

        excel_files_paths = get_excel_files_paths('raw_excels/')

        if len(excel_files_paths) > LIMIT:
            oldest_file = None
            oldest_date = None

            for excel_file in excel_files_paths:
                if excel_file == 'raw_excels/in_use.xlsx':
                    continue

                datetime_str = excel_file.replace('raw_excels/in_use_before_', '').replace('.xlsx', '')

                datetime_instance = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S.%f")

                if not oldest_file:
                    oldest_file = excel_file
                    oldest_date = datetime_instance

                    continue

                if datetime_instance < oldest_date:
                    oldest_file = excel_file
                    oldest_date = datetime_instance

            if oldest_file:
                remove(oldest_file)
    else:
        excel_path = default_storage.save('raw_excels/in_use.xlsx', file)
        

    return excel_path