import requests
import json
url = "https://www.gtabase.com/media/com_jamegafilter/en_gb/1.json?1702510451"

payload = {}
headers = {
  'authority': 'www.gtabase.com',
  'accept': 'application/json, text/javascript, */*; q=0.01',
  'accept-language': 'en-US,en;q=0.7',
  'cookie': '2ceb04f3a9f8c31f302453122c4da5e8=9a150a5b7334a629e065c50f3c7ced1f',
  'referer': 'https://www.gtabase.com/grand-theft-auto-v/vehicles/',
  'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'sec-gpc': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  'x-requested-with': 'XMLHttpRequest'
}

response = requests.request("GET", url, headers=headers, data=payload)

API = json.loads(response.text)
if response.status_code == 200:
    data = response.json()

   
    for key in data.keys():
        
        if key.startswith('item_'):
            name = API[key]['name']
            try:
                type = API[key]['attr']['ct1']['value'][0]
            except:
                type = 'N/A'
            try:
                speed = API[key]['attr']['ct6']['formatted_value']
            except:
                speed = 'N/A'
            try:
                accleration = API[key]['attr']['ct7']['formatted_value']
            except:
                accleration = 'N/A'
            try:
                handling = API[key]['attr']['ct9']['formatted_value']
            except:
                handling = 'N/A'   
            try:
                seats = API[key]['attr']['ct11']['formatted_value']
            except:
                seats = 'N/A' 
            try:
                price = API[key]['attr']['ct13']['formatted_value']
            except:
                price = 'N/A' 
                
            
            
            

