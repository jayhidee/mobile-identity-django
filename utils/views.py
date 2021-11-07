from django.http import JsonResponse


def error_404(request, exception):
    message = ("Endpoint not found")
    response = JsonResponse(
        data={"message": message, "status": False, "ee": exception.detail})
    response.status_code = 404
    return response


def error_500(request):
    message = ("Error occured, we will look into it.")
    response = JsonResponse(data={"message": message, "status": False})
    response.status_code = 500
    return response


def error_503(request, exception):
    message = ("Error occured, we will look into it.")
    response = JsonResponse(data={"message": message, "status": False})
    response.status_code = 503
    return response
