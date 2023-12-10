#create a program that will calculate the return on investment for a rental property 

import requests

def get_financial_data():
    
    api_url = "https://www.biggerpockets.com/investment-calculators"
    
 if response.status_code == 200:
    print('success')
    data = response.json()
    print(data)
else:
    print('Error')
  