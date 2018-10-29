from django.urls import path,include

from apps.contacto.views import index_contacto,contacto_view

app_name="apps"
urlpatterns = [
	path('nuevo', index_contacto,name='contacto'),
	path('nuevo/', contacto_view,name='nuevocontacto'),
]