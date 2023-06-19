#Generators are used to generate the value on the fly ,Lets see what are the syntax etc etc
#they are special type of function, which can create instantly on the fly , this can save the memory

def my_generator():
    for i in range(5):
        yield i          #Yield is the  key word that defines a generator


gen=my_generator()      #this is one more way of dealing with on the fly values
for j in gen:
    print(j)


#Benefits of generator
#They allow you to store the data on the fly , when you work on large data sets
# Memory management is efficient
#you can also use complex generator also 
        