"""
管理画面にモデルを登録するためのファイル
"""

from django.contrib import admin

from .models import CustomerInfo


# class CustomerInfoAdmin(admin.ModelAdmin):
# list_display = ["customer_no", "kanji_name", "email", "plan_code"]
# search_fields = ["customer_no", "kanji_name", "email"]
# list_filter = ["plan_code", "registered_at"]
# ordering = ["-registered_at"]

admin.site.register(CustomerInfo)
