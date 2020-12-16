from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    chart = request.session.get('chart', {})
    if not chart:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'STRIPE_PUBLIC_KEY',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
