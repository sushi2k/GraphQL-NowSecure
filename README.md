# NowSecure Auto - GraphQL

This repo contains two scripts:

- **query_all_scans_convert_to_csv.py** - This script will query GraphQL from NowSecure Auto to get all meta-data of all your uploaded applications, including all scans of each app. After the data was saved as `result.json` the JSON structure will be flattened and saved as csv file.
- **downloader.py** - This script will parse the csv file and will download the mobile app that was uploaded for the scan. 

## Documentation

- <https://docs.nowsecure.com/api/auto/graphql>: GraphQL API Documentation
- <https://lab-api.nowsecure.com/graphql>: Write your GraphQL query directly into your browser, or click on "Schema" on the right and search for all available details that can be retrieved via GraphQL.

## Usage

First install the requirements:

```bash
$ pip install -r requirements.txt
```

Create the file `.apikey` and store your API-Key for NowSecure Auto into the file:

```bash
$ touch .apikey
$ echo "API-KEY" > .apikey
```

Afterwards the script `query_all_scans_convert_to_csv.py` can be executed and the output will look similar to the below:

```bash
$ python3 query_all_scans_convert_to_csv.py
     Assessment_reference   Assessment_createdAt         App_build_digest         ...           package_key       Platform       AnalysisConfigLevel
0    123-4321-123-4321-123  2020-01-03T03:57:46.366275Z  12341234123412341234...  ...           com.bar.foo       ios            BASELINE
1    123-4321-123-4321-321  2020-04-30T04:10:06.908146Z  12341234123412341234...  ...           com.foo.bar       ios            BASELINE
...

[432 rows x 10 columns]
```

Two new files have now been created:

- `result.json`
- `result.csv`

The python script `downloader.py` does the following:

- parse the csv
- collect the information needed from the csv to download the file
- download the APK/IPA via wget
- store the file in the directory `downloads` and give it a unique name.

```bash
$ python3 downloader.py
```

## requirements.txt

`requirements.txt` was created with `pipreqs`.
