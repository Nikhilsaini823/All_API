from django.shortcuts import render
from rest_framework import generics
from product.serializer import ProductSerializer, CartCreateSerializer, CartListSerializer
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from snippets.permissions import IsOwnerOrReadOnly
from product.models import Product, Cart


class Listproduct(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter()


class CartCreateView(generics.CreateAPIView):
    serializer_class = CartCreateSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CartList(generics.ListAPIView):
    serializer_class = CartListSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user.id)
