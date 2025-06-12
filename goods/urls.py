from django.urls import path

from goods import views

app_name = 'goods'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('search/', views.catalog, name='search'),
    path('product/<slug:product_slug>/', views.product, name='product'),
    path('product/<slug:product_slug>/toggle-favorite/', views.toggle_favorite, name='toggle_favorite'),

]
