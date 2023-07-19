from django.urls import path, re_path, include
from .views import *
# from  django.views.decorators.cache import cache_page

app_name = "main"

urlpatterns = [
    re_path(r'^$', ZhannaIndex.as_view(), name='home'),  # cache_page(60)(ZhannaIndex.as_view()),
    path('shooting/<slug:shooting_slug>/', ShowShooting.as_view(), name='shooting'),
    re_path('^contact/', include('contact.urls')),
    re_path('^about_me/', include('about_me.urls')),
    re_path('^blog/', include('blog.urls')),
    re_path('^price/', include('price.urls')),

]

handler404 = "main.views.page_not_found_view"
