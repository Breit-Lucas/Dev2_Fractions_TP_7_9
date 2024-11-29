from math import gcd

class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : Le dénominateur doit-être différent de 0
        POST : Initialisation de num et den
        """
        self.__num = num
        if den == 0:
            raise ZeroDivisionError("Le dénominateur ne peut pas être égal à zéro")
        else:
            self.__den = den
        self.simplification()


    @property
    def numerator(self):
        return self.__num


    @property
    def denominator(self):
        return self.__den


    def simplification(self):
        div_commun = gcd(self.__num, self.__den)

        self.__num = self.__num // div_commun
        self.__den = self.__den // div_commun


    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : Accès à num et den
        POST : Renvoies la fraction actuelle
        """
        return f"{self.__num} / {self.__den}"

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : Accès à num et den
        POST : Renvoies la fraction actuelle simplifiée au maximum avec le numérateur qui reste si il faut
        """
        if self.__den == 0:
            raise ZeroDivisionError("Le dénominateur ne peut pas être égal à zéro")

        entier = self.__num // self.__den

        reste = abs(self.__num % self.__den)

        if reste == 0:
            return f"{entier}"
        else:
            return f"{entier} + {reste} / {self.__den}"

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : other doit être un objet de type fraction
         POST : renvoie la fraction resultante de la somme
         """
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être de type Fraction")
        new_num = self.__num * other.denominator + other.numerator * self.__den
        new_den = self.__den * other.denominator

        result = Fraction(new_num, new_den)
        return result

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : other doit être un objet de type fraction
        POST : renvoie   la fraction resultante de la soustraction
        """
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être de type Fraction")

        new_num = self.__num * other.__den - other.__num * self.__den
        new_den = self.__den * other.__den

        result = Fraction(new_num, new_den)
        return result

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : other doit être un objet de type fraction
        POST : renvoie la fraction resultante de la multiplication
        """
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être de type Fraction")
        new_num = self.__num * other.__num
        new_den = self.__den * other.__den

        result = Fraction(new_num, new_den)
        return result

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : other doit être un objet de type fraction
        POST : renvoie la fraction resultante de la division
        """
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être de type Fraction")
        new_num = self.__num * other.__den
        new_den = self.__den * other.__num

        result = Fraction(new_num, new_den)
        return result

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : other doit être un entier
        POST : renvoies la fraction resultante de la puissance
        """
        new_num = self.__num ** other
        new_den = self.__den ** other

        result = Fraction(new_num, new_den)
        return result

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : other doit être un objet de type fraction
        POST : renvoie True si les deux fractions sont égales et false si non

        """
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être de type Fraction")
        if self.__num == other.__num and self.__den == other.__den:
            return True
        else:
            return False

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : accès à num et den
        POST : renvoie la forme décimale de la fonction
        """
        result = self.__num / self.__den
        return round(result, 2)

    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    # ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : __num doit être un entier
        POST : renvoie true si le numérateur vaut zéro
        """
        return self.__num == 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : __den ne doit pas être égal à zéro
        POST : renvoie true si la fraction est un entier
        """
        return self.__num % self.__den == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : __num et __den doivent être des entiers
        POST : renvoie True si la fraction est propre$
        """

        return abs(self.__num) < self.__den

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : __num et __den doivent être des entiers
        POST : renvoie true si le numérateur et le dénominateur sont 1
        """
        return abs(self.__num) == 1 and self.__den == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference is a unit fraction

        PRE : other doit être de type fraction
        POST : renvoie true si la différence des deux fractions vaut 1
        """
        if isinstance(other, Fraction):
            diff = abs(self.__num * other.__den - other.__num * self.__den)
            den = self.__den * other.__den
            return diff == 1 and den > 0
        raise TypeError("L'opérande doit être une Fraction.")


frac1 = Fraction(1, 2)
frac2 = Fraction(2, 3)


print(frac1.__add__(frac2))
print(frac1.__sub__(frac2))
print(frac1.__mul__(frac2))
print(frac1.__truediv__(frac2))
print(frac1.__pow__(2))
print(frac1.__eq__(frac2))
print(frac1.__float__())
print(frac1.is_zero())
print(frac1.is_integer())
print(frac1.is_proper())
print(frac1.is_unit())
print(frac1.is_adjacent_to(frac2))
