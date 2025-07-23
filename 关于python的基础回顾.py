class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def show(self):
        print(f"{self.num}/{self.den}")

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other_fraction):

        new_num = self.num * other_fraction.den + self.den * other_fraction.num

        new_den = self.den * other_fraction.den
        cmmn = gcd(new_num, new_den)
        return Fraction(new_num // cmmn, new_den // cmmn)

    def __eq__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den

        return first_num == second_num


my_fraction = Fraction(3, 5)

print(my_fraction.__str__())
print(str(my_fraction))


# Greatest common division definition


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


f1 = Fraction(1, 4)
f2 = Fraction(1, 2)

print(f1 + f2)
