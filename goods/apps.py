from typing import Literal
from django.apps import AppConfig


class GoodsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'goods'
    verbose_name: Literal[''] = 'Товары'
