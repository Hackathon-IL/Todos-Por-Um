from django.conf.urls import url 
from card import views 

urlpatterns = [ 
    url(r'^api/card$', views.card_list),
]