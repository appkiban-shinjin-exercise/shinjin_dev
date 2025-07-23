from db.models import CustomerInfo
from rest_framework import serializers


class CustomerInfoInquirySerializer(serializers.ModelSerializer):

    kanjiName = serializers.CharField(source="kanji_name")
    kanaName = serializers.CharField(source="kana_name")
    email = serializers.CharField(source="email")
    phoneNo = serializers.CharField(source="phone_no")
    address = serializers.CharField(source="address")
    planCode = serializers.CharField(source="plan_code")
    subscribedProduct = serializers.CharField(source="subscribed_product")
    registeredAt = serializers.CharField(source="registered_at")

    class Meta:

        model = CustomerInfo
        fields = {
            "kanjiName",
            "kanaName",
            "email",
            "phoneNo",
            "address",
            "planCode",
            "subscribedProduct",
            "registeredAt",
        }
