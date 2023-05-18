# Switch case statement similary in python we use match
# we can take an exapmple to do few things in our program
age =int(input('enter the value of x'))

match age:
    case 10:
        print('heu')
    case 18:
        print('you can have sex')

    case _ if age>78:                   # case_ is default in python you can also add if condition in the default statement in python
        print('sorry')

    case _:
        print('hey how you doing')


    
    

        
    