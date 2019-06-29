from django.db import models
import jsonfield


# Create your models here.
class Temperatura(models.Model):
    DESCRICAO = (
        ('EXTERNA', 'Externa'),
        ('INTERNA', 'Interna')
    )
    temperatura = models.FloatField()
    descricao = models.CharField(max_length=10, choices=DESCRICAO, default='INTERNA')
    tempo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.DESCRICAO + " -- " + self.temperatura)


class BaseDeDados(models.Model):
    base = jsonfield.JSONField()
    data_criacao = models.DateTimeField(auto_now_add=True)
