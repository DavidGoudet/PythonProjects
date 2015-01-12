from django.shortcuts import render, render_to_response, RequestContext
from django.template import RequestContext
from django.http import HttpResponse, HttpRequest

def default(request):
    return render(request, 'index.html')

# Create your views here.
