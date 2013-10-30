from Cart.views import get_cart_widget, update_cart, add_to_cart
from django.conf import settings
from django.conf.urls import patterns, include, url
from Order.views import handle_order_form

from Products.views import ProductDetailView, ProductIndexView, ProductCategoryIndexView, \
    ProducerIndexView, ProducerDetailView, product_category, get_product_sidebar_rendered
from Misc.views import FrontPageView, BasePageView, AboutPageView, FooterPageView, FaqPageView
from Recipes.views import RecipeDetailView, get_recipe_sidebar_rendered, recipe_category, buy_recipe_modal

# Uncomment the next two lines to enable the admin:
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',

    # MISC
    url(r'^$', BasePageView.as_view(), name='basepage'),
    url(r'^frontpage/', FrontPageView.as_view(), name='frontpage'),
    url(r'^about/', AboutPageView.as_view(), name='about'),
    url(r'^footer/', FooterPageView.as_view(), name='footer'),
    url(r'^faq/', FaqPageView.as_view(), name='faq'),

    # PRODUCT
    url(r'^product/$', ProductIndexView.as_view(), name='product_list'),
    url(r'^product/(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail'),

    # CART
    url(r'^cart/widget/$', get_cart_widget, name='cart_widget'),
    url(r'cart/add/$', add_to_cart, name='cart_add'),
    url(r'cart/update/$', update_cart, name='cart_update'),

    # PRODUCER
    url(r'^producer/$', ProducerIndexView.as_view(), name='producer_list'),
    url(r'^producer/(?P<pk>\d+)/$', ProducerDetailView.as_view(), name='producer_detail'),

    # PRODUCT_CATEGORY
    url(r'^product-category/$', ProductCategoryIndexView.as_view(), name='product_category_list'),
    url(r'^product-category/(?P<pk>\d+)/$', product_category, name='product_category_detail'),
    url(r'^product-category-sidebar/$', get_product_sidebar_rendered, name='product_category_sidebar'),
    #url(r'^product-category/(?P<pk>\d+)/$', ProductCategoryDetailView.as_view(), name='product_category_detail'),

    # RECIPE
    url(r'^recipe/(?P<pk>\d+)/$', RecipeDetailView.as_view(), name='recipe_detail'),
    url(r'^buy-recipe-modal/(?P<pk>\d+)/(?P<servings>\d+)/$', buy_recipe_modal, name='buy_recipe_modal'),

    # RECIPE_CATEGORY
    url(r'^recipe-category-sidebar/$', get_recipe_sidebar_rendered, name='recipe_category_sidebar'),
    url(r'^recipe-category/(?P<pk>\d+)/$', recipe_category, name='recipe_category_detail'),

    url(r'^order/$', handle_order_form, name='handle_order_form'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)