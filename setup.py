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
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Natural Language :: English",
    ],
    python_requires='>=3.6'
)