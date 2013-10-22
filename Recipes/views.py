# Create your views here.
from django.shortcuts import render_to_response
from django.views import generic
from Products.models import Product
from Recipes.models import Recipe, RecipeCategory


class RecipeDetailView(generic.DetailView):
    model = Recipe
    template_name = "recipe_detail.html"


def get_recipe_sidebar_rendered(request):
    recipe_category_list = RecipeCategory.objects.filter(parents=None).all()
    return render_to_response('recipe_category_sidebar.html', {'recipe_category_list' : recipe_category_list})


def recipe_category(request, **kwargs):
    recipecategory = RecipeCategory.objects.get(pk=kwargs['pk'])
    return render_to_response('recipe_category_detail.html', {'recipecategory': recipecategory})


def buy_recipe_modal(request, **kwargs):
    recipe = Recipe.objects.get(pk=kwargs['pk'])
    products_to_get = recipe.get_products_for_cart(int(kwargs['servings']))
    product_list = []
    for k, v in products_to_get.iteritems():
        print k
        product_list.append((Product.objects.get(pk=k), v))
    print product_list
    return render_to_response('buy_recipe_modal.html', {'recipe': recipe, 'product_list': product_list})