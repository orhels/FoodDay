# Create your views here.
from django.views import generic
from Products.models import Product


class ProductIndexView(generic.ListView):
    template_name = "products/index.html"
    context_object_name = "product_list"

    def get_queryset(self):
        return Product.objects.order_by('pk')


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "products/detail.html"