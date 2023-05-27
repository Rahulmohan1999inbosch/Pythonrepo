# Today we will be learning how to pass argument in python Never the less we have already discussed how to do .

# how to sef defalut argument
def average(a=23,b=7):  # Here we can set a defalut value if we did't pass the value defalut value is assigned to variable
    print(a+b)

average(56)           # here 56 is passed so a=56 is assigned where as b takes the defalut value 7
average()             # No value is passed hence default value 23 ,7 will be assigned to variables
average(b=10,a=69)    # here a order is not maintained for first and second argument so we can call with any order

# Variable Length arguments you can pass any number of arguments

def sum(*numbers):     # it takes variale length argument 
    for i in numbers:   # here number is a tuple
        print(i)
    

sum(1,2,3,4,5)


def numdict(**numbers):        # here ** implies it can take key value pair as argument and stores as dictionary
    print(numbers)             # the output look something like this for numbers
                               #{'Rahul': 12, 'Sagar': 69}

numdict(Rahul=12,Sagar=69)      # while passing the argument pass it as key and value pair 
                       
