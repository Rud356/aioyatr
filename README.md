# aioyatr
Async yandex.translate api wrapper for python

# Example of usage
```python
import asyncio
from aio_yandex_translate.translator import Translator
key = "TOKEN"

async def main():
    text = 'Hello world'
    print(text)
    t = Translator(key)
    r = await t.translate(text, to_language='ru')
    print(r)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

## Explaining some details
To get to exceptions that module can throw you may go
to Translator.exc and see classes of exceptions (TranslatorError is base)  
The code is really short but i hope it will help you!