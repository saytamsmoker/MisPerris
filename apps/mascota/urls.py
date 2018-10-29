from django.urls import path,include
from apps.mascota.views import index, mascota_view,mascota_list
from django.conf.urls import url
app_name="apps"

urlpatterns = [
    url(r'^$', index,name='index'),
    path('nuevo/', mascota_view, name='mascota_crear'),
    path('listar/',mascota_list, name='mascota_listar'),

]