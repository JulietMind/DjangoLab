from django.shortcuts import render
from .models import Temas
from django.utils import timezone

# Create your views here.

def post_list(request):
	post = Temas.objects.filter(fecha_creacion__lte=timezone.now()).order_by('fecha_creacion')
	return render(request, 'whatever/post_list.html', {'post': post})