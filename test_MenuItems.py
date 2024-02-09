from unittest import TestCase
from MenuItems import Candy, Cookies, IceCream, Sundae, SundaeToppings, IceCreamConeType, IceCreamFlavors


class TestSundae(TestCase):
    def test_calculate_total_no_toppings(self):
        sundae = Sundae()
        self.assertEqual((3.40, .26), sundae.get_total_and_tax(), 'Sundae: calculate total: no toppings')

    def test_calculate_total_hot_fudge(self):
        sundae = Sundae()
        sundae.add_topping(SundaeToppings.Hot_Fudge)
        self.assertEqual((4.65, .35), sundae.get_total_and_tax(), 'Sundae: calculate total: hot fudge')

    def test_calculate_total_hot_fudge_peanuts(self):
        sundae = Sundae()
        sundae.add_topping(SundaeToppings.Hot_Fudge)
        sundae.add_topping(SundaeToppings.Peanuts)
        self.assertEqual((5.00, 0.38), sundae.get_total_and_tax(), 'Sundae: calc total: hot fudge, peanuts')

    def test_calc_total_double_hot_fudge_peanuts(self):
        sundae = Sundae()
        sundae.add_topping(SundaeToppings.Hot_Fudge)
        sundae.add_topping(SundaeToppings.Hot_Fudge)
        sundae.add_topping(SundaeToppings.Peanuts)
        self.assertEqual((6.25, .47), sundae.get_total_and_tax(),
                         'Sundae: calculate total: double hot fudge, peanuts')

    def test_calculate_total_strawberry_double_coconut(self):
        sundae = Sundae()
        sundae.add_topping(SundaeToppings.Strawberry_Syrup)
        sundae.add_topping(SundaeToppings.Coconut)
        self.assertEqual((4.35, 0.33), sundae.get_total_and_tax(),
                         'Sundae: calculate total: Strawberry Syrup, coconut')

    def test_str(self):
        sundae = Sundae()
        sundae.add_topping(SundaeToppings.Hot_Fudge)
        sundae.add_topping(SundaeToppings.Carmel_Syrup)
        sundae.add_topping(SundaeToppings.Peanuts)
        self.assertEqual('Sundae with Hot_Fudge, Carmel_Syrup, Peanuts', str(sundae))


class TestIceCream(TestCase):
    def test_calculate_total_one_scoop(self):
        self.assertEqual((1.70, 0.13),
                         IceCream(1, IceCreamFlavors.Vanilla, IceCreamConeType.Cone).get_total_and_tax(),
                         'Cal total, one scoop')

    def test_calculate_total_two_scoop(self):
        self.assertEqual((3.40, 0.26),
                         IceCream(2, IceCreamFlavors.Vanilla, IceCreamConeType.Cone).get_total_and_tax(),
                         'Cal total, one scoop')


class TestCookies(TestCase):
    def test_one_dozen_cookies(self):
        self.assertEqual((6.25, 0.19), Cookies(1).get_total_and_tax(), 'Cost and Tax, one dozen')

    def test_two_dozen_cookies(self):
        self.assertEqual((12.50, 0.38), Cookies(2).get_total_and_tax(), 'Cost and Tax, 2 dozen')

class TestCandy(TestCase):
    def test_one_lb_candy(self):
        self.assertEqual((4.75, 0.14), Candy(1.0).get_total_and_tax(), 'Cost and Tax, 1 lb')

    def test_one_half_lb_candy(self):
        self.assertEqual((2.38, 0.07), Candy(0.5).get_total_and_tax(), 'Cost and Tax, 1/2 lb')
