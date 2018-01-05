
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include


# Third-party Libraries
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='Test Trafilea')),

    url(r'', include('security.urls')),

    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
]
