from typing import ContextManager
from django.shortcuts import render

from categories.models import Category

# Create your views here.
def home(request):
    categories = Category.objects.filter(is_active=True)

    context = {
        'categories':categories
    }
    return render(request, 'home.html', context)
