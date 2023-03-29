from unittest import TestCase

import MenuItems
from Order import Order
from MenuItems import Candy, Cookies, IceCream, Sundae
from money.money import Money


class TestOrder(TestCase):
    def test_calculate_total_no_items(self):
        order = Order()
        self.assertEqual(Money('0'), order.calculate_total(), "Test Order: calculate total: no items")

    def test_calculate_total_candy(self):
        order = Order()
        order.add_item(Candy(0.35))
        val = order.calculate_total()
        self.assertEqual(Money('1.66'), val, "Test Order: calculate total: candy")

    def test_calculate_total_candy_cookies(self):
        order = Order()
        order.add_item(Candy(0.35))
        order.add_item(Cookies(2))
        val = order.calculate_total()
        self.assertEqual(Money('14.16'), val, "Test Order: calculate total: candy, cookies")

    def test_calculate_total_candy_cookies_candy(self):
        order = Order()
        order.add_item(Candy(0.35))
        order.add_item(Cookies(2))
        order.add_item(Candy(0.78))
        val = order.calculate_total()
        self.assertEqual(Money('17.87'), val, "Test Order: calculate total: candy, cookies, candy")

    def test_calculate_total_IceCream_Sundae(self):
        order = Order()
        order.add_item(IceCream(3))
        sundae = Sundae()
        sundae.add_topping(Sundae.HotFudge)
        sundae.add_topping(Sundae.Peanuts)
        order.add_item(sundae)
        val = order.calculate_total()
        self.assertEqual(Money('10.10'), val, "Test Order: calculate total: ice cream, Sunday")

    def test_calculate_tax_no_items(self):
        order = Order()
        self.assertEqual(Money('0'), order.calculate_tax(), "Test Order: calculate tax: no items")

    def test_calculate_tax_with_items(self):
        order = Order()
        order.add_item(Candy(.25))
        order.add_item(IceCream(2))
        order.add_item(IceCream(1))
        order.add_item((IceCream(3)))
        self.assertEqual(Money('0.79'), order.calculate_tax(), "Test Order: cal tax with items")

    def test_get_menu_items(self):
        order = Order()
        order.add_item(Candy(.45))
        order.add_item(Cookies(1))
        order.add_item(Candy(.5))
        order.add_item(IceCream(2))
        order.add_item(Candy(.31))
        order.add_item(Cookies(2))
        order.add_item(IceCream(1))
        order.add_item(Candy(.25))
        order.add_item((IceCream(3)))
        ordered_items = order.get_items()
        self.assertTrue(isinstance(ordered_items[0], MenuItems.Candy))
        self.assertTrue(isinstance(ordered_items[3], MenuItems.Candy))
        self.assertTrue(isinstance(ordered_items[4], MenuItems.Cookies))
        self.assertTrue(isinstance(ordered_items[6], MenuItems.IceCream))
        self.assertTrue(isinstance(ordered_items[8], MenuItems.IceCream))

