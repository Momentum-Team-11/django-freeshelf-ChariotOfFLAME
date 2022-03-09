from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.text import slugify

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(max_length=2000)
    url = models.URLField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    categories = models.ManyToManyField("Category", related_name="book", blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=75)
    slug = models.SlugField(max_length=75, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"<Category name={self.name}>"
    
    def save(self):
        self.slug = slugify(self.name)
        super().save()
