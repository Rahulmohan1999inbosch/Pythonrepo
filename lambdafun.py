#lambda functions , this is a very interesting function
#This is a simple expression function

def double(num):
    print(num*2)

double(5)

#This can be made via lambda function also
#function_name=lambda (variables):return expression
double1=lambda x:x*2
print(double1(6))

#sum of 3 numbers using lambda
summ=lambda a,b,c:a+b+c
print(summ(34,56,89))  #179
#They can also be used to passed as an argument to an higher order function

def apply(func,value):
    return 10+func(value)

print(apply(lambda x:x**2,9))  #91  

#like this you can pass function as an argument 


