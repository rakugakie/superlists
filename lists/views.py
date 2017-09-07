from django.shortcuts import render
from django.http import HttpResponse
#from django.Http import HttpResponse



def home_page(request):

    return render(request, 'home.html')
