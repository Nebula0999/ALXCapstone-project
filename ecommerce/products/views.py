from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Cart, CartItem, Product
from rest_framework.serializers import ModelSerializer
from api.serializers import ProductSerializer

class ProductListView(APIView):
    #Returns the view of products
    def get(self, request):
        products = Product.objects.all()
        category = request.query_params.get('category', None)
        search = request.query_params.get('search', None)
        if category:
            products = products.filter(category__icontains=category)
        if search:
            products = products.filter(name__icontains=search)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddToCartView(APIView):
    def post(self, request, user_id):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        cart, _ = Cart.objects.get_or_create(user_id=user_id)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity

        cart_item.save()
        return Response({"message": "Product added to cart"}, status=status.HTTP_201_CREATED)

# Create your views here.
