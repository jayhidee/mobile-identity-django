from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler
# from django.urls import

from logs.views import errorHandeling
import json
import traceback


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code
        error = {
            "code": response.status_code,
            "error_type": "other error codes",
            "error_details": json.dumps(traceback.format_exc())
        }
        errorHandeling(error)
    return response
