import requests
import json
import pandas as pd

# mempersiapkan data
url = 'http://www.floatrates.com/daily/idr.json'
json_data = requests.get(url)
m = json_data.json()
currency_list =[]

# menscrap data
for data in m.values():
    name = data['name']
    code = data['code']
    inverse = data['inverseRate']
    #print(name,code,inverse)
    tabel = {
        'Currency Name': name,
        'Currency Code': code,
        'Inverse Rate' : inverse
    }
    currency_list.append(tabel)

print(currency_list)

df = pd.DataFrame (currency_list)
df.to_csv ("./ IndonesiaCurrency.csv", index = False, header = False)
