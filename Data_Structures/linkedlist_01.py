# This is program for single linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class linkedlist:
    def __init__(self):
        self.head=None

    def display(self):
        
        if self.head==None:
            print('Empty list')
          
        else:
            temp=self.head
            while(temp):
                print("--------->",temp.data,end=" ")
                temp=temp.next

          
        

l=linkedlist()    
n1=Node(10)
l.head=n1
n2=Node(20)
n1.next=n2
n3=Node(3)
n2.next=n3
n4=Node(56)
n3.next=n4

x=n2.next
print(x.data)

print(n3.next.data)
print(n4.next)
print(n4.data)

n5=Node(619)
n4.next=n5
l.display()


    
    
  





            

            


  