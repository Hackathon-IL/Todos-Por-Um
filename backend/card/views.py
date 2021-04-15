from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from card.serializers import CardSerializer
from card.models import Card
from django.shortcuts import render
from django.contrib.auth.models import Group
from rest_framework import viewsets

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
