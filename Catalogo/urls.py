from django.conf.urls import url
from .import views 
from .views import RegistroUsuario

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^registrar/$', RegistroUsuario.as_view(), name='registrar'),

] 
