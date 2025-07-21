from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .whois_service import get_whois_data
from .utils.response_helpers import parse_request_body, create_error_response, create_success_response
from .exceptions import (
    InvalidInputException,
    WhoisAPIException,
    WhoisDataNotFoundException,
    WhoisConfigurationException
)


@csrf_exempt
@require_POST
def whois_lookup(request):
    """
    Handle WHOIS lookup requests from frontend.
    
    Accepts POST requests with JSON body containing:
    - domain: Domain name to lookup (required)
    - type: Type of data to retrieve ('domain' or 'contact') (required)
    
    Returns:
        JsonResponse: JSON response with WHOIS data or error message
    """
    try:
        # Parse request body and extract parameters
        data = parse_request_body(request)
        domain = data.get("domain")
        data_type = data.get("type")
        
        # Get WHOIS data using the service
        result = get_whois_data(domain, data_type)
        
        # Return successful response
        return create_success_response(result)
        
    except InvalidInputException as e:
        return create_error_response(str(e), 400)
        
    except WhoisDataNotFoundException as e:
        return create_error_response(str(e), 404)
        
    except WhoisConfigurationException as e:
        return create_error_response(f"Service configuration error: {str(e)}", 500)
        
    except WhoisAPIException as e:
        return create_error_response(f"WHOIS service error: {str(e)}", 500)
        
    except Exception as e:
        return create_error_response(f"An unexpected error occurred: {str(e)}", 500)