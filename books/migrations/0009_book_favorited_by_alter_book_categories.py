# Generated by Django 4.0.3 on 2022-03-09 15:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_alter_book_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='favorited_by',
            field=models.ManyToManyField(related_name='favorite_books', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='books', to='books.category'),
        ),
    ]