from django.urls import path
from .views import Listproduct, CartList, CartCreateView

urlpatterns = [
    path('product/', Listproduct.as_view()),
    path('cart/', CartList.as_view()),
    path('cart/add_product/', CartCreateView.as_view()),
]
