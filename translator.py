import aiohttp
try: import ujson as json
except ImportError: import json

# If you reading this - hello from Rud!
# Github repo: https://github.com/Rud356/aioyatr


class Translator:
    supported = {
        'az','sq','am','en','ar','hy','af','eu','ba','be','bn','my',
        'bg','bs','cy','hu','vi','ht','gl','nl','mrj','el','ka','gu',
        'da','he','yi','id','ga','it','is','es','kk','kn','ca','ky',
        'zh','ko','xh','km','lo','la','lv','lt','lb','mg','ms','ml',
        'mt','mk','mi','mr','mhr','mn','de','ne','no','pa','pap','fa',
        'pl','pt','ro','ru','ceb','sr','si','sk','sl','sw','su','tg',
        'th','tl','ta','tt','te','tr','udm','uz','uk','ur','fi','fr',
        'hi','hr','cs','sv','gd','et','eo','jv','ja'
    }
    valid_text_formats = {'plain', 'html'}
    base_url = 'https://translate.yandex.net/api/v1.5/tr.json/'

    def __init__(self,
        key: str,
        to_language: str = 'en',
        text_format = 'plain',
        hint = []
    ):
        self.key = str(key)
        if to_language not in Translator.supported:
            raise ValueError("You setted wrong language")

        self._language = to_language
        if text_format not in Translator.valid_text_formats:
            raise ValueError("You setted incorrect text format")

        self.hint = hint
        self.text_format = text_format

    @property
    def to_language(self):
        return self._language

    @to_language.setter
    def to_language(self, value: str):
        value = str(value)
        if value not in Translator.supported:
            raise ValueError("You setting wrong language")

        self._language = value

    async def detect_lang(self, text):
        url = Translator.base_url + 'detect?'
        data = {
            'key': self.key,
            'text': text,
            'hint': ','.join(self.hint)
        }

        async with aiohttp.ClientSession(
            json_serialize=json
        ) as session:
            response = await session.get(
                url, params=data
            )

            if response.status == 401:
                raise self.exc.TranslatorKeyInvalid('Invalid API key')

            if response.status == 402:
                raise self.exc.TranslatorKeyBlocked('Blocked API key')

            if response.status == 404:
                raise self.exc.TranslatorError('Ran out of daily limit of translated text')

            if response.status != 200:
                raise self.exc.TranslatorError(f"Failed detecting language ({response.reason})")

            data = await response.json()
            return data['lang']

    async def translate(self, text, from_language=None, to_language=None):
        if not from_language:
            from_language = await self.detect_lang(text)

        to_language = to_language or self.to_language

        if to_language not in Translator.supported:
            raise self.exc.TranslatorLanguage('Translating from language unsupported')

        if from_language not in Translator.supported:
            raise self.exc.TranslatorLanguage('Translating to language unsupported')

        url = Translator.base_url + "translate?"
        data = {
            "key": self.key,
            'text': text,
            'lang': f'{from_language}-{to_language}',
            'format': self.text_format
        }

        async with aiohttp.ClientSession(
            json_serialize=json
        ) as session:
            response = await session.get(
                url, params=data
            )

            if response.status == 401:
                raise self.exc.TranslatorKeyInvalid('Invalid API key')

            if response.status == 402:
                raise self.exc.TranslatorKeyBlocked('Blocked API key')

            if response.status == 404:
                raise self.exc.TranslatorError('Ran out of daily limit of translated text')

            if response.status == 413:
                raise self.exc.TranslatorError('Too long text')

            if response.status == 501:
                raise self.exc.TranslatorError('This translation direction unsupproted')

            if response.status != 200:
                raise self.exc.TranslatorError(f"Failed detecting language ({response.reason})")

            data = await response.json()
            return data['text'][0]

    class exc:
        class TranslatorError(Exception): ...
        class TranslatorKeyInvalid(TranslatorError): ...
        class TranslatorKeyBlocked(TranslatorError): ...
        class TranslatorLanguage(TranslatorError): ...
