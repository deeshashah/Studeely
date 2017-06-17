from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^topics/(?P<anystring>\w+)?/?$','magic.views.lot'),
    url(r'^test/(?P<anystring>\w+)?/?$','magic.views.test'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
