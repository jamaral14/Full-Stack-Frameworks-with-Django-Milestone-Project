""" Create urls.py within the products app,
 which will then be linked to in the top-level URLs in ecommerce """
from django.conf.urls import url, include
from .views import all_products

urlpatterns = [
    url(r'^$', all_products, name='products'),
]