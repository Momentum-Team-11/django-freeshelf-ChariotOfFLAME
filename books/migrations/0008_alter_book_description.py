# Generated by Django 4.0.3 on 2022-03-08 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_alter_book_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(max_length=2000),
        ),
    ]
