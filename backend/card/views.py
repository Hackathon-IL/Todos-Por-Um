from django.http.response import JsonResponse
from rest_framework import views, viewsets
from rest_framework.decorators import api_view
from card.serializers import CardSerializer
from card.models import Card
from rest_framework.parsers import JSONParser

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
