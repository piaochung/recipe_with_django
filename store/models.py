from django.db import models
from django.db.models.fields import NOT_PROVIDED
from categories.models import Category

# Create your models here.
class Food(models.Model):
    food_name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    kcal = models.FloatField()
    fat = models.FloatField()
    saturates = models.FloatField()
    carbs = models.FloatField()
    sugars = models.FloatField()
    fibre = models.FloatField()
    protein = models.FloatField()
    salt = models.FloatField()

    def __str__(self):
        return self.food_name


class FoodRecipe(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    description = models.TextField(max_length=300)

    def __str__(self):
        return f'{self.order} | {self.food.food_name}'

    def get_food_name(self):
        return self.food.food_name



class FoodGallery(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=f'media/foods', max_length=255)


    def __str__(self):
        return self.food.food_name