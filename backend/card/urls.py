from django.conf.urls import url 
from card import views 

urlpatterns = [ 
    url(r'^api/card$', views.card_list),
    url(r'^api/create_card$', views.create_card),
]