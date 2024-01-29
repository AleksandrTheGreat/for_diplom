from django.shortcuts import render
from .models import Price

def index(request):
    prices = Price.objects.all()
    data = {'prices':prices}
    return render(request,'index.html',context=data)