#Short hand if else is very handy,When you write a single line expression short hand if else is very handy
a=330
b=3300
print('A') if a>b else print('====') if a==b else print("B") # output is B here we cascaded one more if else inside ele block

#print the maximum of 3 numbers

number2=303
number1=302
number3=301

print(number1) if number1>number2 and number1>number3 else print(number2) if number2>number1 and number2>number3 else print("All are eqaula") if number1==number2 and number1==number3  else print(number3)

#This is an example how of how to use short if else statement

#print something is a number is greater than something
A=33
print('yes') if A>23 else "" #Thus is the syntax of using shorthand if and else