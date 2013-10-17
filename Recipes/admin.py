__author__ = 'orjan'

from django.contrib import admin
from Recipes.models import Recipe, Ingredient, RecipeCategory


class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']
    filter_horizontal = ['ingredients']
    inlines = [IngredientInline]

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == 'ingredients':
            kwargs['queryset'] = Ingredient.objects.all()
        return super(RecipeAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeCategory)