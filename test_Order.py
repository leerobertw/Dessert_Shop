from unittest import TestCase

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
