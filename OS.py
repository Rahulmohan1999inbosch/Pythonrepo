#OS module is used to automatae the command line
import os
#print(dir(os))
#os.mkdir("./../data") 
# if (not os.path.exists("./../data")):  #checks if the directpry exists
#     os.mkdir("./../data")
# for i in range(100):
#     os.mkdir(f"./../data/day{i+1}") #makes the directory


#Os is a very vast module and you can google a lot of  os modules are available
#os.rename is also one scuh module


folders=os.listdir("./../data") #lists all the folders and stores in folder varible

#our new exercise is to explore os module commands

######################## This session advance session on os ##################################3

print(os.getcwd()) #D:\python
print(os.listdir())

#how to change your current working directory
#os.chdir(r"") #this will chabhe the current working directory

for root,directory,files in os.walk(os.getcwd()):
    #print(root) #gives all the root directory
    print(directory) #give all the directories 
    print(files)
