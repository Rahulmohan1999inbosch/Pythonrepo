Fruits={1:"Apple",2:"Banana",3:"orange"}
#print(Fruits)
for i in range(4,7):
    Fruits[i]=input("enter some fruits name:-")

for i in Fruits.keys():
    print(i,"----->"+Fruits.get(i))
