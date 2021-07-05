from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Food, FoodRecipe, FoodGallery


# Create your views here.
def foods(request):
    foods = Food.objects.filter(active=True)

    context = {
        'foods': foods
    }
    return render(request, 'food.html', context)

def food_detail(request, category_slug, food_slug):
    try:
        single_food = Food.objects.get(category__slug=category_slug, slug=food_slug)
    except Exception as e:
        raise e

    food_gallery = FoodGallery.objects.filter(food_id=single_food.id)
    food_recipe = FoodRecipe.objects.filter(food_id=single_food.id)

    context = {
        'food_gallery': food_gallery,
        'food_recipe': food_recipe,
    }
    return render(request, 'food_detail.html', context)