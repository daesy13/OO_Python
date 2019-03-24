import random

class Thief:
    sneaky = True

    def pickpocket(self):
        # print("Called by {}".format(self))
        if self.sneaky:
            return bool(random.randint(0,1))
        return False