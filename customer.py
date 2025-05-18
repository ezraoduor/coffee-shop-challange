class Customer:

    all = []

    def __init__(self, name):
        self.name = name
        Customer.all._append(self)

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, value):
         if not isinstance(value, str):
            raise TypeError("name must be a string")
