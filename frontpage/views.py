from updater.models import bhav
from django.shortcuts import render, redirect,HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache

# Create your views here
CACHE_TTL = getattr(settings ,'CACHE_TTL' , 60*60*24)
def search(response):
    name = response.POST.get("name")
    if(name == None or name == "") :
        name = "FULLRESULT"
    if name:
        name = name.upper()
    if cache.get(name) :  
        result = cache.get(name)
    else :
        if name=='FULLRESULT':
            result = query(None)
        else:
            result = query(name)
        cache.set(name,result)
    if(name == 'FULLRESULT'):
        name = "Enter Equity Name"
    context = {'result' : result , 'equity' : name}
    return render(response,"frontpage/home.html",context)
def query(name = None):
    if name:
        equity = bhav.objects.filter(name__contains = name)
    else:
        equity = bhav.objects.all()
    return  equity



