from django.contrib import admin
# from django.conf.urls import include
from django.urls import path, include

urlpatterns = [
    path('', include('leads.urls')),
    path('', include('frontend.urls'))
]
