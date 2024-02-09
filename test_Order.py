from unittest import TestCase

import MenuItems
from Order import Order
from MenuItems import Candy, Cookies, IceCream, IceCreamFlavors, IceCreamConeType, Sundae, SundaeToppings


class TestOrder(TestCase):
    def test_calculate_total_candy(self):
        order = Order()
        order.add_item(Candy(0.35))
        self.assertEqual((1.66, 0.05), order.get_total_and_tax(),
                         "Test Order: calculate total: candy")

    def test_calculate_total_candy_cookies_candy(self):
        order = Order()
        order.add_item(Candy(0.35))
        order.add_item(Cookies(2))
        order.add_item(Candy(0.78))
        self.assertEqual((17.87, 0.54), order.get_total_and_tax(),
                         "Test Order: calculate total: candy, cookies, candy")

    def test_calculate_total_ice_cream_sundae(self):
        order = Order()
        order.add_item(IceCream(3, IceCreamFlavors.Vanilla, IceCreamConeType.Cone))
        sundae = Sundae()
        sundae.add_topping(SundaeToppings.Hot_Fudge)
        sundae.add_topping(SundaeToppings.Peanuts)
        order.add_item(sundae)
        val, tax = order.get_total_and_tax()
        self.assertEqual((10.10, 0.76), (val, tax),
                         "Test Order: calculate total: ice cream, Sunday")

    def test_calculate_cost_no_items(self):
        order = Order()
        self.assertEqual((0, 0), order.get_total_and_tax(),
                         "Test Order: calculate no items")

    def test_calculate_cost_with_candy_and_ice_cream(self):
        order = Order()
        order.add_item(Candy(.25))
        order.add_item(IceCream(2, IceCreamFlavors.Chocolate, IceCreamConeType.Cone))
        order.add_item(IceCream(1, IceCreamFlavors.Strawberry, IceCreamConeType.Cone))
        order.add_item((IceCream(3, IceCreamFlavors.Huckleberry, IceCreamConeType.Cone)))
        self.assertEqual((11.39, 0.81), order.get_total_and_tax(),
                         "Test Order: calc cost with items")

    def test_calculate_total_with_candy_cookies_ice_cream(self):
        order = Order()
        order.add_item(Candy(0.45))
        order.add_item(Cookies(1))
        order.add_item(Candy(0.5))
        order.add_item(IceCream(2, IceCreamFlavors.Vanilla, IceCreamConeType.Waffle_Cone))
        order.add_item(Candy(.31))
        order.add_item(Cookies(2))
        order.add_item(IceCream(1, IceCreamFlavors.Vanilla, IceCreamConeType.Cone))
        order.add_item(Candy(0.25))
        order.add_item((IceCream(3, IceCreamFlavors.Huckleberry, IceCreamConeType.Waffle_Cone)))
        self.assertEqual((36.13, 1.55), order.get_total_and_tax())

    def test_get_menu_items(self):
        order = Order()
        order.add_item(Candy(.45))
        order.add_item(Cookies(1))
        order.add_item(Candy(.5))
        order.add_item(IceCream(2, IceCreamFlavors.Vanilla, IceCreamConeType.Cone))
        order.add_item(Candy(.31))
        order.add_item(Cookies(2))
        order.add_item(IceCream(1, IceCreamFlavors.Chocolate, IceCreamConeType.Cone))
        order.add_item(Candy(.25))
        order.add_item((IceCream(3, IceCreamFlavors.Strawberry, IceCreamConeType.Cone)))
        ordered_items = order.get_items()
        self.assertTrue(isinstance(ordered_items[0], MenuItems.Candy))
        self.assertTrue(isinstance(ordered_items[3], MenuItems.Candy))
        self.assertTrue(isinstance(ordered_items[4], MenuItems.Cookies))
        self.assertTrue(isinstance(ordered_items[6], MenuItems.IceCream))
        self.assertTrue(isinstance(ordered_items[8], MenuItems.IceCream))
