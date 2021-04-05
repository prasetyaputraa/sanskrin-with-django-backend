class NotFoundWord(Exception):
    def __init__(self, word):
        super().__init__(word)

class NotFoundTargetWord(NotFoundWord):
    pass

class NotFoundSourceWord(NotFoundWord):
    pass

class Dictionary():
    def __init__(self, table, source_lang, target_lang):
        self.table = table
        self.source_lang = source_lang
        self.target_lang = target_lang

        self.direction = '{}_{}'.format(source_lang, target_lang)

    def translate(self, word):
        try:
            self.translation = getattr(self, 'translate_{}'.format(self.direction))(word)
        except AttributeError:
            raise AttributeError(
                "Dictionary can not translate a source language: {} to target language: {}"
                .format(self.source_lang, self.target_lang)
                )

        return self

    def translate_sanskrit_indonesian(self, word):
        translation = self.table.get(word, None)

        if translation is None:
            raise NotFoundSourceWord

        if translation == '' or translation == []:
            raise NotFoundTargetWord

        return translation

    def translate_indonesian_sanskrit(self, word):
        translation = self.table.get(word, None)

        if translation is None:
            raise NotFoundSourceWord

        if translation == '' or translation == []:
            raise NotFoundTargetWord

        return translation

class Translation():
    def __init__(self):
        pass