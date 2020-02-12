from django.shortcuts import render

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET

@login_required()