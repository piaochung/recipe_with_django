from django.contrib import admin
from .models import Food, FoodGallery, FoodRecipe

# Register your models here.
class FoodGalleryInline(admin.TabularInline):
    model = FoodGallery
    extra = 1


class FoodRecipeInline(admin.TabularInline):
    model = FoodRecipe
    extra = 1


class FoodAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'category', 'description', 'created_at', 'updated_at', 'active')
    prepopulated_fields = {'slug': ('food_name',)}
    inlines = [FoodGalleryInline, FoodRecipeInline]


class FoodRecipeAdmin(admin.ModelAdmin):
    list_display = ('order', 'get_food_name', 'description')

admin.site.register(Food, FoodAdmin)
admin.site.register(FoodGallery)
admin.site.register(FoodRecipe, FoodRecipeAdmin)