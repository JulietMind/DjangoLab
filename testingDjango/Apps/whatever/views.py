from django.shortcuts import render
from .models import Temas
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# Create your views here.

def post_list(request):
	from django.shortcuts import render, get_object_or_404
	post = Temas.objects.filter(fecha_creacion__lte=timezone.now()).order_by('-fecha_creacion')
	return render(request, 'whatever/post_list.html', {'post': post})

def post_detail(request, pk):
    post = get_object_or_404(Temas, pk=pk)
    return render(request, 'whatever/post_detail.html', {'post': post})