import os
from http import HTTPStatus

from django.http import JsonResponse


class Authentication:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        server_passphrase = os.environ.get("AUTH_PASSPHRASE")
        client_passphrase = request.headers.get("Auth-Phrase")

        if not client_passphrase:
            return JsonResponse(
                {
                    "result": {
                        "code": "401",
                        "message": HTTPStatus.UNAUTHORIZED.phrase,
                    }
                },
                status=HTTPStatus.UNAUTHORIZED,
            )

        if server_passphrase == client_passphrase:
            return self.get_response(request)

        else:
            return JsonResponse(
                {
                    "result": {
                        "code": "401",
                        "message": HTTPStatus.UNAUTHORIZED.phrase,
                    }
                },
                status=HTTPStatus.UNAUTHORIZED,
            )
