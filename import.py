#Today we shall see how imoport works , you can invoke import by simply using import keyword, using import use can use all the menthods that is used in the module , accessing becomes easy

import math
print(math.floor(4.4444))  #like this we can use floor method this is available in math module

# from key word , if you want to import only one method from the module, 

from math import sqrt  #from math module you imported sqrt method if '*'Then all the  methods  can be used but this is not recommended,as it leads to ambiquity
print(sqrt(9))

#as key word, example import math as m , this will create alias for math module , you use math as m.
#This is applicable for function also example from ------->ath import sqrt as q<------------


#dir method 
#This mwthod prints all the methods and variables present in the module, as a list output
print(dir(math))
'''
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
'''

# Now let us create a module, Create a module called module.py write a method and a variale in it lets import and execute

import summodule as sm
print(sm.summation(10,20)) #30 is printed
print(sm.value) #This is a simple string

print(dir(sm))
#['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'summation', 'value']

from summodule import summation,value
print(summation(23,67)) #90
print(value)    #This is a simple string


print(sm.__name__)
print(sm.__package__)
print(sm.__file__)
print(sm.__spec__)










