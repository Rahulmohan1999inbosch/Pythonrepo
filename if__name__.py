#if __name__ = __main__
#Today we shall be learning about how and why this function is used in pyhton
import summodule
print(summodule.summation(23,76)) #30
                                 # 99
#99 is expected why is 30 coming tht is becuase in summodule summation method is also called , this is  major problem to solve this problem ,
#we use name=main , so that this duplication can be avoided

# def summation(number1,number2):
#     return number1+number2

# value="This is a simple string"
# print(__name__)
# if __name__ =="__main_-":
    
#   print(summation(10,20))
#summation is imported and if you run summtion.py file directly __name__ will be equal to "__name__"
#if you import the module then in __name__ we get module name
# like this we can avoid this issue ...




