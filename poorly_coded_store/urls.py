from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('checkout', views.render_checkout),
    path('checkout/payment', views.checkout)
]
