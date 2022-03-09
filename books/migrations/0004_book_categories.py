# Generated by Django 4.0.3 on 2022-03-08 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(related_name='book', to='books.category'),
        ),
    ]