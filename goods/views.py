from email.mime import image
from django.shortcuts import render

# Create your views here.
def catalog(request):
    context: dict[str,] = {
        "goods": [
            {
                "image": "deps/assets/im_trying_to_be_cool_about_it.webp",
                "title": "Значок “I’m trying to be cool about it”",
                "user": "sfiiosadlk",
                "price": 300,
            },
            {
                "image": "deps/assets/cat_poster.webp",
                "title": "Постер с ДжиДжи из  “Ведьмина служба доставки”",
                "user": "kashikad",
                "price": 500,
            },
            {
                "image": "deps/assets/cat_cup.webp",
                "title": "Кружка “CAT CAT CAT”",
                "user": "catslover",
                "price": 900,
            },
            {
                "image": "deps/assets/rabbit_nippon.webp",
                "title": "Nippon кролик с открыткой стикер",
                "user": "sfiaaadf",
                "price": 150,
            },
            {
                "image": "deps/assets/flowers_bag.webp",
                "title": "Сумка шопер цветочный",
                "user": "nikaqqpppp",
                "price": 1100,
            },
            {
                "image": "deps/assets/tshirt.webp",
                "title": "Футболка Surprised Oswald Essential",
                "user": "1osdk",
                "price": 2000,
            },
            {
                "image": "deps/assets/blueberry_postcard.webp",
                "title": "Открытка “Черника”",
                "user": "bbb81",
                "price": 50,
            },
            {
                "image": "deps/assets/frogs_cup.webp",
                "title": "Стикер “Чашка с лягушками”",
                "user": "Narinaa",
                "price": 200,
            },
        ]
    }
    return render(request, 'goods/catalog.html', context)

def product(request):
    return render(request, 'goods/product.html')