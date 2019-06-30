from rest_framework import serializers
from caixa_racional.models import Temperatura, BaseDeDados


class TemperaturaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Temperatura
        fields = ('url', 'pk', 'temperatura', 'descricao', "tempo")


class BaseDeDadosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BaseDeDados
        fields = ('url', 'pk', 'base', 'data_criacao')
