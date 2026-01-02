from django.test import TestCase
from restaurant.models import Menu  # Remplacé MenuItem par Menu

class MenuTest(TestCase):
    def test_get_item(self):
        # Création d'une instance de test
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        # Vérification de la représentation en chaîne
        self.assertEqual(str(item), "IceCream : 80")
