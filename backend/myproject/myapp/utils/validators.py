import os
from dotenv import load_dotenv
from ..exceptions import InvalidInputException, WhoisConfigurationException

load_dotenv()


def validate_whois_config():
    """
    Validate WHOIS API configuration.
    
    Raises:
        WhoisConfigurationException: If API key is not configured
    """
    whois_api_key = os.getenv("WHOIS_API_KEY")
    if not whois_api_key:
        raise WhoisConfigurationException("WHOIS API key is not configured in environment variables")


def validate_request_data(domain, data_type):
    """
    Validate input data for WHOIS lookup request.
    
    Args:
        domain (str): Domain name to lookup
        data_type (str): Type of data to retrieve ('domain' or 'contact')
        
    Raises:
        InvalidInputException: If domain is missing or data_type is invalid
    """
    if not domain:
        raise InvalidInputException("Domain name is required")
    
    if data_type not in ["domain", "contact"]:
        raise InvalidInputException("Data type must be 'domain' or 'contact'")