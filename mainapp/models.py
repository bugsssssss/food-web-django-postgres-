import imp
from pyexpat import model
from unicodedata import category
from django.db import models
from django.urls import reverse, reverse_lazy
# from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Cover(models.Model):
    image = models.ImageField(("image"), upload_to='covers')
    is_active = models.BooleanField(("is_active"))

    class Meta:
        verbose_name = 'Cover'
        verbose_name_plural = 'Covers'

    def __str__(self):
        return f'{self.id}: {self.is_active}'


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


class FoodModel(models.Model):
    name = models.CharField(("name"), max_length=50)
    picture = models.ImageField(("picture"), upload_to='food-models')
    about = models.TextField(("about"))
    price = models.IntegerField(("Price"))
    category = models.ForeignKey(Category, verbose_name=(
        "category"), on_delete=models.PROTECT)
    quantity = models.IntegerField(("quantiy"))

    def __str__(self):
        return self.name


    # def get_absolute_url(self):
    #     return reverse("Foodmodel_detail", kwargs={"pk": self.pk})




# class FoodModel(models.Model):
#     name = models.CharField(("name"), max_length=50)
#     picture = models.ImageField(("picture"), upload_to='food-models')
#     about = models.TextField(("about"))
#     price = models.IntegerField(("Price"))
#     category = models.ForeignKey(Category, verbose_name=(
#         "category"), on_delete=models.PROTECT)

#     def __str__(self):
#         return self.name




class Callback(models.Model):

    name = models.CharField(("name"), max_length=100)
    # phone = PhoneNumberField(("phone"))
    phone = models.CharField(("phone"), max_length=100)
    message = models.TextField(("message"))    

    class Meta:
        verbose_name = ("Callback")
        verbose_name_plural = ("Callbacks")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Callback_detail", kwargs={"pk": self.pk})




# class Basket(models.Model):

#     summary = models.IntegerField(("summary"))


#     class Meta:
#         verbose_name = ("Basket")
#         verbose_name_plural = ("Baskets")

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("Basket_detail", kwargs={"pk": self.pk})
