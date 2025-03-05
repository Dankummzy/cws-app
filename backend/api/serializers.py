from rest_framework import serializers

class ConversionSerializer(serializers.Serializer):
    base_currency = serializers.CharField(max_length=3)
    target_currency = serializers.CharField(max_length=3)
    amount = serializers.FloatField()

class WeatherSerializer(serializers.Serializer):
    city = serializers.CharField(max_length=255)

class StockSerializer(serializers.Serializer):
    symbol = serializers.CharField(max_length=10)
