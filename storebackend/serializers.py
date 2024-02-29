from rest_framework import serializers

from storebackend.models import Category, Product, User, ConfirmEmailToken, Contact, Shop, Order, OrderItem


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'user', 'city', 'street', 'house', 'structure', 'building', 'apartment', 'phone']
        read_only_fields = ['id']


class UserSerializer(serializers.ModelSerializer):
    contact_data = ContactSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'company', 'position', 'username', 'type', 'contact_data']
        read_only_fields = ['id']


class ConfirmEmailTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfirmEmailToken
        fields = ['id', 'created_at', 'key', 'user_id']
        read_only_fields = ['id']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'shops']
        read_only_fields = ['id']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'category']
        read_only_fields = ['id']


class SupplierRetrieveUpdateSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(read_only=True)

    class Meta:
        model = Shop
        fields = ['id', 'name', 'url', 'user_data', 'state']
        read_only_fields = ['id', 'name', 'url', 'user_data']


class OrderSerializer(serializers.ModelSerializer):
    contact = ContactSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'dt', 'state', 'contact']
        read_only_fields = ['id']
