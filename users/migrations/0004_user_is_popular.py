# Generated by Django 4.2.21 on 2025-06-12 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_popular',
            field=models.BooleanField(default=False),
        ),
    ]
