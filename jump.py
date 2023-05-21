# Today we will be learning on break and continue statement
for i in range(1,11):
    if i ==10:              #if i value is 10 loop is broken and we come out of the loop
        print('im breaking')  
        break
    print(i)

# Similarly we do it for contiue but there is a slight change when we do it with cotinue, continue statement only skip that particular iteration based on condition

# Example for continue statement
for i in range(12):
    if i==5:                   # In this example when the value of the i reaches 5 the loop is skipped
        
        continue
    print('value of i is',i)
  
