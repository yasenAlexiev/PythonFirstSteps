import math


# Problem 1
# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
class Line:

    def __init__(self, coord1, coord2):
        self.coord1 = coord1
        self.coord2 = coord2

    def distance(self):
        d_x = (abs(self.coord1[0] - self.coord2[0])) ** 2
        d_y = (abs(self.coord1[1] - self.coord2[1])) ** 2

        return math.sqrt(d_x + d_y)

    def slope(self):
        return (self.coord2[1] - self.coord1[1]) / (self.coord2[0] - self.coord1[0])


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)
print(li.distance())
print(li.slope())


class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return math.pi * self.radius ** 2 * self.height

    def surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)


c = Cylinder(2, 3)
print(c.volume())
print(c.surface_area())


class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account owner:   {self.owner}" + f"\nAccount balance: ${self.balance}"

    def deposit(self, amount):
        self.balance += amount
        print("Deposit Accepted")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Funds Unavailable!")
        else:
            self.balance -= amount
            print("Withdrawal Accepted")


acct1 = Account('Yasen',100)
print(acct1)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)