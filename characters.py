import random

class Character:
    def __init__(self, name, **kwargs):
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)           # example = Thief("Kenneth", scars=None, favorite_weapon="Wit")


class Thief(Character):                         # Thief class inherits from Character class
    sneaky = True          

    def __init__(self, name, sneaky=True, **kwargs):
        super().__init__(name, **kwargs)
        self.sneaky = sneaky

    def pickpocket(self):                # classes don't use methods, only instances, so they need at least one                                             parameter - instance
        return self.sneaky and bool(random.randint(0, 1))

    def hide(self, light_level):
        return self.sneaky and light_level < 10
