# Dictionary are very useful , in dictionaries we can go key and value pair
# This is a basic dictionary 
dic={'Brock lesnar':'mma',
    'Roman Reigns':'wwe superstar',
    'conor':'ufc superstar',
    'Rahul':'Full stack web developer'
     }

#To access the dictionar use the key of the ductionay
print(dic['Rahul']) #Full stack web developer accssing is similar to list or tuple just use the square brackets

#.get()
print(dic.get('Roman Reigns')) #wwe superstar
#Advantage of using get method is if the key is not present you None as return but in [] it returns error

#from python 3.7 onwards dictinaries are ordered

print(dic.keys()) #This returns all the keys in the form of a list
for i in dic.keys():
    print(i) 

#You can get similar output by running this
for i in dic:
    print(i)

#To get all the values
print(dic.values()) #Returns a list of values

#Lets make a small code print the key and value pain in dictionary
for i in dic.keys():
    print(f"{i}-------->{dic[i]}")

for i in dic.values():  # you cam iterate along the values and print it
    print(i)

#To get all the key pairs
print(dic.items()) #dict_items([('Brock lesnar', 'mma'), ('Roman Reigns', 'wwe superstar'), ('conor', 'ufc superstar'), ('Rahul', 'Full stack web developer')])

#To iterate on this
for key,value in dic.items():
    print(f"{key}              =====>{value}")


########################Dictionary methods###################################
#update
employeeid={'Rahul':10,'sagar':20,'Rashmi':'45','Kavya':99}
employeeid.update({'Rohna':45,'Roman':467})
print(employeeid) #{'Rahul': 10, 'sagar': 20, 'Rashmi': '45', 'Kavya': 99, 'Rohna': 45, 'Roman': 467} 

#clear method
#print(employeeid.clear()) # clears the dictionary
empt={} #Emplty dictionary

#pop method
print(employeeid.pop('Rahul')) # Add the key, Thus will pop the value
print(employeeid) #And the key value pair is also removed from dictionary

#popitem() This will pop the last key value pair in the dictionary and that key value pair is removed

print(employeeid.popitem())
print(employeeid)  #{'sagar': 20, 'Rashmi': '45', 'Kavya': 99, 'Rohna': 45}


#Delete
# del employeeid this will delete the entire dictionary

#if you want to delete any specifi key value pair
del employeeid['sagar']
print(employeeid) # sagar key value entry is gone

#You can go through documentation and learn more on dictionary

