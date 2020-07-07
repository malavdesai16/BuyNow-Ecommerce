from django.urls import path
from .views import (
<<<<<<< HEAD
    ItemDetailView,
    checkout,
    HomeView
    # add_to_cart,
    # remove_from_cart
=======
    products,
    checkout,
    home
>>>>>>> e8995eda040034fa45d51e1774f450c1fd96d922
)

app_name = 'core'

urlpatterns = [
<<<<<<< HEAD
    path('', HomeView.as_view(), name='home'),
    path('checkout/', checkout, name='checkout'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product')
    # path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    # path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart')
=======
    path('', home, name='home'),
    path('checkout/', checkout, name='checkout'),
    path('products/', products, name='products')
>>>>>>> e8995eda040034fa45d51e1774f450c1fd96d922
]
