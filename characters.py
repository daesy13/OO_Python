import random

class Characters:
    def __init__(self, name, **kwargs):
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)



class Thief(Characters):
    sneaky = True

    def __init__(self, name, sneaky= True, **kwargs):
        super().__init__(name, **kwargs)
        self.sneaky = sneaky

    def pickpocket(self):
        # print("Called by {}".format(self))
        return self.sneaky and bool(random.randint(0,1))

    def hide(self, light_level):
        return self.sneaky and light_level < 10
