from django.db import models
from django.core.exceptions import ValidationError


class CustomerInfoManager(models.Manager):

    def get_the_data(self, customer_no):

        if not isinstance(customer_no, str):
            raise ValidationError("顧客番号はstr型で指定してください")

        result = CustomerInfo.objects.filter(customer_no=customer_no)

        return result


class CustomerInfo(models.Model):
    customer_no = models.CharField(max_length=20, verbose_name="顧客番号")
    kanji_name = models.CharField(max_length=40, verbose_name="漢字氏名")
    kana_name = models.CharField(max_length=40, verbose_name="カナ氏名")
    email = models.EmailField(max_length=50, verbose_name="メールアドレス")
    phone_no = models.CharField(max_length=20, verbose_name="電話番号")
    address = models.TextField(max_length=100, verbose_name="住所")
    plan_code = models.CharField(max_length=20, verbose_name="契約プランコード")
    subscribed_product = models.CharField(max_length=50, verbose_name="契約商品")
    registered_at = models.DateTimeField(verbose_name="登録日時")

    def __str__(self):
        return f"{self.customer_no} - {self.kanji_name}"

    objects = CustomerInfoManager()

    class Meta:
        app_label = "db"
        verbose_name = "顧客情報"
        verbose_name_plural = "顧客情報一覧"
        db_table = "TB_CUSTOMER_INFO"
