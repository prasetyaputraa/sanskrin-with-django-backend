import magic

from django import forms
from django.views import View
from django.template.response import TemplateResponse
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile
from django.http import HttpResponseRedirect

import pandas as pd

from pandas_api.queries import get_stats_from_dict, get_first_n_words
from pandas_api.preparations import persist_dictionary

from raw_excels.handlers import replace_in_use

from .models import RawModel

def validate_excel(data):
    mime = magic.from_buffer(data.read(1024), mime=True)

    if mime not in (
        'application/zip', 
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 
        'application/vnd.oasis.opendocument.spreadsheet'
        ):

        raise ValidationError('Invalid file type, expecting an excel spreadsheet.')

class Message:
    def __init__(self, message, tags=None):
        self.message = message
        self.tags = tags

    def __str__(self):
        return self.message

class UploadExcelForm(forms.Form):
    excel_file = forms.FileField(validators=[validate_excel])

class RawDataView(View):
    def get(self, request, **kwargs):
        app_list = kwargs.get('admin_site').get_app_list(request)

        stats = get_stats_from_dict(request.dictionary)

        data = {
            'opts': RawModel._meta,
            'title': 'Upload Raw Data',
            'change': True,
            'is_popup': False,
            'save_as': False,
            'has_permission': True,
            'has_delete_permission': False,
            'has_change_permission': False,
            'has_add_permission': False,
            'has_file_field': True,
            'is_nav_sidebar_enabled': True,
            'available_apps': app_list,
            'dictionary_statistics': stats,
            'messages': [],
            'form': UploadExcelForm()
        }

        # query params handling
        if request.GET.get('samples'):
            try:
                data['samples'] = get_first_n_words(request.dictionary, request.GET['samples']).to_html()
            except ValueError:
                pass

        # end of query params handling

        if kwargs.get('excel_path'):
            data['excel_path'] = kwargs.get('excel_path')

        if kwargs.get('success'):
            data['messages'].append(Message(kwargs.get('success'), 'success'))

        if kwargs.get('errors'):
            data['errors'] = kwargs.get('errors')

        response = TemplateResponse(request, 'admin/raw_data/upload.html', data)

        return response

    def post(self, request, **kwargs):
        form = UploadExcelForm(request.POST, request.FILES)

        if form.is_valid():
            path = replace_in_use(request.FILES['excel_file'])
            persist_dictionary(path, 'final_dictionary.pkl')

            request.dictionary = pd.read_pickle('final_dictionary.pkl')

            kwargs['excel_path'] = path
            kwargs['success'] = 'File saved and processed successfully'
        else:
            kwargs['errors'] = form.errors
        
        return self.get(request, **kwargs)