import csv, json
import pandas as pd
import requests

json_data_url = requests.get('https://shorturl.at/nsv45')
json_file = open('/Users/prabodhmayekar/Documents/rawjson.json','w')
json_file.write(str(json_data_url.text))
json_file.close()

fileInput = '/Users/prabodhmayekar/Documents/rawjson.json'
fileOutput = '/Users/prabodhmayekar/Documents/raw2.csv'
inputFile = open(fileInput) 
outputFile = open(fileOutput, 'w') 
data = json.load(inputFile)
inputFile.close()
output = csv.writer(outputFile)
output.writerow(data['raw_data'][0].keys())
for row in data['raw_data']:
    output.writerow(row.values())
    
pd.read_csv(fileOutput).to_excel('/Users/prabodhmayekar/Documents/covid_19Data.xlsx')
print('Completed...')

