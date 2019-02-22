# public-datapoints-csv-extractor
Public version of datapoints-csv-extractor released as a package

# To use:
`sh run_extractor.sh -d DATA_TYPE -p PATH`

Where:
- DATA_TYPE: "historical" or "live" (if live, the earliest desired date of processing needs to be modified in the script under LAST_PROCESSED_TIMESTAMP)
- PATH: path to the folder containing the relevant data
