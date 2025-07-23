from db.models import CustomerInfo
import re
from django.core.exceptions import ValidationError


class CustomerInfoInquiryService:

    def get_the_data(self, customer_no):

        if not len(customer_no) == 11 or re.fullmatch("[0-9]+", customer_no) is None:
            raise ValidationError("顧客番号の形式が不正です")

        result = CustomerInfo.objects.get_the_data(customer_no)

        return result
