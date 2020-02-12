from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import MakePaymentForm, OrderForm
from django.conf import settings
import stripe


# Create your views here.

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)