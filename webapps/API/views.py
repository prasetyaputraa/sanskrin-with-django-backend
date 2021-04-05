from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import exceptions

from modules.entities.dictionary import Dictionary
from pandas_api.queries import get_translation

from django_apps.submitted_translations.models import TranslationSubmission, TranslationMap

class TranslateWordView(APIView):

    def get(self, request):
        word = request.query_params.get('word')
        from_lang = request.query_params.get('lang', 'sanskrit')

        if not word:
            return Response({}, status=200)

        translation = {word: get_translation(request.dictionary, word, from_lang)}

        if translation[word].empty:
            translation[word] = {}
        else:
            translation[word] = translation[word].to_json()

        data = {
            'translation': translation
        }

        import time
        time.sleep(1)

        return Response(data, status=200)

class TranslateSentenceView(APIView):

    def post(self, request):
        sentence =  request.data.get('sentence')
        from_lang = 'sanskrit'

        if not sentence:
            return Response({}, status=200)

        translations = {word: get_translation(request.dictionary, word, from_lang) for word in sentence.split()}

        translations = {word: ({} if trans.empty else trans.to_json()) for word, trans in translations.items()}

        data = {
            'sentence': sentence,
            'translations': translations
        }

        import time
        time.sleep(1)

        return Response(data, status=200)

class TranslateSubmissionView(APIView):

    def post(self, request):
        sentences = request.data.get('sentences')
        translations = request.data.get('translations')

        message = ''

        if (not translations):
            message = 'Terjemahan belum dibangun.'

        if (not sentences) or (not translations):
            return Response({'error_message': message}, status=400)

        translation_submission = TranslationSubmission()

        trans_maps = []

        for (source_place, data) in translations.items():
            if int(source_place) < 0:
                source_place = None

            translation_map = {'source_place': int(source_place), 'coordinate': data['coordinate'], 'translation': data['translation']}

            trans_maps.append(translation_map)

        translation_submission.maps = trans_maps
        translation_submission.sentences = sentences

        translation_submission.save()

        return Response({}, status=200)
