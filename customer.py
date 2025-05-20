class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not 1 <= len(value) <= 15:
            raise ValueError("Name must be 1–15 characters long")
        self._name = value

    def orders(self):
        from order import Order
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order

        coffee_orders = [
            order for order in Order.all if order.coffee == coffee]
        if not coffee_orders:
            return None
        
        spending = {}
        for order in coffee_orders:
            spending[order.customer] = spending.get(
                order.customer, 0) + order.price
        
        return max(spending, key=spending.get)
