#object oriented programming OOPS concept
#using object oriented programming we can create templated using which we can create a lot of instances

#create a cass of bussinessman who has a name , sales ,profit

class bussinessman():
    def __init__(self,name,sales,profit):
        self.name=name
        self.sales=sales
        self.profit=profit

    def display(self):
        print(f"Name--->{self.name}")
        print(f"sales--->{self.sales}")
        print(f"profit--->{self.profit}")

    
Employee1=bussinessman('Rahul',6000,2000)
Employee2=bussinessman('Rashmi',3444,798)
Employee3=bussinessman('Sagar',4443,456)

#Right now I have created 3 employees  who has a class bussinessman

Employee1.display()
Employee2.display()
Employee3.display()