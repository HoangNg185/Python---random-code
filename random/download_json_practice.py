import pandas as pd
import requests

# API endpoint URL
api_url = 'https://api.db.nomics.world/v22/series/WB/commodity_prices/FALUMINUM-1W.xlsx'

# Send a GET request to the API endpoint
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Save the JSON response to a file
    with open('data.xlsx', 'wb') as f:
        f.write(response.content)
    print('JSON file downloaded successfully.')
else:
    print('Failed to download JSON file. Status code:', response.status_code)

'''df=pd.read_json('data.json')
print(df)
df.to_excel('data from github1.xlsx')'''