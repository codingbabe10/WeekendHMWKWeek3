import property_information

def Property_information():
    
    api_url = "https://www.biggerpockets.com/analysis/rentals/new#"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching financial data: {e}")
        return None