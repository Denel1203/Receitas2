from django.db import models


class Receitas(models.Model):
    Name = models.CharField(max_length=30)
    Nome_Receita= models.CharField(max_length=30)
    Ingredientes= models.TextField(max_length=200)
    Instrucoes = models.TextField(max_length=600)
    Notas = models.TextField(max_length=200)
    
    def __str__(self):
        return self.Name
    
class Comentario(models.Model):
    Nome = models.CharField(max_length=50)
    comentario= models.TextField(max_length=120)
    def __str__(self):
        return self.Nome