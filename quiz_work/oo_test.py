class Student:
    name = "Daesy"

me = Student()

print(me.name)

class Student:
    name = "Daesy"

    def praise(self):
        return "You're doing a great job, {}".format(self.name)

class Student:
    name = "Your Name"

    def praise(self):
        return "You inspire me, {}".format(self.name)

    def reassurance(self):
        return "Chin up, {}. You'll get it next time!".format(self.name)

    def feedback(self, grade):
        if grade > 50:
            return self.praise()
        else:
            return self.praise()