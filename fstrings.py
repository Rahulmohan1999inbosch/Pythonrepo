#fstrings in python is one the most beautifu feature using this you can insert a variable inside string and also used in string formatting
letter="Hey my name is {} and I'm from {}"
name="Rahul"
place="India" 
print(letter.format(name,place))  # output-->Hey my name is Rahul and I'm from India
print(letter.format(place,name))   #Hey my name is India and I'm from Rahul
# Here in place of {} you get the variales substitued in that place

#This is not that much convient instead of this we can go with fstrig

print(f"Hey my name is {name} and I live in {place}") #Hey my name is Rahul and I live in India
# This approach of using string is much simpler when you want to include a variable 

# Slicing the decimal values
number="For only {price:.2f}"
print(number.format(price=49.433333))

n1=23.34455
str1="The price of this item is {: .2f}" 
print(str1.format(n1))                   ## output The price of this item is  23.34

# The above can also be via fstring something like this
print(f"The price of the product is {n1: .3f}") #output --->The price of the product is  23.345
print(f"{n1: .4f}")   #output-->23.3446

# we can admit that f string is easier than using format method
# Suppose you dont want your f string to replace the values you have use something like this

print(f"Hey my name is {{name}} and I live in {{place}}")  #Hey my name is {name} and I live in {place}
#Prints exactly the same 
 
 







