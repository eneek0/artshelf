from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request) -> HttpResponse:
    context: dict[str, str] = {
        'content': "Авторская печатная продукция"
    }
    return render(request, 'main/index.html', context)

def authors(request) -> HttpResponse:
    context: dict[str, str] = {
    }
    return render(request, 'main/authors.html', context)

def events(request) -> HttpResponse:
    context: dict[str, str] = {
    }
    return render(request, 'main/events.html', context)