from django.urls import path
from myapp.views import whois_lookup

urlpatterns = [
    path('api/whois/', whois_lookup),
]
