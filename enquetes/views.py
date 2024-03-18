from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def  index (request):
    return HttpResponse('DSWeb - 2024.1<br>Matrícula: 20231014040030<br>Nome: Giovana Barros')
