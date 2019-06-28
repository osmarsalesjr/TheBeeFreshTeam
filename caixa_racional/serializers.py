from rest_framework import serializers
from caixa_racional.models import Temperatura


class TemperaturaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Temperatura
        fields = ('temperatura', 'descricao', 'tempo')
