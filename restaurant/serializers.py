from rest_framework import serializers
from .models import Menu,Booking  # ou MenuItem si tu as nommé ton modèle ainsi

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu  # Remplace par MenuItem si nécessaire
        fields = ['id', 'title', 'price', 'inventory']  # Ajuste les champs selon ton modèle


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'  # Tous les champs du modèle Booking seront exposés