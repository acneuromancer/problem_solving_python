class Fraction:

    def __init__(self, top, bottom):

        def gcd(m, n):
            while m % n != 0:
                old_m = m
                old_n = n

                m = old_n
                n = old_m % old_n

            return n

        common = gcd(top, bottom)
        self.num = top // common   # numerator
        self.den = bottom // common     # denominator

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

    def show(self):
        print("%d/%d" % (self.num, self.den))

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num == second_num

    def __gt__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num > second_num

    def __ge__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num >= second_num

    def __lt__(self, other):
        first_num = self.num * other.den
        second_num = self.den * other.num
        return first_num < second_num

    def __le__(self, other):
        first_num = self.num * other.den
        second_num = self.den * other.num
        return first_num <= second_num

    def __ne__(self, other):
        first_num = self.num * other.den
        second_num = self.den * other.num
        return first_num != second_num
