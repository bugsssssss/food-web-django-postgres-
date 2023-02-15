from django.urls import path, include

from mainapp.views import HomeView, food_by_category


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<int:category_id>', food_by_category, name='food_by_category')
]
