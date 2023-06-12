#Access ,modifiers
#they are used to limit the acess of class varibles or  methods]
#by defalut all the variables and method are private

class Employee:
    def __init__(self,name):
        self.__name=name # "--"<variable_name> this is private varible

obj=Employee('Rahul')
#print(obj.__name)  #This cannot be accessed as its a private variable directly

print(obj._Employee__name)

