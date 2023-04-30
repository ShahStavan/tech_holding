from rest_framework import serializers
from .models import order

class OrderSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    order_id = serializers.CharField(max_length=100)
    pname = serializers.CharField(max_length=100)
    product_id = serializers.CharField(max_length=100)

    class Meta:
        model = order
        fields = ['id', 'order_id', 'pname', 'product_id']

def create(self, validated_data):
    return order.objects.create(**validated_data)

