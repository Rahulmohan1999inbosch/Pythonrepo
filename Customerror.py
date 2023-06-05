#Today we will be learning about custom errors
a=int(input('enter any value between 5 and 9:-'))
if a<5 or a>9:
    #here you can rasie value error
    #some errors are handled by pyhton ,an we can create our own custom errors like this
    raise ValueError('Value should be between 5 and 9')

name=input('enter a name')
if name!='Rashmi':
    raise ValueError('Only Rashmi is eligible Rahul heart')
else:
    print("Rashmi has eneterd Rahul's heart congratualations")