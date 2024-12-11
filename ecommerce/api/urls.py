from django.urls import path
from .serializers import ProductSerializer
from products.views import ProductListView, AddToCartView
from users.views import LoginView
urlpatterns = [
    path('api/', ProductSerializer),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/products/', ProductListView.as_view(), name='product-list'),
    path('api/carts/<int:user_id>/items/', AddToCartView.as_view(), name='add-to-cart'),
]