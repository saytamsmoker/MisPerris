from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.contacto.forms import ContactoForm
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