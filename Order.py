

class Order:
    def __init__(self):
        self.menu_items = []

    def add_item(self, item):
        self.menu_items.append(item)

    def get_items(self):
        return sorted(self.menu_items, key=lambda item: type(item).__name__)

    def get_total_and_tax(self):
        total = 0
        tax = 0
        for item in self.menu_items:
            tot, tx = item.get_total_and_tax()
            total += tot
            tax += tx
        return round(total, 2), round(tax, 2)
