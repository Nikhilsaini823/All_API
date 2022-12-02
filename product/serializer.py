from rest_framework import serializers
from product.models import Product, Cart


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'description',
            'price',
            'weight',
            'image',
        )


class CartListSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='owner.username')
    # cart_product = ProductSerializer(source='product')
    product = ProductSerializer()

    class Meta:
        model = Cart
        fields = (
            'id',
            'product',
            'quantity',
            'price',
            'user'
        )


class CartCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Cart
        fields = (
            'id',
            'product',
            'quantity',
            'price',
            'user'
        )
