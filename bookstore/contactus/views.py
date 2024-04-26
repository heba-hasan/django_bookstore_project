
from django.http import HttpResponse
from django.shortcuts import render

def contactUS(request):
    return  render(request,'contactuspage.html')

