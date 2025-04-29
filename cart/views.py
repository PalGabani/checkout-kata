from django.shortcuts import render
from .checkout import Checkout

def calculate_checkout(request):
    total = None
    items = ''
    if request.method == 'POST':
        items = request.POST.get('items', '').upper()
        checkout = Checkout(items)
        total = checkout.total()
    return render(request, 'cart/checkout.html', {'total': total, 'items': items})

