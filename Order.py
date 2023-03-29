from money.money import Money

class Order:
    def __init__(self):
        self.menu_items = []

    def add_item(self, item):
        self.menu_items.append(item)

    def calculate_total(self):
        total = Money('0', 'USD')
        for item in self.menu_items:
            total += item.calculate_total()
        return total

    def calculate_tax(self):
        tax = Money('0', 'USD')
        for item in self.menu_items:
            tax += item.calculate_tax()
        return tax
