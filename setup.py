import setuptools

setuptools.setup(
    name='aio_yandex_translate',
    version='1.0',
    author="Rud356",
    author_email='devastator12a@mail.ru',
    description="Yandex translate async api wrapper",
    license='GPLv3',
    url="https://github.com/Rud356/aioyatr",
    install_requires=['aiohttp>=3.6',],
    extras_require={'ujson':'1.35'},
    classifiers=[
        "Programming Language :: Python :: 3.6 Python :: 3.7 Python :: 3.8",
        "License :: OSI APPROVED :: GNU GENERAL PUBLIC LICENSE V3 OR LATER (GPLV3+)",
        "Operating System :: OS OS Independent",
        "Intended Audience :: Developers",
        "natural Language :: English",
    ],
    python_requires='>=3.6'
)