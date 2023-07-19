from django.urls import path
from .views import Contacts

app_name = "contact"

urlpatterns = [
    path('', Contacts.as_view(), name='contact'),
]

handler404 = "main.views.page_not_found_view"
