#Try and except is called errer handling ,errors are always populated in programs 
# try:
#     number=input('enter a number')
#     print(int(number))
    
# except Exception as e:    # except:                 
#     print(e)                    #print('this is one me way of writing except block)

# print('end of programs')

#Try and exception is very useful block

#Different types of handling errors by adding multiple except

# except ValueError # when there is a number gets caught in value error
# except IndexError  #This we get in index error


#This is a  code for index error handling

l=[1,2,4,5,6]
def func():
   #Finally block has one more feature if the try block has return or if it goes inside catch block for return finally is still executed 
   #This is one more most significant use of finally block
   #Because as we know once return is encountered , nothing below is the return is considered but when you use finally block neverthe less
   #it is always executed this is the most important concept so remember it.

  try:
    for i in range(len(l)+1):
      print(l[i])
      return

  except IndexError:
    print('Index is out of the range') 
    return 0
    
      #This will catch index out of range error
  finally:
    print("I'm always executed")
  #Finally block is used when never the less except blocked is executed or not finally block always gets executed . or can also be used for cleaning purpose.

func()



