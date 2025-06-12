from pyexpat import model
from unicodedata import category
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")

    class Meta:
        db_table: str = 'category'
        verbose_name: str = 'Категория'
        verbose_name_plural: str = 'Категории'

    def __str__(self):
        return self.name

class Tags(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Название")

    class Meta:
        db_table: str = 'tag'
        verbose_name: str = 'Тэг'
        verbose_name_plural: str = 'Тэги'

    def __str__(self):
        return self.name

class Products(models.Model):
    title = models.CharField(max_length=150, unique=False, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name="Изображение")
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name="Цена")
    category = models.ForeignKey(to=Categories, on_delete=models.PROTECT, verbose_name="Категория")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")
    is_available = models.BooleanField(default=True, verbose_name="В наличии")
    tags = models.ManyToManyField(Tags, blank=True, verbose_name="Тэги")

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Пользователь',
        null=True,  # временно разрешаем пустые значения
        blank=True
    )

    class Meta:
        db_table: str = 'product'
        verbose_name: str = 'Продукт'
        verbose_name_plural: str = 'Продукты'
        ordering = ("id",)

    def __str__(self):
        return self.title

class Favorite(models.Model):
    user = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE, 
        related_name='favorites', 
        verbose_name='Пользователь',
        null=True,  # временно разрешаем пустые значения
        blank=True
    )
    product = models.ForeignKey(
        Products, 
        on_delete=models.CASCADE, 
        related_name='favorited_by', 
        verbose_name='Продукт',
        null=True,  # временно разрешаем пустые значения
        blank=True
    )
    added_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Дата добавления')

    class Meta:
        db_table = 'favorite'
        unique_together = ('user', 'product')
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные товары'

    def __str__(self):
        return f"{self.user.username} → {self.product.title}"