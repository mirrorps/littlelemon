from django.test import TestCase
from django.urls import reverse
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setup():
        Menu(name='Name1',price='1').save()
        Menu(name='Name2',price='2').save()
        Menu(name='Name3',price='3').save()
        
    def test_getall(self):
        menus = Menu.objects.all()
        response = self.client.get(reverse("menu"))
        self.assertEqual(response.status_code, 200)
        
        # self.assertQuerySetEqual(
        #     response.context["menu"],
        #     menus,
        # )
        