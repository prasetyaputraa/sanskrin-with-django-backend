import pandas as pd
import numpy as np

class Dictionary:
    def __init__(self, dataframe):
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError('Expecting a pandas Dataframe object.')
        
        self.dataframe = dataframe

    def translate(self, word, from_lang='sanskrit'):
        if not from_lang in ['sanskrit', 'indonesian']:
            raise ValueError('Expecting sanskrit or indonesian')

        if from_lang == 'sanskrit':
            return self.dataframe.loc[self.dataframe['sanskrit'] == word]

        return self.dataframe.loc[self.dataframe['translations'].str.contains(word, na=False)]

    def get_word_count(self):
        return len(self.dataframe)

    def get_translation_total_count(self):
        return self.dataframe.length.sum()

    def get_translation_mean(self):
        return self.dataframe.length.mean()

    def get_first_n_words(self, n):
        return self.dataframe.head(n)

    def request_samples(self, data_length):
        return None