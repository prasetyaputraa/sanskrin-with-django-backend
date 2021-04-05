import os

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError

from django.views import View

class DownloadDoc(View):
    def get(self, request):

        os.system('mongoexport --collection=submitted_translations_translationsubmission --db=sanskrin --out={}'
            .format(os.getcwd() + '/privates/submission_dump.json'))

        file_path = os.getcwd() + '/privates/submission_dump.json'

        try:
            with open(file_path, 'r') as f:
                file_data = f.read()

            response = HttpResponse(file_data, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="submission_dump.json"'
        except IOError as e:
            response = HttpResponseServerError(e)

        return response