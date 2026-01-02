from django.test import TestCase
from restaurant.models import Menu  # Remplacé MenuItem par Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Création de quelques objets de test
        Menu.objects.create(title="Pizza", price=50, inventory=20)
        Menu.objects.create(title="Burger", price=40, inventory=30)

    def test_get_all(self):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(len(serializer.data), 2)
        self.assertEqual(serializer.data[0]['title'], "Pizza")
        self.assertEqual(serializer.data[1]['title'], "Burger")
