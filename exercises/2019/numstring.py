# Magic Methods

class NumString:
    def __init__(self, value):          # __init__ - Customize the initialization of your instances
        self.value = str(value)

    def __str__(self):                  # __str__ - Control how your instances turn into strings
        return self.value

    def __int__(self):                  # __int__ - Control int() conversion
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __add__(self, other):           # works only for NumString(5) + 2, not 2 + NumString(5)
        if '.' in self.value:
            return float(self) + other
        return int(self) + other

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.value = self + other
        return self.value


five = NumString(5)
str(five)       # returns '5'
int(five)       # returns 5
float(five)     # returns 5.0
five + 2        # returns 7
five + 4.2      # returns 9.2

