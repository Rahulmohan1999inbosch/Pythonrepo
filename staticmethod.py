#Static methonds does not belong to any class or any instance , then why do we use this lets sees

#staticmthod it is prsent inside a class , you can use the methods inside the static class using instance varaible or a classname directly and do the operation , it becomes a generic method which you can use without usinfg the self keyword

#If some one is using your class and you want this method to be a part of the class , then you can simply put it under a class an call 


class Math:
    def __init__(self,num):
        self.num=num
    
    def add(self,n):
        self.num+=n

    @staticmethod
    def printmessage():
        print("Hey I can be called from instance varibale and also from class name")
        
    

a=Math(8)
print(a.num)
a.add(78)
print(a.num)

print(a.printmessage())  #Hey I can be called from instance varibale and also from class name
print(Math.printmessage())