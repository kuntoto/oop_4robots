from abc import ABC, abstractmethod

class Amath(ABC):
    @property
    @abstractmethod
    def pi(self):
        pass
    
    @abstractmethod
    def sqrt(self, n):
        pass
    
class Mymath(Amath):
    def sin(self, r, n=50):
        ''' Approximate sin(r) using Taylor series '''
        import math
        sin, sign = 0, 1
        for i in range(1, n, 2):
            sin += sign * (r ** i / math.factorial(i))
            sign *= -1
        return sin
        
    @property
    def pi(self,n=1000000):
        ''' Calculate pi using Gregory-Leibniz Series '''
        pi_approx = 0
        for i in range(n):
            term = 1 / (2*i+1)
            if i%2 == 0:
                pi_approx += term
            else:
                pi_approx -= term
        return 4 * pi_approx
    
    def sqrt(self, n):
        ''' Calculate sqrt(n) using Babylonian method '''
        x = n
        y, e = 1, 0.0000001
        while (x - y > e):
            x = (x + y) / 2
            y = n / x
        return x
        
import math
m = Mymath()
print(m.pi, math.pi)
print(math.sqrt(2), m.sqrt(2))
print(math.sin(math.pi/2), m.sin(math.pi/2))
