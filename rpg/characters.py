class Character:
    def __init__(self, name="", **kwargs):
        if not name:
            raise ValueError("name is required")
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        # __str__ control how an instance convert into a str
        # this will call the name of the class and the attribute name
        # you will get "Thief: Daesy"
        return "{}: {}".format(self.__class__.__name__, self.name)
