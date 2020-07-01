import setuptools

with open('README.md') as f:
    text = f.read()

setuptools.setup(
    name="aio_yandex_translate",
    version="1.1.0",
    author="Rud356",
    author_email="devastator12a@mail.ru",
    description="Yandex translate async api wrapper",
    long_description=text,
    long_description_content_type="text/markdown",
    license="GPLv3",
    url="https://github.com/Rud356/aioyatr",
    packages=["aio_yandex_translate"],
    package_dir={"aio_yandex_translate": ""},
    install_requires=["aiohttp>=3.6", "aiohttp-proxy>=0.1.2"],
    extras_require={"ujson":"1.35"},
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Natural Language :: English",
    ],
    python_requires=">=3.6"
)