from rest_framework import status, exceptions

from .error_codes import *


class CustomValidationException(exceptions.APIException):
    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(self, default_message="Validation error"):
        error_message = DEFAULT_ERROR

        # Check if error_message is a string or a dictionary
        if isinstance(error_message, str):
            error_code, error_message = error_message.split('-')
        elif isinstance(error_message, dict):
            error_code = error_message.get('code', 'Unknown')
            error_message = error_message.get('message', default_message)
        else:
            error_code = 'Unknown'
            error_message = str(error_message)

        self.detail = error_message
        self.code = error_code
