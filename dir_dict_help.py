#dir()  ,__dict__, help() Theses will help you to give an overview any unknown classes and their methods
#dir()  ,help() and __dict__ 

x=[1,2,4]
print(dir(x))  #you will get list of all the methods and attribute present in list class.
for i in dir(x):
    print(i)

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p=person('Rahul',24)
print(p.__dict__)      #{'name': 'Rahul', 'age': 24} what ever you have set as self. will get in  form of a dictionary


##help()
print(help(str))