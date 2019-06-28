from django.db import models


# Create your models here.
class Temperatura(models.Model):
    DESCRICAO = (
        ('EXTERNA', 'Externa'),
        ('INTERNA', 'Interna')
    )
    temperatura = models.FloatField()
    descricao = models.CharField(max_length=10, choices=DESCRICAO, default='INTERNA')
    tempo = models.DateTimeField()

    def __str__(self):
        return str(self.DESCRICAO + " -- " + self.temperatura)
