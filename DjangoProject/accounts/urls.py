from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^login/$','accounts.views.login'),
    url(r'^auth/$','accounts.views.auth_view'),
    url(r'^logout/$','accounts.views.logout'),
    url(r'^loggedin/$','accounts.views.loggedin'),
    url(r'^invalid/$','accounts.views.invalid_login'),
    url(r'^register/$','accounts.views.register_user'),
    url(r'^register_success/$','accounts.views.register_success'),
    url(r'^profile_update/$', 'accounts.views.user_profile'),
    url(r'^profile/$', 'accounts.views.profile'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)