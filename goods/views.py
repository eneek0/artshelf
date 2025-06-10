# from email.mime import image
# from django.shortcuts import render

# from goods.models import Products

# # Create your views here.
# def catalog(request):


#     context: dict[str,] = {
#     }
#     return render(request, 'goods/catalog.html', context)

def product(request, product_slug):
    product: Products = Products.objects.get(slug=product_slug)

    context: dict[str, Products] = {
        'product': product
    }
    return render(request, 'goods/product.html', context=context)


from urllib import request
from django.core.paginator import Paginator
from django.shortcuts import render
from goods.models import Products
from goods.models import Categories  # если у тебя отдельная модель категорий

def catalog(request):
    page = request.GET.get('page', 1) 

    category_ids = request.GET.getlist('categories')  # получаем id выбранных категорий
    if category_ids:
        products = Products.objects.filter(category__id__in=category_ids).distinct()
    else:
        products = Products.objects.all()

    categories = Categories.objects.all()  # чтобы отрисовать список в шаблоне

    paginator = Paginator(products, 4)
    current_page = paginator.page(int(page))

    context = {
        'products': current_page,
        'categories': categories,
        'selected_categories': list(map(int, category_ids)),  # для галочек в чекбоксах
    }
    return render(request, 'goods/catalog.html', context)