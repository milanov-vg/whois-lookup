from .utils.validators import validate_whois_config, validate_request_data
from .utils.api_client import fetch_whois_data
from .utils.data_processors import process_domain_data, process_contact_data

def get_whois_data(domain, data_type):
    """
    Main function to get WHOIS data based on domain and data type.

    Args:
        domain (str): Domain name to lookup
        data_type (str): Type of data to retrieve ('domain' or 'contact')

    Returns:
        dict: Processed WHOIS data based on requested type

    Raises:
        WhoisConfigurationException: If API is not properly configured
        InvalidInputException: If input parameters are invalid
        WhoisAPIException: If API request fails
        WhoisDataNotFoundException: If no data is found for the domain
        ValueError: If unsupported data_type is provided
    """
    # Validate configuration
    validate_whois_config()

    # Validate input parameters
    validate_request_data(domain, data_type)

    # Fetch raw WHOIS data from API
    whois_data = fetch_whois_data(domain)

    try:
        if data_type == "domain":
            return process_domain_data(whois_data)
        elif data_type == "contact":
            return process_contact_data(whois_data)
        else:
            raise ValueError(f"Unsupported data_type: {data_type}")
    except Exception as e:
        raise e 
