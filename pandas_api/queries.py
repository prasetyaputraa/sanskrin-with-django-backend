import pandas as pd
from .models import Dictionary

def get_translation(dictionary_df, word, from_lang):
    dictionary = Dictionary(dictionary_df)

    return dictionary.translate(word, from_lang)

def get_stats_from_dict(dictionary_df):
    dictionary = Dictionary(dictionary_df)

    return {
        'sanskrit_word_count': dictionary.get_word_count(),
        'translations_count': dictionary.get_translation_total_count(),
        'translations_mean': dictionary.get_translation_mean()
    }

def get_first_n_words(dictionary_df, n: int):
    dictionary_df = Dictionary(dictionary_df)

    n = int(n)

    n = 10 if n > 10 else n

    return dictionary_df.get_first_n_words(n)