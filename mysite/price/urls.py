from django.urls import path
from .views import ZhannaPrice

app_name = "price"

urlpatterns = [
    path('', ZhannaPrice.as_view(), name='price'),
]

handler404 = "main.views.page_not_found_view"
