#decorators in python
#decorator decorators the existing function and returnd the decorated function, existing function can be python in built function and function can also be user defined function , 
 
#hello() method prints hello world but you can modify this fuction using decorator
#greet function is the modified function here hello() function is the base function and to modify this @greet is the function that is created 
# below @greet we can put our function and when you call this function the base function  is modified as we can see,

def greet(fx):
    def mfx():
        print("hello Rahul")
        fx()
        print("Hey how you doing")
    return mfx



@greet                       #This is more preferred .
def hello():
    print('hello world')

greet(hello)()   #This is another way of invoking the decorator as , if you are not using the @ keyword


#How to pass arguments in the decorators, this is a little bit tricky

def summation(fx):
    def mfx(*args,**kwargs):
        print ("This is addition of two numbers")
        fx(*args,**kwargs)
        print("Addition of numbers is done")

    return mfx    #returing the modified function is important and for passing the arguments use the *args and **kwags

@summation
def add(x,y):
    print(x+y)

add(12,445)   #This is addition of two numbers
#               457
#               Addition of numbers is done





  
