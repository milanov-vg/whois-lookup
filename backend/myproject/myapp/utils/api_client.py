import os
import json
import requests
from dotenv import load_dotenv
from ..exceptions import WhoisAPIException, WhoisDataNotFoundException

load_dotenv()

WHOIS_API_KEY = os.getenv("WHOIS_API_KEY")
WHOIS_BASE_URL = "https://www.whoisxmlapi.com/whoisserver/WhoisService"

# # For Testing purposes only
# current_dir = os.path.dirname(os.path.abspath(__file__))

# # Build the full path to test.json
# json_path = os.path.join(current_dir, 'test.json')

# # Load the JSON data
# with open(json_path, 'r') as f:
#     data = json.load(f)


def fetch_whois_data(domain):
    """
    Fetch WHOIS data from the API service.
    
    Args:
        domain (str): Domain name to lookup
        
    Returns:
        dict: WHOIS record data from the API
        
    Raises:
        WhoisAPIException: If API request fails
        WhoisDataNotFoundException: If no WHOIS data is found
    """
    try:
        # Make API request to WHOIS service
        response = requests.get(WHOIS_BASE_URL, params={
            "apiKey": WHOIS_API_KEY,
            "domainName": domain,
            "outputFormat": "JSON"
        })
        
        # Check if request was successful
        response.raise_for_status()
        
        # Parse JSON response
        api_response = response.json()
        whois_data = api_response.get("WhoisRecord", {})
        # whois_data = data["WhoisRecord"] # For testing purposes only
        if not whois_data:
            raise WhoisDataNotFoundException(f"No WHOIS data found for domain: {domain}")
            
        return whois_data
        
    except requests.RequestException as e:
        raise WhoisAPIException(f"Failed to fetch WHOIS data: {str(e)}")
    except ValueError as e:
        raise WhoisAPIException(f"Invalid JSON response from WHOIS API: {str(e)}")