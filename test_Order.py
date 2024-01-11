from unittest import TestCase

import MenuItems
from Order import Order
from MenuItems import Candy, Cookies, IceCream, Sundae, SundaeToppings, IceCreamConeType, IceCreamFlavors


class TestOrder(TestCase):
    def test_calculate_total_and_tax_candy(self):
        order = Order()
        order.add_item(Candy(0.35))
        self.assertEqual((1.66, 0.10), order.calculate_total_and_tax(),
                         "Test Order: calculate total: candy")

    def test_calculate_total_and_tax_candy_cookies_candy(self):
        order = Order()
        order.add_item(Candy(0.35))
        order.add_item(Cookies(2))
        order.add_item(Candy(0.78))
        self.assertEqual((17.87, 1.11), order.calculate_total_and_tax(),
                         "Test Order: calculate total: candy, cookies, candy")

    def test_calculate_total_and_tax_ice_cream_sundae(self):
        order = Order()
        order.add_item(IceCream(3, IceCreamFlavors.Vanilla, IceCreamConeType.Cone))
        sundae = Sundae()
        sundae.add_topping(SundaeToppings.Hot_Fudge)
        sundae.add_topping(SundaeToppings.Peanuts)
        order.add_item(sundae)
        val = order.calculate_total_and_tax()
        self.assertEqual((10.10, 0.71), val,
                         "Test Order: calculate total: ice cream, Sunday")

    def test_calculate_cost_tax_no_items(self):
        order = Order()
        self.assertEqual((0, 0), order.calculate_total_and_tax(),
                         "Test Order: calculate tax: no items")

    def test_calculate_cost_and_tax_with_candy_and_ice_cream(self):
        order = Order()
        order.add_item(Candy(.25))
        order.add_item(IceCream(2, IceCreamFlavors.Vanilla, IceCreamConeType.Cone))
        order.add_item(IceCream(1, IceCreamFlavors.Vanilla, IceCreamConeType.Cone))
        order.add_item((IceCream(3, IceCreamFlavors.Vanilla, IceCreamConeType.Cone)))
        self.assertEqual((11.39, 0.79), order.calculate_total_and_tax(),
                         "Test Order: calc cost and tax with items")

    def test_calculate_total_and_tax_with_candy_cookies_ice_cream(self):
        order = Order()
        order.add_item(Candy(0.45))
        order.add_item(Cookies(1))
        order.add_item(Candy(0.5))
        order.add_item(IceCream(2, IceCreamFlavors.Vanilla, IceCreamConeType.Cone))
        order.add_item(Candy(.31))
        order.add_item(Cookies(2))
        order.add_item(IceCream(1, IceCreamFlavors.Vanilla, IceCreamConeType.Cone))
        order.add_item(Candy(0.25))
        order.add_item((IceCream(3, IceCreamFlavors.Vanilla, IceCreamConeType.Cone)))
        self.assertEqual((36.13, 2.33), order.calculate_total_and_tax())

    def test_get_menu_items(self):
        order = Order()
        order.add_item(Candy(.45))
        order.add_item(Cookies(1))
        order.add_item(Candy(.5))
        order.add_item(IceCream(2, IceCreamFlavors.Vanilla, IceCreamConeType.Cone))
        order.add_item(Candy(.31))
        order.add_item(Cookies(2))
        order.add_item(IceCream(1, IceCreamFlavors.Vanilla, IceCreamConeType.Cone))
        order.add_item(Candy(.25))
        order.add_item((IceCream(3, IceCreamFlavors.Vanilla, IceCreamConeType.Cone)))
        ordered_items = order.get_items()
        self.assertTrue(isinstance(ordered_items[0], MenuItems.Candy))
        self.assertTrue(isinstance(ordered_items[3], MenuItems.Candy))
        self.assertTrue(isinstance(ordered_items[4], MenuItems.Cookies))
        self.assertTrue(isinstance(ordered_items[6], MenuItems.IceCream))
        self.assertTrue(isinstance(ordered_items[8], MenuItems.IceCream))
