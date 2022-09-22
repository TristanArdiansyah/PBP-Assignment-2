from email import message
from typing import Counter
from django.shortcuts import render

from mywatchlist.models import WatchList
from django.http import HttpResponse
from django.core import serializers
# Create your views here.
def show_mywatchlist(request):
    data_watchlist = WatchList.objects.all()
    yescounter = 0
    totalcounter = 0
    for watched in data_watchlist:
        if watched.watched == "Yes":
            yescounter+=1
        totalcounter+=1
    
    message = "Wah, kamu masih sedikit menonton!"
    if (yescounter>(totalcounter-yescounter)):
        message = "Selamat, kamu sudah banyak menonton!"
    
    context = {
        'watchlist': data_watchlist,
        'nama': 'Nanda Tristan Ardiansyah',
        'npm' : '2106752086',
        'message' : message
    }
    return render(request, "mywatchlist.html",context)
def show_xml(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
