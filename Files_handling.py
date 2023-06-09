#Python has many built in methods 
#Files can be text files or any binary files , 


f=open('files/myfile.txt','r') #It takes two argument (r- reading,w-writing,a-appending), 'r' mode is the default if you did not pass any argument
#Here is f is an object for file class
print(type(f))  #<class '_io.TextIOWrapper'>  This is the class for files

#To read the file , 
text=f.read() #This will read the whole file content in one go
print(text)  

text=f.readline()   #This reads one single line
print(text)     


text=f.readlines()  #This creates a  list of all indivdual lines and you can easily iterate over this
#print(text)
print(type(text))
f.close() #closes the file

#write(w) 'w' write mode over writes the file when you open the files and write something
#append(a) 'a' append mode also writes into the file but it does not over writes
#create(x) 'x This will create a files, but it throws error if the file already exists
#text(t) 't' 
#binary(b) 'b' used to handle binary files like images pdf etc


#Write methods 
f=open('files/myfile1.txt','w')
f.write("Hello world duehdehudh") #write method writes content into files
f.close()       

f=open('files/myfile1.txt','a')  
f.write("behhedbehdbhedb")
f.close()

#Here manually you are closing the file to let python do this for you ,use the with keyword

with open('files/myfile.txt','w') as f2:  #This will automatically close the file .
    f2.write("Hello India")

#=============some more important methods in file handling==========================
#just like read lines we have write lines
#write lines will write the content one by one
#like readlines writelines does not add new line , therefore you need to add a new line explicitly

lines=['line1','line2','line3']
with open('files/myfile1.txt','w') as f:
    for i in lines:
        f.writelines(i+"\n")
        
#There are some miscellanous mrthods available in python
#seek() and tell() suppose you have myfile.txt , and you have opened in read mode
#to start reading the lines after 10 or 20 or whatever characters use seek()
#f.seek(10)  ,Then from from that line you can read specific character  read() just like before and it can read spefic number of character
#data=f.read(5)  

#tell() function
#f.tel() returns the seek number like seek(10) this 10 value is returned when you call f.tell() method

#f.truncate() , this will truncate the size ,like f.truncate(3)


  












