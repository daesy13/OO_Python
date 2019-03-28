# run age = NumString(25)
# >>> age + 5
# 30
# >>> 5 + age
# 30
# >>> age += 1
# 26

class NumString:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
        return self.value

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __add__(self, other):
        if '.' in self.value:
            return float(self) + other
        return int(self) + other

    # reflective add
    def __radd__(self, other):
        return self + other

    # inplace add
    def __iadd__(self,other):
        self.value = self + other
        return self.value