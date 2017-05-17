from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Category

def index(request):
	texts = ['lorem', 'fdsfsa']
	context = {
		'title' : 'django e-commerce',
		'texts' : texts,
		'categories' : Category.objects.all()
	}

	return render(request, 'index.html', context)

def contact(request):
	return render(request, 'contact.html')

