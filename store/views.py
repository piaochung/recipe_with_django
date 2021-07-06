from django.shortcuts import render

from django.db.models import Q
from .models import Food, FoodRecipe, FoodGallery


# Create your views here.
def foods(request):
    foods = Food.objects.filter(is_active=True)

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


def food_category(request, category_slug):
    try:
        cat_foods = Food.objects.order_by('-created_at').filter(Q(food_name__icontains=category_slug) | 
        Q(category__slug__icontains=category_slug) & Q(is_active=True))
        food_count = cat_foods.count()
    except Exception as e:
        raise e
    
    context = {
        'cat_foods': cat_foods,
        'food_count': food_count,
    }
    return render(request, 'search.html', context)
