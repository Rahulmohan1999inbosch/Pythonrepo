#OS module is used to automatae the command line
import os
#print(dir(os))
#os.mkdir("./../data") 
if (not os.path.exists("./../data")):  #checks if the directpry exists
    os.mkdir("./../data")
for i in range(100):
    os.mkdir(f"./../data/day{i+1}") #makes the directory


#Os is a very vast module and you can google a lot of  os modules are available
#os.rename is also one scuh module


folders=os.listdir("./../data") #lists all the folders and stores in folder varible
for i in folders:
    print(i)
  