from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from .forms import RegistroForm
from .models import Perfil, Libro, Autor
from itertools import chain
from django.db.models.functions import Concat
from django.db.models import Value

#http://django-book.blogspot.com/2012/11/realizando-consultas-una-vez-que-hayas.html

@login_required()
def index(request):
	query =request.GET.get("q")
	if query == 0:

		libros = Libro.objects.all().order_by('-fecha_registro')[:8]
		return render(request, 'index.html', {'libros': libros})
		
	else:
		if query:
			libros=Libro.objects.annotate(nombrecompleto = Concat('autor__nombre', Value(' '), 'autor__apellido'),).filter(Q(titulo__icontains=query) | 
				Q(autor__nombre__icontains = query) | Q(autor__apellido__icontains=query) | Q(nombrecompleto__icontains = query)
				)
		else:
			libros = Libro.objects.all().order_by('-fecha_registro')[:8]
		return render(request, 'index.html', {'libros': libros})
	

class RegistroUsuario(CreateView):
	model = Perfil
	template_name = 'registrar.html'
	form_class = RegistroForm
	success_url = reverse_lazy('form_login')


  






