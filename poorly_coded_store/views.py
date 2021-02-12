from django.shortcuts import render, redirect
from .models import Order, Product

global_total = 0
quantity = 0
total_charge = 0


def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def render_checkout(request):
    global total_charge
    global global_total
    global quantity
    context = {
        "total": total_charge,
        "quantity": quantity,
        "global_total": global_total,
    }
    return render(request, "store/checkout.html", context)


def checkout(request):
    global total_charge
    global global_total
    global quantity

    quantity_from_form = int(request.POST["quantity"])
    product = Product.objects.get(id=request.POST["product_id"])
    price_from_form = float(product.price)

    total_charge = quantity_from_form * price_from_form
    global_total += total_charge
    quantity += quantity_from_form
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)

    return redirect("/checkout")