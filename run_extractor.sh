#!/usr/bin/env bash
pip3 install -e git+https://github.com/s38feng/public-datapoints-csv-extractor.git#egg=public-datapoints-csv-extractor
python3 -m bin.datapoints-csv-extractor $@
