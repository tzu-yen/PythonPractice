class Fraction(object):
    def __init__(self, num, den):
        self.num = num
        self.den = den
    def __str__(self):
        return str(self.num)+'/'+str(self.den)
    def __add__(self, otherfraction):
        newnum =(self.num*otherfraction.den + self.den*otherfraction.num)
        newden = self.den*otherfraction.den
        this_gcd = self.gcd(newnum, newden)
        return Fraction(newnum/this_gcd, newden/this_gcd)
    def __sub__(self, otherfraction):
        pass
    def __mul__(self, otherfraction):
        pass
    def __div__(self, otherfraction):
        pass
    def __lt__(self, otherfraction):
        return self.num*otherfraction.den < otherfraction.num * self.den
    def __gt__(self, otherfraction):
        return not self.__lt__(otherfraction)
    def __eq__(self, otherfraction):
        firstnum = self.num * otherfraction.den
        secondnum = otherfraction.num * self.den
        return firstnum == secondnum
        
    def gcd(self,m,n):
        while m%n!=0:
            oldm=m; oldn=n
            m=oldn; n=oldm%oldn
        return n


if __name__ == '__main__':
    f = Fraction(1,4)
    f1 = Fraction(4,5)
    print 'I ate %s of the pizza' % f
    print (f + f1)
    print f == f1
    print '%s is less than %s: %s' % (f, f1, str(f<f1))
    print '%s is greater than %s: %s' % (f, f1, str(f>f1))
