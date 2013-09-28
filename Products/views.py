# Create your views here.
from django.views import generic
from Products.models import Product, ProductType, Producer


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


class ProductTypeIndexView(generic.ListView):
    template_name = 'product_type_index.html'
    context_object_name = 'product_type_list'

    def get_queryset(self):
        return ProductType.objects.order_by('name')


class ProductTypeDetailView(generic.DetailView):
    model = ProductType
    template_name = 'product_type_detail.html'
