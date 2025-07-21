# def format_hostnames(hostnames_list, max_length=25):
#     """
#     Format hostname list into a string with length limitation.
    
#     Args:
#         hostnames_list (list): List of hostname strings
#         max_length (int): Maximum length of the formatted string
        
#     Returns:
#         str: Formatted hostname string, truncated if necessary
#     """
#     if not hostnames_list:
#         return ""
    
#     hostnames_str = ", ".join(hostnames_list)
#     if len(hostnames_str) > max_length:
#         hostnames_str = hostnames_str[:max_length] + "..."
    
#     return hostnames_str


def process_domain_data(whois_data):
    """
    Process WHOIS data for domain information request.
    
    Args:
        whois_data (dict): Raw WHOIS data from API
        
    Returns:
        dict: Processed domain information
    """
    # Extract hostname information
    hostnames = whois_data.get("nameServers", {}).get("hostNames", [])
    # hostnames_str = format_hostnames(hostnames)
    
    # Build domain information response
    result = {
        "domainName": whois_data.get("domainName"),
        "registrarName": whois_data.get("registrarName"),
        "registrationDate": whois_data.get("createdDate"),
        "expirationDate": whois_data.get("expiresDate"),
        "estimatedDomainAge": whois_data.get("estimatedDomainAge"),
        "hostnames": hostnames
    }
    
    return result


def process_contact_data(whois_data):
    """
    Process WHOIS data for contact information request.
    
    Args:
        whois_data (dict): Raw WHOIS data from API
        
    Returns:
        dict: Processed contact information
    """
    # Extract contact information
    contact_email = whois_data.get("contactEmail")
    
    # Build contact information response
    result = {
        "registrantName": whois_data.get("registrant", {}).get("name"),
        "technicalContactName": whois_data.get("technicalContact", {}).get("name"),
        "administrativeContactName": whois_data.get("administrativeContact", {}).get("name"),
        "contactEmail": contact_email
    }
    
    return result