import re
import os

import pandas as pd
import numpy as np

def persist_dictionary(xlsx_path, persistence_path):
    df_sheets_dict = pd.read_excel(xlsx_path, sheet_name=None, header=None)

    df = pd.concat(df_sheets_dict.values())

    df.columns = ['sanskrit', 'translations']

    df.reset_index(inplace=True, drop=True)

    df_pos_tr = df['translations'].str.extract(r'(^[^\s]+)(.*)', expand=True)

    df_pos_tr.columns = ['part of speech', 'translations']

    df.drop(columns=['translations'], inplace=True)

    final_dataframe = df.join(df_pos_tr)

    final_dataframe['length'] = final_dataframe['translations'].str.split(';')
    final_dataframe['length'] = final_dataframe['length'].apply(lambda x: len(x) if isinstance(x, list) else 0)

    final_dataframe.dropna()

    final_dataframe['translations'].str.strip()

    final_dataframe.to_pickle(persistence_path)