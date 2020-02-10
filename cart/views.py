from django.shortcuts import render

# Create your views here.
def view_cart(request): # View that renders the cart contents page
    return render(request, "cart.html")

def add_to_cart(request, id): # Add a quantity of wine product to the cart
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('index')) 

