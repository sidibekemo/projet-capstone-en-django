from rest_framework import generics,viewsets
from .models import Menu,Booking  # Menu ou MenuItem selon ton modèle
from .serializers import MenuSerializer,BookingSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
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
    permission_classes = [IsAuthenticated]  # seuls les utilisateurs authentifiés peuvent accéder

class MenuItemsView(generics.ListCreateAPIView):
     permission_classes = [IsAuthenticated]
     queryset = Menu.objects.all()
     serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def message(request):
    return Response({"message": "Cette vue est protégée par token"})

