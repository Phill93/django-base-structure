'''Root URL Config'''
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings

from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)