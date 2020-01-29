from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_cart(request):
    """Render all the content in the cart"""
    return render(request, 'cart.html')

def add_to_cart(request, id):
    """add a quantity of the specified product to the cart"""
    quantity=int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart

    return redirect(reverse('index'))


def adjust_cart(request, id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    request.session['cart'] = cart    

    return redirect(reverse('cart_view'))
        
