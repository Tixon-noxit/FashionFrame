from django.urls import path
from .views import AboutMe

app_name = "about_me"

urlpatterns = [
    path('', AboutMe.as_view(), name='about_me'),
]

handler404 = "main.views.page_not_found_view"
