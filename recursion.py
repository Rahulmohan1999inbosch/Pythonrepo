#Today we will be doing recursion ,and recursion whcih means a function calling itself
# we generally do a program to find the factorila of two numbers
def factorial(number):
    if number ==1:
        return 1
    else:
        return number*factorial(number-1)
    
print(factorial(10))  #This will give you the factorial for number similary we can use recursion of numbers

#This is a very popular example for fibonasi series
def fibonachi(number):
    if number==1:
        return 1
    elif number==0:
        return 0
    else:
        return fibonachi(number-1)+fibonachi(number-2)
    
print(fibonachi(12))
#This is a famous example of using fibonacho series 


