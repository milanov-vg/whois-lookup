import json
from django.http import JsonResponse
from ..exceptions import InvalidInputException


def parse_request_body(request):
    """
    Parse and validate JSON request body.
    
    Args:
        request: Django HTTP request object
        
    Returns:
        dict: Parsed JSON data
        
    Raises:
        InvalidInputException: If request body is invalid JSON
    """
    try:
        return json.loads(request.body)
    except (json.JSONDecodeError, ValueError) as e:
        raise InvalidInputException(f"Invalid JSON in request body: {str(e)}")


def create_error_response(error_message, status_code):
    """
    Create standardized error response.
    
    Args:
        error_message (str): Error message to return
        status_code (int): HTTP status code
        
    Returns:
        JsonResponse: Django JSON response with error information
    """
    return JsonResponse({"error": error_message}, status=status_code)


def create_success_response(data):
    """
    Create standardized success response.
    
    Args:
        data (dict): Data to return in response
        
    Returns:
        JsonResponse: Django JSON response with success data
    """
    return JsonResponse(data, status=200)