from card.models import Card
from rest_framework import fields, serializers


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'title', 'description')