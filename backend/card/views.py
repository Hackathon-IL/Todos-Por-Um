from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from card.serializers import CardSerializer
from card.models import Card
from django.shortcuts import render
from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework.parsers import JSONParser

@api_view(['GET'])
def card_list(request):
    if request.method == 'GET':
        cards = Card.objects.all()
        #Pega o valor de uma variável GET com o nome 'página', e se não existir, retorna None
        title = request.GET.get('title',None)
        if title is not None:
            cards = cards.filter(title__icontains=title)
        card_serializer = CardSerializer(cards, many=True)
        return JsonResponse(card_serializer.data, safe=False)
    
@api_view(['POST'])
def create_card(request):
    if request.method == 'POST':
        card_data = JSONParser().parse(request)
        card_serizalizer = CardSerializer(data=card_data)

        if card_serizalizer.is_valid():
            card_serizalizer.save()
            return JsonResponse(card_serizalizer.data, status=201) #created
        return JsonResponse(card_serizalizer.error_messages, status = 400)# bad request