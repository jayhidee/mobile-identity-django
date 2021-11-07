from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler
from django.urls import

from logs.views import errorHandeling
import json


def custom_exception_handler(request, exc, context):
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code
        error = {
            "code": response.status_code,
            "error_type": exc.detail,
            "error_details": json.dumps(exc.get_full_details()) + " - URL" + request.get_full_path()
        }
        errorHandeling(error)
    return response


def _handle_authentication_error(exc, context, response):
    pass
