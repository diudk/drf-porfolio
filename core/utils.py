from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        custom_response = dict()
        custom_response['errors'] = response.data
        custom_response['status_code'] = response.status_code
        response.data = custom_response

    return response
