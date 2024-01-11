

class Order:
    def __init__(self):
        self.menu_items = []

    def add_item(self, item):
        self.menu_items.append(item)

    def get_items(self):
        return sorted(self.menu_items, key=lambda item: type(item).__name__)

    def calculate_total_and_tax(self):
        if len(self.menu_items) > 0:
            totals = [t.get_total_and_tax() for t in self.menu_items]
            total_cost, total_tax = map(sum, zip(*totals))
            return round(total_cost, 2), round(total_tax, 2)
        return 0, 0
