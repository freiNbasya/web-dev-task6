from django.shortcuts import render
from django.http import HttpResponseNotFound
from .info.info import APIs

def main_page(request):
    context = {
        'apis': APIs['APIs']
    }
    return render(request, 'main_page.html', context)

