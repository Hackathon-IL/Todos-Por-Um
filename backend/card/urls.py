from django.conf.urls import url
from django.urls.conf import include, path 
from card import views 
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'card',views.CardViewSet)


urlpatterns = [ 
    path('',include(router.urls)),
]