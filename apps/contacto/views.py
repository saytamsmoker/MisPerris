from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.contacto.forms import ContactoForm
from apps.contacto.models import Contacto
# Create your views here.
def index_contacto(request):
	return render("contacto/contacto_form.html")

def contacto_view(request):
	if request.method =='POST':
		form = ContactoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('contacto/contacto_form.html')
	else:
		form = ContactoForm()

	return render(request, 'contacto/contacto_form.html',{'form':form})

def contacto_list(request):
	contacto = Contacto.objects.all()
	contexto = {'contacto':contacto}
	return render(request, 'contacto/contacto_list.html',contexto)