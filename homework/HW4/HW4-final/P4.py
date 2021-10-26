class AutoDiffToy:

    def __init__(self, val, der=1.0):
        self.val = val
        self.der = der
        
    def __add__(self, other):
        try:
            value = self.val + other.val
            derivative = self.der + other.der 
        except AttributeError:
            value = self.val + other
            derivative = self.der
        finally:
            return AutoDiffToy(value, derivative)
    
    def __radd__(self, other):
        return self.__add__(other)
     
    def __mul__(self, other):
        try:
            value =  self.val * other.val
            derivative = self.der * other.val + self.val * other.der
        except AttributeError:
            value = self.val * other
            derivative = self.der * other
        finally:
            return AutoDiffToy(value, derivative)
        
    def __rmul__(self, other):
        return self.__mul__(other)


x = AutoDiffToy(2)
alpha = 2.0
beta = 3.0

#demos
f1 = alpha * x + beta
print(f1.val, f1.der)

f2 = x * alpha + beta
print(f2.val, f2.der)

f3 = beta + alpha * x
print(f3.val, f3.der)

f4 = beta + x * alpha
print(f4.val, f4.der)
