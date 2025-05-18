class Coffee:

    all = []

    def __init__(self, name):
        self.name = name
        if not isinstance(name, str):
            raise TypeError("the name must be a string")
        if  len(name) < 3:
            raise ValueError("name must be atleast 3 characters long")
        self._name = name
        Coffee._all.append(self)
