from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.nome