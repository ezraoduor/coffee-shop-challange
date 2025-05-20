class Coffee:
    all = []

    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Coffee name must be a string")
        if not value:
            raise ValueError("Coffee name cannot be empty")
        self._name = value

    def orders(self):
        from order import Order
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
       return len(self.orders())
