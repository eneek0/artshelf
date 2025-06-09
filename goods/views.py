from email.mime import image
from django.shortcuts import render

from goods.models import Products

# Create your views here.
def catalog(request):


    context: dict[str,] = {
    }
    return render(request, 'goods/catalog.html', context)

def product(request):
    return render(request, 'goods/product.html')