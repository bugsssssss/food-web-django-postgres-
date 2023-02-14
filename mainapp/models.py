import imp
from pyexpat import model
from unicodedata import category
from django.db import models
from django.urls import reverse, reverse_lazy

# Create your models here.


class Cover(models.Model):
    image = models.ImageField(("image"), upload_to='covers')
    is_active = models.BooleanField(("is_active"))

    class Meta:
        verbose_name = 'Cover'
        verbose_name_plural = 'Covers'


class Category(models.Model):

    category = models.CharField(("category"), max_length=100)
    picture = models.ImageField(
        ("picture"), upload_to='categories')

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
        ordering = ['-category']

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})
