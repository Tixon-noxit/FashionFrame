from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from mysite import settings
from main.views import page_not_found_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]

if settings.DEBUG:
    # import debug_toolbar
    from django.urls import include, path

    #urlpatterns = [
    #    path('__debug__/', include('debug_toolbar.urls')),
    #] +
    #urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found_view
