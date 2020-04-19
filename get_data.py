import pandas as pd
from pandas.io.json import json_normalize
import requests
import json
from pathlib import Path
RAW_DATA = Path('./covid_19Data_raw.xlsx')
CLEAN_DATA = Path('./covid_19Data_clean.xlsx')

def get_data(api = 'raw_data',key = 'raw_data'):
    print("Fetching data...")
    json_data_url = requests.get('https://api.covid19india.org/'+api+'.json')
    print("Fetching data completed...")
    print("Creating excel sheet...")
    js = json.loads(json_data_url.text)
    df = json_normalize(js[key])
    df.to_excel(RAW_DATA)
    print("Creating excel sheet completed...")
    return True

def clean_data():
    print("Cleaning data...")
    df = pd.read_excel(RAW_DATA)
    df['agebracket'].fillna(-1,inplace = True)
    df['gender'].fillna('UK',inplace = True)
    df['statecode'].fillna('UK',inplace=True)
    df = df[['agebracket','gender','statecode','currentstatus','detectedstate']][df['detectedstate'].notna()]  
    df.to_excel(CLEAN_DATA)  
    print("Cleaning data completed...")
    return True