from urllib import request
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from goods.models import Products, Favorite
from goods.models import Categories
from goods.utils import q_search  # если у тебя отдельная модель категорий
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST


def catalog(request):
    page = request.GET.get('page', 1) 
    order_by = request.GET.get('order_by', None) 
    query = request.GET.get('q', None) 

    category_ids = request.GET.getlist('categories')  # получаем id выбранных категорий
    if category_ids:
        products = Products.objects.filter(category__id__in=category_ids).distinct()
    elif query:
        products = q_search(query)
    else:
        products = Products.objects.all()

    if order_by and order_by != "default":
        products = products.order_by(order_by)

    categories = Categories.objects.all()  # чтобы отрисовать список в шаблоне

    paginator = Paginator(products, 40)
    current_page = paginator.page(int(page))

    context = {
        'products': current_page,
        'categories': categories,
        'selected_categories': list(map(int, category_ids)),  # для галочек в чекбоксах
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):
    product = get_object_or_404(Products, slug=product_slug)
    favorite_products = []

    if request.user.is_authenticated:
        favorite_products = Favorite.objects.filter(user=request.user).values_list('product_id', flat=True)

    return render(request, 'goods/product.html', {
        'product': product,
        'favorite_products': favorite_products,
    })


@login_required
@require_POST
def toggle_favorite(request, product_slug):
    try:
        product = Products.objects.get(slug=product_slug)
    except Products.DoesNotExist:
        return JsonResponse({'error': 'Товар не найден'}, status=404)

    favorite, created = Favorite.objects.get_or_create(user=request.user, product=product)

    if not created:
        favorite.delete()
        return JsonResponse({'status': 'removed'})
    else:
        return JsonResponse({'status': 'added'})
