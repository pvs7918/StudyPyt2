# from random import random
import random

from django.shortcuts import render
from django.http import HttpResponse
from .models import SaveCoin, Client, Product, Order


def index(request):
    return HttpResponse("Hello, world!")


def coin(request):
    rnd_coin = random.choice(["Орел", "Решка"])
    save_coin = SaveCoin(coin_variant=rnd_coin)
    save_coin.save()
    return HttpResponse(rnd_coin)

def clients(request):
    client = Client.objects.all()
    return HttpResponse(client)

def clients(request, id):
    client = Client.objects.all()
    return HttpResponse(client)