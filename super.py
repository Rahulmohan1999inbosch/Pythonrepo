#Super key word in python

class parentclass:
    def parent_method(self):
        print("This is the parent method")

class childclass(parentclass):
    
    def parent_method(self):
        print("This is a parent1 class")
        
    def child_method(self):
        print("This is a child class")    #This is a child class
        super().parent_method()           #This is the parent method

child_object=childclass()
child_object.child_method()

#Here in the above example we have a parent method in both the classes and in order to use the parent method that is present in the chils's parent class you can use super keyword to invoke that method

#Here we have one more example to demonstrate the super keyword

class Area:
    def __init__(self,length,bredth):
        self.length=length
        self.bredth=bredth

    def area(self):
        print(f"The area of the rectangle is {self.length*self.bredth}") 
        # The area of the rectangle is 540

class Volume(Area):
    def __init__(self,length,bredth,height):
        super().__init__(length,bredth)
        self.height=height
      
    def volume(self):
        print(f"volume of the cuboid id {self.length *self.bredth*self.height}") #volume of the cuboid id 48060


a=Area(12,45)
a.area()

v=Volume(12,45,89)
v.volume()

#The above example is another way of using super key word in python
