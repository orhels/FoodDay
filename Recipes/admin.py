__author__ = 'orjan'

from django.contrib import admin
from Recipes.models import Recipe, Ingredient, RecipeCategory


class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']
    inlines = [IngredientInline]

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        #if db_field.name == 'ingredients':
        #    kwargs['queryset'] = Ingredient.objects.all()
        if db_field.name == 'recipe_categories':
            kwargs['queryset'] = RecipeCategory.objects.filter(children=None)
        return super(RecipeAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)


class RecipeCategoryAdmin(admin.ModelAdmin):
    filter_horizontal = ['parents']


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeCategory, RecipeCategoryAdmin)