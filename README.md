# aio_yandex_translate

Async yandex.translate api wrapper for python

## Example of usage

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

If you need to use proxies

```python
import asyncio
from aio_yandex_translate.translator import Translator
key = "TOKEN"

async def main():
    text = 'Hello world'
    t = Translator(key, proxy="http://user:password@127.0.0.1:1080")
    r = await t.translate(text, to_language='ru')
    print(r)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

See [aiohttp-proxy](https://pypi.org/project/aiohttp-proxy/), it should also support socks proxies

Changing proxies on a go

```python
import asyncio
from aio_yandex_translate.translator import Translator
key = "TOKEN"

async def main():
    text = 'Hello world'
    t = Translator(key, proxy="http://user:password@127.0.0.1:1080")
    r = await t.translate(text, to_language='ru')

    t.proxy = "http://user:password@localhost:1080"
    r = await t.translate(text, to_language='ru')
    print(r)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

Detecting language

```python
async def main():
    text = 'Hello world'
    t = Translator(key, proxy="http://user:password@127.0.0.1:1080")
    r = await t.detect_lang(text)
    print(r)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

You also may use keyword argument `hint` to give a list of languages, that should be preffered when detecting langs  
To add new hint you should use function `add_hint` with passed lang parameter 
in return you'll get bool value representing if it was added  
To remove lang from hints:

```python
from aio_yandex_translate.translator import Translator
key = "TOKEN"
translator = Translator(key)
translator.add_hint("en")
translator.hints.remove("en")
```

## Explaining some details
To get to exceptions that module can throw you may go
to Translator.exc and see classes of exceptions (TranslatorError is base)  
The code is really short but i hope it will help you!