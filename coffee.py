class Coffee:
    def __init__(self, name):
      self.name = name 
      if not isinstance(name,str):
         raise TypeError("the name must be a string")