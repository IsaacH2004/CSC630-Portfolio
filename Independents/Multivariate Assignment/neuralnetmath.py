# This is the derive module, which includes the mathvar class. 
# The class can be used in calculus, which will be important in the neural network project haha. 
# This code is heavily inspired by my work in CSC630: Machine Learning and the work of Dr. Nicholas Zufelt.

import math # math module for sin, cos, etc

# we need a function to flatten lists
def fltn(lst):
    """
    Flatten lst (presumably a nested list). 
    """
    to_rtn = []
    
    def fltn_inner(lst, to_rtn):

        for item in lst:
            if isinstance(item, (list, tuple)):
                to_rtn.append(fltn_inner(item, to_rtn))
            else:
                to_rtn.append(item)

        return [i for i in to_rtn if type(i) != list]
            
    return fltn_inner(lst, to_rtn)



class mathvar:

    """

    """

    def __init__(self, name):
        self.name = name
        self.items = self.name

    def evaluate(self, values):
        if self.name in list(values.keys()):
            return values[self.name] 
        else:
            return 0 
        
    def __call__(self, values):
        return self.evaluate(values)

    def d(self, values, d_):
        return 1

    def __add__(self, other):
        return addvar(self, other)

    def __radd__(self, other):
        return raddvar(self, other)

    def __sub__(self, other):
        return subvar(self, other)

    def __rsub__(self, other):
        return rsubvar(self, other)

    def __mul__(self, other):
        return mulvar(self, other)

    def __rmul__(self, other):
        return mulvar(other, self)

    def __truediv__(self, other):
        return divvar(self, other)

    def __rtruediv__(self, other):
        return divvar(other, self)

    def __pow__(self, other):
        return powvar(self, other)

    def __rpow__(self, other):
        return rpowvar(self, other)

    
                

#___________________________________________________________#

class addvar(mathvar):
    
    def __init__(self, me, other):
        self.other = other
        self.me = me
        self.items = [self.me if isinstance(self.me, (int, float)) else self.me.items,
                      self.other if isinstance(self.other, (int, float)) else self.other.items]
        # this helps with storage and identification later on, especially when we need to use the partial derivatives. 

    def evaluate(self, values):
        if isinstance(self.other, (float, int)):
            return self.me.evaluate(values) + self.other
        if isinstance(self.me, (float, int)):
            return self.other.evaluate(values) + self.me
        else:
            return self.other.evaluate(values) + self.me.evaluate(values)
        
    def d(self, values, d_):
        if d_ in fltn(self.items): # is this a function of d_?
            if isinstance(self.other, (int, float)): # regular derivative
                return self.me.d(values, d_) + 0 # derivative and chain rule
            if isinstance(self.me, (int, float)): 
                return self.other.d(values, d_) + 0
            else:
                return self.me.d(values, d_) + self.other.d(values, d_)
        else:
            return 0


class raddvar(mathvar):
    
    def __init__(self, me, other):
        self.other = other
        self.me = me
        self.items = [self.me if isinstance(self.me, (int, float)) else self.me.items,
                      self.other if isinstance(self.other, (int, float)) else self.other.items]
        # this helps with storage and identification later on, especially when we need to use the partial derivatives. 

    def evaluate(self, values):
        if isinstance(self.other, (float, int)):
            return self.other + self.me.evaluate(values) 
        if isinstance(self.me, (float, int)):
            return self.other.evaluate(values) + self.me
        else:
            return self.other.evaluate(values) + self.me.evaluate(values)
        
    def d(self, values, d_):
        if d_ in fltn(self.items): # is this a function of d_?
            if isinstance(self.other, (int, float)): # regular derivative
                return self.me.d(values, d_)  # derivative and chain rule
            if isinstance(self.me, (int, float)): 
                return self.other.d(values, d_)
            else:
                return self.other.d(values, d_) + self.me.d(values, d_) 
        else:
            return 0

        
class subvar(mathvar):
    
    def __init__(self, me, other):
        self.other = other
        self.me = me
        self.items = [self.me if isinstance(self.me, (int, float)) else self.me.items,
                      self.other if isinstance(self.other, (int, float)) else self.other.items]

    def evaluate(self, values):
        if isinstance(self.other, (float, int)):
            return self.me.evaluate(values) - self.other
        if isinstance(self.me, (float, int)):
            return self.other.evaluate(values) - self.me
        else:
            return  self.me.evaluate(values) - self.other.evaluate(values)
        
    def d(self, values, d_):
        if d_ in fltn(self.items): # is this a function of d_?
            if isinstance(self.other, (int, float)): # regular derivative
                return self.me.d(values, d_)  # derivative and chain rule
            else:
                return self.me.d(values, d_) - self.other.d(values, d_)
        else:
            return 0
        

