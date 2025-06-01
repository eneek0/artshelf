from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request) -> HttpResponse:
    context: dict[str, str] = {
        'content': "Авторская печатная продукция"
    }
    return render(request, 'main/index.html', context)