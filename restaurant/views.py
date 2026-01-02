from rest_framework import generics,viewsets
from .models import Menu,Booking  # Menu ou MenuItem selon ton modèle
from .serializers import MenuSerializer,BookingSerializer
# Liste et création d'éléments du menu
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# Détail, mise à jour et suppression d'un élément de menu
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()       # Récupère toutes les réservations
    serializer_class = BookingSerializer   # Sérialiseur associé