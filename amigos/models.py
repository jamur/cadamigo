from django.db import models

# Create your models here.

class Amigo(models.Model):
	nome = models.CharField(max_length=100)
	data_de_nascimento = models.DateTimeField('Data de Nascimento')


	def __str__(self):
		return self.nome


class Telefone(models.Model):
	telefone = models.CharField(max_length=30)
	amigo = models.ForeignKey(Amigo, on_delete=models.CASCADE)