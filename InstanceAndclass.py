#Instace variable and class variable

#Instance variable can be unique and it belongs to that particular object only where as class variable is common for all the objects

class school:
    school_name="Nehru centenary English School"  #This is a class variable
    def __init__(self,name,roll_no):
        self.name=name              #insatance variable
        self.roll=roll_no 

    def display(self):
        print(f"student name is {self.name} roll number is {self.roll} studies in {self.school_name}")


student1=school('Rahul',69)
student2=school('Rashmi',89)

#Here both are from same school so schoo_name can be used by both 

#suppose Rashmi changes her school as 
student1.school_name="KV international school"

#student name is Rahul roll number is 69 studies in KV international school

#now Rashmi has a instance variable as school name so she will refer the instance variable if instance variable is not present she will roll back to class variable

#you can change the class variable like this


school.school_name="vijaya bharthi public school"

student2.display() 
student1.display() 


##########################class methods#############################
#class methods that are bound to class and not instances
#class varibale can be modified using the class name, what if using instance variable you want to change class varibale for that we use the classmethod decorator
class Employee:
    
    company='Bosch'
    
    @classmethod
    def changecompany (cls,new_name):  #cls will hold the class name
        cls.company=new_name

emp1=Employee()
emp2=Employee()
print(emp1.company) #Bosch

emp1.changecompany('google')
print(emp1.company)
print(emp2.company)

#This is how you can use the classmethod decorator to modify class variable via instance varaible










      