import pandas as pd
from pandas.io.json import json_normalize
import requests
import json
from pathlib import Path
RAW_DATA = Path('./Data/covid_19Data_raw.xlsx')
CLEAN_DATA = Path('./Data/covid_19Data_clean.xlsx')

def get_data(api = 'raw_data',key = 'raw_data'):
    json_data_url = requests.get('https://api.covid19india.org/'+api+'.json')
    js = json.loads(json_data_url.text)
    df = json_normalize(js[key])
    df.to_excel(RAW_DATA)
    return True

def clean_data():
    df = pd.read_excel(RAW_DATA)
    df['agebracket'].fillna(-1,inplace = True)
    mydf = df[['agebracket']][df['agebracket'].str.contains("-")== True] 
    mylist =mydf['agebracket'].unique()
    mydf = list(map(lambda x : avg(x),mylist))
    df['agebracket'] = df['agebracket'].replace(mylist,mydf)
    df['agebracket'] = pd.to_numeric(df['agebracket'])
    df['gender'].fillna('UK',inplace = True)
    df['statecode'].fillna('UK',inplace=True)
    df = df[['agebracket','gender','statecode','currentstatus','detectedstate']][df['detectedstate'].notna()]  
    df.to_excel(CLEAN_DATA)  
    return True

def avg(st):
    sum = 0
    for i in st.split("-"):
        sum += int(i)
    return str(sum/2)