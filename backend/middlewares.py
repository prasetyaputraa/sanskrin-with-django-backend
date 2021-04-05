from os import path

import pandas as pd

from pandas_api.preparations import persist_dictionary

class LoadDictionaryDataframeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        if not path.exists('final_dictionary.pkl'):
            persist_dictionary('raw_excels/in_use.xlsx', 'final_dictionary.pkl')

        self.dictionary_df = pd.read_pickle('final_dictionary.pkl')

    def __call__(self, request):
        # if request.GET.get('reassign'):
        self.dictionary_df = pd.read_pickle('final_dictionary.pkl')

        request.dictionary = self.dictionary_df

        response = self.get_response(request)

        return response