class rsubvar(mathvar):
    
    def __init__(self, me, other):
        self.other = other
        self.me = me
        self.items = [self.me if isinstance(self.me, (int, float)) else self.me.items,
                      self.other if isinstance(self.other, (int, float)) else self.other.items]

    def evaluate(self, values):
        if isinstance(self.other, (float, int)):
            return  self.other - self.me.evaluate(values)
        if isinstance(self.me, (float, int)):
            return  self.me - self.other.evaluate(values)
        else:
            return  self.other.evaluate(values) - self.me.evaluate(values)

    def d(self, values, d_):
        if d_ in fltn(self.items): # is this a function of d_?
            if isinstance(self.me,(int,float)):
                return 0 - self.other.d(values, d_)
            else:
                return 0 - self.me.d(values, d_) 
        else:
            return 0
        

class mulvar(mathvar):

    def __init__(self, me, other):
        self.other = other
        self.me = me
        self.items = [self.me if isinstance(self.me, (int, float)) else self.me.items,
                      self.other if isinstance(self.other, (int, float)) else self.other.items]

    def evaluate(self, values):
        if isinstance(self.other, (float, int)):
            return self.me.evaluate(values) * self.other
        if isinstance(self.me, (float, int)):
            return self.other.evaluate(values) * self.me
        else:
            return self.other.evaluate(values) * self.me.evaluate(values)

    def d(self, values, d_):
        if d_ in fltn(self.items): # is this a function of d_?
            if isinstance(self.other, (int, float)): # regular derivative
                return self.me.d(values, d_) * self.other # derivative and chain rule
            if isinstance(self.me, (int, float)): 
                return self.other.d(values, d_) * self.me 
            else:
                return self.other.evaluate(values) * self.me.d(values, d_) + self.other.d(values, d_) * self.me.evaluate(values) # product rule
        else:
            return 0


class divvar(mathvar):

    def __init__(self, me, other):
        self.other = other
        self.me = me
        self.items = [self.me if isinstance(self.me, (int, float)) else self.me.items,
                      self.other if isinstance(self.other, (int, float)) else self.other.items]

    def evaluate(self, values):
        if isinstance(self.other, (float, int)):
            return self.me.evaluate(values) / self.other
        if isinstance(self.me, (float, int)):
            return self.me / self.other.evaluate(values)
        else:
            return self.other.evaluate(values) / self.me.evaluate(values)

    def d(self, values, d_):
        if d_ in fltn(self.items): # is this a function of d_?
            
            if isinstance(self.other, (int, float)): # regular derivative
                return self.me.d(values, d_) / self.other # derivative and chain rule
            if isinstance(self.me, (int, float)): # reverse reverse
                return self.me * (self.other ** (-1)).d(values, d_)
            else:
                return (self.other.evaluate(values) * self.me.d(values, d_) - self.other.d(values, d_) * self.me.evaluate(values)) / (self.other.evaluate(values) ** 2) # quotient rule
        else:
            return 0



class powvar(mathvar):

    def __init__(self, me, other):
        self.other = other
        self.me = me
        self.items = [self.me if isinstance(self.me, (int, float)) else self.me.items,
                      self.other if isinstance(self.other, (int, float)) else self.other.items]

    def evaluate(self, values):
        if isinstance(self.other, (float, int)):
            return self.me.evaluate(values) ** self.other
        if isinstance(self.me, (float, int)):
            return self.other.evaluate(values) ** self.me
            
        else:
            return self.other.evaluate(values) ** self.me.evaluate(values)

    def d(self, values, d_):
        if d_ in fltn(self.items): # is this a function of d_?
            return (self.other * self.me ** (self.other - 1)).evaluate(values) * self.me.d(values, d_) # derivative and chain rule
        else:
            return 0
        

class rpowvar(mathvar):

    def __init__(self, me, other):
        self.other = other
        self.me = me
        self.items = [self.me if isinstance(self.me, (int, float)) else self.me.items,
                      self.other if isinstance(self.other, (int, float)) else self.other.items]

    def evaluate(self, values):
        if isinstance(self.other, (float, int)):
            return  self.other ** self.me.evaluate(values)
        if isinstance(self.me, (float, int)):
            return self.me ** self.other.evaluate(values)
        else:
            return self.me.evaluate(values) ** self.other.evaluate(values)

    def d(self, values, d_):
        if d_ in fltn(self.items): # is this a function of d_? 
            return (ln(self.other) * self.other**self.me).evaluate(values) * self.me.d(values, d_) # derivative and chain rule
        else:
            return 0
        

# ______________________________________________________________FUNCTIONS (e, ln, sin, cos, tan, etc)______________________________________________________________

