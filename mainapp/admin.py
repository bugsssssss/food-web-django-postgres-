from django.contrib import admin

from mainapp.models import *
# Register your models here.


class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')


admin.site.register(Cover)
admin.site.register(Category)
admin.site.register(FoodModel, FoodAdmin)
