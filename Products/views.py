# Create your views here.
from django.shortcuts import render_to_response
from django.template import Context
from django.template.loader import get_template
from django.views import generic
from Products.models import Product, ProductCategory, Producer


class ProductIndexView(generic.ListView):
    template_name = 'product_index.html'
    context_object_name = "product_list"

    def get_queryset(self):
        return Product.objects.order_by('pk')


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'product_detail.html'


class ProducerIndexView(generic.ListView):
    template_name = 'producer_index.html'
    context_object_name = "producer_list"

    def get_queryset(self):
        return Producer.objects.order_by('name')


class ProducerDetailView(generic.DetailView):
    model = Producer
    template_name = 'producer_detail.html'


class ProductCategoryIndexView(generic.ListView):
    template_name = 'product_category_index.html'
    context_object_name = 'product_category_list'

    def get_queryset(self):
        return ProductCategory.objects.order_by('name')


class ProductCategoryDetailView(generic.DetailView):
    model = ProductCategory
    template_name = 'product_category_detail.html'


def get_product_sidebar_rendered(request):
    product_category_list = ProductCategory.objects.filter(parents=None).all()
    return render_to_response('product_category_sidebar.html', {'product_category_list': product_category_list})


def product_category(request, **kwargs):
    productcategory = ProductCategory.objects.get(pk=kwargs['pk'])
    return render_to_response('product_category_detail.html', {'productcategory' : productcategory})