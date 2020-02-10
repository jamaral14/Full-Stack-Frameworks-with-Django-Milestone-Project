from django.conf.urls import url
from .views import view_cart, add_to_cart, adjust_cart

urlpatterns = [
    url(r'^$', view_cart, name='view_cart'), # The regex will just be the view the cart, and everthing within.
    url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'), # This allowed a numeber/ID and adding a cart.
    url(r'^adjust/(?P<id>\d+)', adjust_cart, name='adjust_cart'), # Adjust the quantities within a cart.
]