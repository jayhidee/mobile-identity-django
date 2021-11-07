import traceback
import json
from logging import exception
from django.http import JsonResponse

from logs.views import errorHandeling


def error_404(request, exception):
    message = ("Endpoint not found")
    response = JsonResponse(
        data={"message": message, "status": False})
    response.status_code = 404
    error = {
        "code": response.status_code,
        "error_type": request.get_full_path(),
        "error_details": json.dumps(traceback.format_exc()) + " - URL" + request.get_full_path()
    }
    errorHandeling(error)
    return response


def error_403(request, exception):
    message = ("Error occured, we will look into it.")
    response = JsonResponse(
        data={"message": message, "status": False})
    response.status_code = 403
    error = {
        "code": response.status_code,
        "error_type": request.get_full_path(),
        "error_details": json.dumps(traceback.format_exc()) + " - URL" + request.get_full_path()
    }
    errorHandeling(error)
    return response


def error_500(request):
    message = ("Error occured, we will look into it.")
    response = JsonResponse(data={"message": message, "status": False})
    response.status_code = 500
    error = {
        "code": response.status_code,
        "error_type": request.get_full_path(),
        "error_details": json.dumps(traceback.format_exc())
    }
    errorHandeling(error)
    return response


def error_503(request, exception):
    message = ("Error occured, we will look into it.")
    response = JsonResponse(data={"message": message, "status": False})
    response.status_code = 503
    error = {
        "code": response.status_code,
        "error_type": request.get_full_path(),
        "error_details": json.dumps(traceback.format_exc())
    }
    errorHandeling(error)
    return response
