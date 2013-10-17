# Create your views here.
from django.shortcuts import render_to_response
from django.views import generic
from Recipes.models import Recipe, RecipeCategory


class RecipeDetailView(generic.DetailView):
    model = Recipe
    template_name = "recipe_detail.html"


def get_recipe_sidebar_rendered(request):
    recipe_category_list = RecipeCategory.objects.all()
    return render_to_response('recipe_category_sidebar.html', {'recipe_category_list' : recipe_category_list})


def recipe_category(request, **kwargs):
    recipecategory = RecipeCategory.objects.get(pk=kwargs['pk'])
    return render_to_response('recipe_category_detail.html', {'recipecategory': recipecategory})