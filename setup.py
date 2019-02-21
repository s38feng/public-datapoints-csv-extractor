import setuptools

setuptools.setup(
    name='public-datapoints-csv-extractor',
    version='0.1',
    author="Sam Feng",
    author_email="samfeng279@gmail.com",
    description="Extractor for datapoints stored in CSV files",
    url="https://github.com/s38feng/public-datapoints-csv-extractor",
    packages=['public-datapoints-csv-extractor'],
    install_requires=[
        'pandas',
        'cognite-sdk'
    ],
    scripts=['bin/datapoints-csv-extractor.py'],
 )
