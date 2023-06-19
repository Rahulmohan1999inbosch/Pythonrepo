#operator over loading in pyhton using magic /Dunder method

class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):
        return f"{self.i}i + {self.j}k + {self.k}k"
    
    def __add__(self,self1):
        print("adding two vectors")
        #return f"{self.i+self1.i}i + {self.j+self1.j}j + {self.k+self1.k}k "
        #return a vector
        return Vector(self.i+self1.i , self.j+self1.j, self.k+self1.k)
  


v1=Vector(3,4,5)
print(str(v1))
v2=Vector(4,8,5)
print(str(v2))

#now we can add the 3 vectors and see the outputs ,but making v1+v2 does not work as python does not know how to add the vectors so in this case we can use the magic/ dunder method

v3=v1+v2 #7i + 12j + 10k  "here  + operator got overloaded as you can see "
# v1+v2 return type is a string but we want a new fector 

print(str(v3))
print(type(v3))


