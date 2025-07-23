from django.urls import path, include
from api import views

urlpatterns = [
    path(
        "customer/inquiry",
        views.CustomerInfoInquiryVew.as_view(),
        name="customer_inquiry",
    )
]
