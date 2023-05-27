from unittest import TestCase
from money.money import Money
from MenuItems import Candy, Cookies, IceCream, Sundae, SundaeToppings


class TestSundae(TestCase):
    def test_calculate_total_no_toppings(self):
        sundae = Sundae()
        self.assertEqual((Money('3.40', 'USD'), Money('.238', 'USD')), sundae.get_total_and_tax(),
                         'Sundae: calculate total: no toppings')

    def test_calculate_total_hot_fudge(self):
        sundae = Sundae()
        sundae.add_topping(SundaeToppings.Hot_Fudge)
        self.assertEqual((Money('4.65', 'USD'), Money('.3255', 'USD')), sundae.get_total_and_tax(),
                         'Sundae: calculate total: hot fudge')

    def test_calculate_total_hot_fudge_peanuts(self):
        sundae = Sundae()
        sundae.add_topping(SundaeToppings.Hot_Fudge)
        sundae.add_topping(SundaeToppings.Peanuts)
        self.assertEqual((Money('5.00', 'USD'), Money('0.35', 'USD')), sundae.get_total_and_tax(),
                          'Sundae: calculate total: hot fudge, peanuts')

    def test_calc_total_double_hot_fudge_peanuts(self):
        sundae = Sundae()
        sundae.add_topping(SundaeToppings.Hot_Fudge)
        sundae.add_topping(SundaeToppings.Hot_Fudge)
        sundae.add_topping(SundaeToppings.Peanuts)
        self.assertEqual((Money('6.25', 'USD'), Money('.4375', 'USD')), sundae.get_total_and_tax(),
                         'Sundae: calculate total: double hot fudge, peanuts')

    def test_calculate_total_strawberry_double_coconut(self):
        sundae = Sundae()
        sundae.add_topping(SundaeToppings.Strawberry_Syrup)
        sundae.add_topping(SundaeToppings.Coconut)
        self.assertEqual((Money('4.35', 'USD'), Money('.3045', 'USD')), sundae.get_total_and_tax(),
                         'Sundae: calculate total: Strawberry Syrup, coconut')

    def test_str(self):
        sundae = Sundae()
        sundae.add_topping(SundaeToppings.Hot_Fudge)
        sundae.add_topping(SundaeToppings.Carmel_Syrup)
        sundae.add_topping(SundaeToppings.Peanuts)
        self.assertEqual('Sundae with Hot_Fudge, Carmel_Syrup, Peanuts', str(sundae))


class TestIceCream(TestCase):
    def test_calculate_total_one_scoop(self):
        self.assertEqual((Money('1.70', 'USD'), Money('.119', 'USD')), IceCream('1').get_total_and_tax(),
                         'Cal total, one scoop')

    def test_calculate_total_two_scoop(self):
        self.assertEqual((Money('3.40', 'USD'), Money('.238', 'USD')), IceCream('2').get_total_and_tax(),
                         'Cal total, one scoop')


class TestCookies(TestCase):
    def test_one_dozen_cookies(self):
        self.assertEqual((Money('6.25', 'USD'), Money('0.390625', 'USD')), Cookies('1').get_total_and_tax(),
                         'Cost and Tax, one dozen')
    def test_two_dozen_cookies(self):
        self.assertEqual((Money('12.50', 'USD'), Money('0.78125', 'USD')), Cookies('2').get_total_and_tax(),
                         'Cost and Tax, 2 dozen')

class TestCandy(TestCase):
    def test_one_lb_candy(self):
        self.assertEqual((Money('4.75', 'USD'), Money('.296875','USD')), Candy('1.0').get_total_and_tax(),
                         'Cost and Tax, 1 lb')

    def test_one_half_lb_candy(self):
        self.assertEqual((Money('2.375', 'USD'), Money('.1484375','USD')), Candy('0.5').get_total_and_tax(),
                         'Cost and Tax, 1/2 lb')