from django.conf.urls import patterns, include, url

from Products.views import ProductDetailView, ProductIndexView, ProductTypeDetailView, ProductTypeIndexView, \
    ProducerIndexView, ProducerDetailView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FoodDay.views.home', name='home'),
    # url(r'^FoodDay/', include('FoodDay.foo.urls')),

    # PRODUCT
    url(r'^product/$', ProductIndexView.as_view(), name='product_list'),
    url(r'^product/(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail'),

    # PRODUCER
    url(r'^producer/$', ProducerIndexView.as_view(), name='producer_list'),
    url(r'^producer/(?P<pk>\d+)/$', ProducerDetailView.as_view(), name='producer_detail'),

    # PRODUCT_TYPE
    url(r'^productType/$', ProductTypeIndexView.as_view(), name='product_type_list'),
    url(r'^productType/(?P<pk>\d+)/$', ProductTypeDetailView.as_view(), name='product_type_detail'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)

urlpatterns += staticfiles_urlpatterns()
