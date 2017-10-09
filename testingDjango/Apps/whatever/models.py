from django.db import models
from django.utils import timezone

# Create your models here.

class Temas(models.Model):
	autor = models.ForeignKey('auth.User', null=True)
	titulo = models.CharField(max_length=100, null=False)
	texto = models.TextField(max_length=1000, null=False)
	categoria = models.CharField(max_length=35)
	fecha_creacion = models.DateTimeField(default=timezone.now)
	fecha_publicacion = models.DateTimeField(blank=True, null=True)
	
	def post(self):
		fecha_publicacion = timezone.now()
		self.save()

	def __str__(self):
		return self.titulo

