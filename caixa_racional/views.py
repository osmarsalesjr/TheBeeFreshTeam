from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics

from caixa_racional.models import Temperatura
from caixa_racional.serializers import TemperaturaSerializer
''', BaseDeDadosSerializer'''


class TemperaturaList(generics.ListCreateAPIView):
    queryset = Temperatura.objects.all()
    serializer_class = TemperaturaSerializer
    name = 'temperatura-list'


class TemperaturaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Temperatura.objects.all()
    serializer_class = TemperaturaSerializer
    name = 'temperatura-detail'

'''
class BaseDeDadosList(generics.ListCreateAPIView):
    queryset = BaseDeDados.objects.all()
    serializer_class = BaseDeDadosSerializer
    name = 'base-de-dados-list'


class BaseDeDadosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BaseDeDados.objects.all()
    serializer_class = BaseDeDadosSerializer
    name = 'base-de-dados-detail'

'''
# Create your views here.
class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'temperaturas': reverse(TemperaturaList.name, request=request),
            #'base-de-dados': reverse(BaseDeDadosList.name, request=request),
        })
