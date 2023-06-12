#getters() and setters()
#This is used more in OOPs programming

class Myclass:
    def __init__(self,fname,lname) -> None:
      self._fname=fname
      self._lname=lname

    @property
    def email(self):
       return f"{self._fname} ------>{self._lname}"
    

    @email.setter
    def email(self,new_email):
        print("settig value ...")
        self._fname=new_email
  
obj=Myclass('Rahul','B')
#print(obj.email)
obj.email="Shilpajyot"
#print(obj.email)


###########################Second example of getters and setters#########################################
class Myclass:
   def __init__(self,value):
      self._value=value

   @property
   def ten_value(self):
      return 10*self._value
   
   @ten_value.setter
   def ten_value(self,value):
      self._value=value

   
obj=Myclass(10)
obj.ten_value=90909
print(obj.ten_value)

#so insteas of modifying the values as function you can simply use it as a property and the set the values 

#Note
#When some variable that are created while creating an object is used to create a new variable ,this is where getters and setters come into picture
#you can create a complex calculation for the varaible for setter and getter metods.

   
   
   



  
     


    

   