class exponent(mathvar):

    def __init__(self, x):
        self.x = x
        self.items = [x if isinstance(x, (int, float)) else x.items]

    def evaluate(self, values):
        return math.e**self.x if isinstance(self.x, (int, float)) else math.e ** self.x.evaluate(values)

    def d(self, values, d_):
        if d_ in fltn(self.items): # is e a function of d_? 
            return math.e**(self.x).evaluate(values) * self.x.d(values, d_) # derivative and chain rule
        else:
            return 0
        

class ln(mathvar):

    def __init__(self, x):
        self.x = x
        self.items = [x if isinstance(x, (int, float)) else x.items]

    def evaluate(self, values):
        return math.log(self.x) if isinstance(self.x, (int, float)) else math.log(self.x.evaluate(values))

    def d(self, values, d_):
        if d_ in fltn(self.items): # is ln a function of d_? 
            return (1 / self.x).evaluate(values) * self.x.d(values, d_) # derivative and chain rule
        else:
            return 0
        

class sin(mathvar):

    def __init__(self, x):
        self.x = x
        self.items = [x if isinstance(x, (int, float)) else x.items]

    def evaluate(self, values):
        return math.sin(self.x) if isinstance(self.x, (int, float)) else math.sin(self.x.evaluate(values))

    def d(self, values, d_):
        if d_ in fltn(self.items): # is sin a function of d_?
            return (cos(self.x)).evaluate(values) * self.x.d(values, d_) # derivative and chain rule
        else:
            return 0
        
    
class cos(mathvar):

    def __init__(self, x):
        self.x = x
        self.items = [x if isinstance(x, (int, float)) else x.items]

    def evaluate(self, values):
        return math.cos(self.x) if isinstance(self.x, (int, float)) else math.cos(self.x.evaluate(values))

    def d(self, values, d_):
        if d_ in fltn(self.items): # is cos a function of d_? 
            return -1 * (sin(self.x)).evaluate(values) * self.x.d(values, d_) # derivative and chain rule
        else:
            return 0    

    
class tan(mathvar):

    def __init__(self, x):
        self.x = x
        self.items = [x if isinstance(x, (int, float)) else x.items]

    def evaluate(self, values):
        return math.tan(self.x) if isinstance(self.x, (int, float)) else math.tan(self.x.evaluate(values))
    
    def d(self, values, d_):
        if d_ in fltn(self.items): # is tan a function of d_? 
            return (1 / (cos(self.x)**2)).evaluate(values) * self.x.d(values, d_) # derivative and chain rule
        else:
            return 0


class reluL(mathvar): # leaky relu- this way, the network isn't destroyed when we encounter a zero input. 

    def __init__(self, x):
        self.x = x
        self.items = [x if isinstance(x, (int, float)) else x.items]

    def evaluate(self, values):
        if isinstance(self.x, (int, float)):
            return self.x if self.x > 0 else 0
        else:
            return self.x.evaluate(values) if self.x.evaluate(values) > 0 else 0
  
    def d(self, values, d_):
         if d_ in fltn(self.items): # is this a function of d_? 
            return self.x.d(values, d_) if self.x.evaluate(values) >= 0 else 0.01  # derivative and chain rule 
         else:
            return 0


class relu(mathvar): # reular relu

    def __init__(self, x):
        self.x = x
        self.items = [x if isinstance(x, (int, float)) else x.items]

    def evaluate(self, values):
        if isinstance(self.x, (int, float)):
            return self.x if self.x > 0 else 0
        else:
            return self.x.evaluate(values) if self.x.evaluate(values) > 0 else 0
  
    def d(self, values, d_):
         if d_ in fltn(self.items): # is this a function of d_? 
            return self.x.d(values, d_) if self.x.evaluate(values) >= 0 else 0  # derivative and chain rule 
         else:
            return 0


class sigmoid(mathvar):

    def __init__(self, x):
        self.x = x
        self.items = [x if isinstance(x, (int, float)) else x.items]

    def evaluate(self, values):
        return (1 / (1 + exponent(-1*self.x))).evaluate(values)
    
    def d(self, values, d_):
        if d_ in fltn(self.items): # is this a function of d_? 
            return (1 / (1 + exponent(-1*self.x))).evaluate(values) * (1 - (1 / (1 + exponent(-1*self.x))).evaluate(values)) * self.x.d(values, d_) # derivative and chain rule
        else:
            return 0


class tanh(mathvar):

    def __init__(self, x):
        self.x = x
        self.items = [x if isinstance(x, (int, float)) else x.items]

    def evaluate(self, values):
        return ((exponent(self.x) - exponent(-1 * self.x)) / (exponent(self.x) + exponent(-1 * self.x))).evaluate(values)
    
    def d(self, values, d_):
        if d_ in fltn(self.items): # is this a function of d_? 
            return 1 - tanh(self.x).evaluate(values) ** 2  # derivative and chain rule
        else:
            return 0


