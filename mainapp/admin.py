from django.contrib import admin

from mainapp.models import *
# Register your models here.


class FoodAdmin(admin.ModelAdmin):
    list_display = ('pk','name', 'price', 'category')

@admin.register(Callback)
class CallbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ( 'pk','category')
    


admin.site.register(Cover)
# admin.site.register(Category)
admin.site.register(FoodModel, FoodAdmin)
