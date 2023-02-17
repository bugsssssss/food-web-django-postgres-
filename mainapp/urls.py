from django.urls import path, include

from mainapp.views import  *


urlpatterns = [
    path('', HomeCreateView.as_view(), name='home'),
    path('category/<int:pk>', FoodDetailView.as_view(), name='detail')
]
