from django.core.exceptions import ValidationError, ImproperlyConfigured
from django.http import Http404
import requests


# Custom exceptions
class InvalidInputException(ValidationError):
    """
    Raised when input data is invalid or missing required fields.
    Inherits from Django's ValidationError for consistency with Django patterns.
    """
    def __init__(self, message="Invalid input data"):
        super().__init__(message)


class WhoisConfigurationException(ImproperlyConfigured):
    """
    Raised when there's a configuration error.
    Inherits from Django's ImproperlyConfigured for configuration-related errors.
    """
    def __init__(self, message="WHOIS service configuration error"):
        super().__init__(message)


class WhoisDataNotFoundException(Http404):
    """
    Raised when WHOIS data is not found for the requested domain.
    Inherits from Django's Http404 for resource not found scenarios.
    """
    def __init__(self, message="WHOIS data not found"):
        super().__init__(message)


# Use standard Python exception for API errors
class WhoisAPIException(requests.RequestException):
    """
    Raised when there's an error communicating with the WHOIS API service.
    Inherits from requests.RequestException since it's related to HTTP API calls.
    """
    def __init__(self, message="WHOIS API communication error"):
        super().__init__(message)