print("===============================================\nWelcome to KBC\n===============================================")
Name=input("Please enter your name-->")


questions={
  'What is the Capital of India??'  :"Delhi",
  'Which is the national bird of India ??':'peacock',
  'What is sin(a)/cos(a) ???':'tan(a)'
}

Amount=0
initial=0
options=[['Delhi','Bagalore','chennai','Mumbai'],
        ['peacock','parrot','crow','pegion'] ,
        ['sin(a)','tan(a)','sec(a)','cosec(a)'] ]

for question in questions.keys():
    print(question)
    print('your options are')
    print(options[initial])
    answer=int(input('please enter your options as index place between 0 to 4:-'))
    if questions.get(question) == options[initial][answer]:
        print("===============Right Aswer=====================")
        Amount+=1000
    else:
        print('**************Wrong Anwer**********************')
        break
    initial+=1

print(f"Thank you {Name} for beigh part of KBC\n your take home amount is ========>{Amount}")




    

