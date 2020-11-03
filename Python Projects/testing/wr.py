class Robot:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hi, I am " + self.name)

    def __repr__(self):
        0

class PhysicianRobot(Robot):
    pass

y = PhysicianRobot("James")

print(y, type(y))

y.say_hi()
