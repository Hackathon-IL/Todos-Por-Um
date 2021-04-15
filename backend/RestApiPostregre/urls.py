from card.views import CardViewSet
from django.conf.urls import include
from django.contrib import admin
from django.db import router
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('card.urls')),
]
