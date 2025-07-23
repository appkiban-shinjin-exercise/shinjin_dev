from http import HTTPStatus

from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from api.services.customer_info_inquiry_service import CustomerInfoInquiryService
from django.core.exceptions import ValidationError
from api.serializers.customer_info_inquiry_serializer import (
    CustomerInfoInquirySerializer,
)


class CustomerInfoInquiryVew(APIView):

    def post(self, request):

        response_data: dict = {
            "customerNo": request.data.get("customerNo"),
            "result": {"code": "2001", "message": ""},
        }

        if not isinstance(request.data.get("customerNo"), str):
            response_data["result"]["message"] = "顧客番号はstr型で指定してください"
            return Response(response_data, status=HTTPStatus.BAD_REQUEST)

        try:
            service = CustomerInfoInquiryService()

            result = service.get_the_data(request.data.get("customerNo"))
            serializer = CustomerInfoInquirySerializer(result, many=True)

        except ValidationError as e:
            response_data["result"]["message"] = e.message
            return Response(response_data, status=HTTPStatus.BAD_REQUEST)

        except Exception as ve:
            response_data.pop("customerNo")
            response_data["result"]["code"] = ""
            response_data["result"]["message"] = "システムエラー"
            return Response(response_data, status=HTTPStatus.INTERNAL_SERVER_ERROR)

        response_data["result"]["code"] = "1001"
        response_data["data"] = serializer.data

        return Response(response_data, status=HTTPStatus.OK)
