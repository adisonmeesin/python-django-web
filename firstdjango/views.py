from django.http import HttpResponse
from django.shortcuts import render
from datetime import date


def home(request):
    return render(request, 'home.html')

def products(request):
    return render(request, 'products.html')

def contact(request):
    return render(request, 'contact.html')


# def index(request):
#     # return HttpResponse('my about page')
#     return render(request, 'index.html')


def about(request):
    return HttpResponse('my about page')


def search(request, keyword, page):
    return HttpResponse(f'Search for {keyword} page : {page}')


def maps(request):
    type = request.GET.get('type', 'hybrid')
    lat = request.GET.get('lat', '13.00')
    lon = request.GET.get('lon', '10.32654')
    zoom = request.GET.get('z', '10')

    return HttpResponse(f'Map type: {type}<br>Location: {lat},{lon}<br>Zoom: {zoom}')


def test(request):
    dt = date.today()
    data = {
        'site': {'title': 'django framwork', 'message': 'Hello Python Django'},
        'colors': ['red', 'green', 'blue'],
        'date': dt
    }
    return render(request, 'test.html', data)
