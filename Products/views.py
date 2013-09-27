# Create your views here.
from django.views import generic
from Products.models import Product, ProductType


class ProductIndexView(generic.ListView):
    template_name = "products/product_index.html"
    context_object_name = "product_list"

    def get_queryset(self):
        return Product.objects.order_by('pk')


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "products/product_detail.html"


class ProductTypeIndexView(generic.ListView):
    template_name = "products/product_type_index.html"
    context_object_name = 'product_type_list'

    def get_queryset(self):
        return ProductType.objects.order_by('name')


class ProductTypeDetailView(generic.DetailView):
    model = ProductType
    template_name = "products/product_type_detail.html"
