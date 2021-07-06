from django.urls import path
from . import views

urlpatterns = [
    path('', views.foods, name='foods'),
    path('food_detail/<slug:category_slug>/', views.food_category, name='food_category'),
    path('food_detail/<slug:category_slug>/<slug:food_slug>/', views.food_detail, name='food_detail'),
]
