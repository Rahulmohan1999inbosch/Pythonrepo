#Regular expressio is very useful while string for complex matching ######
import re #regular expression module
pattern=r"[A-Z]yclone"  #r"<string>" means raw string it takes takes the characters as it is like \n will not be treated as  new line
text="Adipurush (transl. First man)[a] is an upcoming Indian Rahul  epic mythological film based on the Hindu epic Ramayana.[6] The film is written and directed by Om Raut and produced by T-Series and Retrophiles. Shot simultaneously Ryclone in Hindi and Telugu languages, the film stars Prabhas, Kriti Sanon, Saif Ali Khan, Sunny Byclone Singh and Devdatta Nage."
match=re.search(pattern,text) #This is the templaate to use a regular expression using the "search  method"
#Search method only sees the forst occurance and if matched returns match , and does not look for any other occcurance,

print(match)
if match:
    print("yes")

match1=re.finditer(pattern,text)  #Gives alll the matches 
for i in match1:
    print(i)

#Regular expression complete tutorial on the way

##########################Comprehensive course on regular expression###############################################
#Regular expression in pyhton is inspired from python

#Compiling regular expression

#Unicode is like ascii character unlike ascii uicode range is quite wider than ascii in ascii we grt 0-255 range where as in unicode we get much higher range
pattern=re.compile("hello")
print(type(pattern) )

pattern=re.compile("Hello",flags=re.I)  #re.I flag will ignore the case sensitive part
print(pattern)

#Perfroming matching
#four methods used for matchig


#match() function
#This checks the match only at the beginiing
#match("text",pos="start_index of text",endpos="end_index of text") default for pos =0 and endpos=infinite
pattern=re.compile("hello") #creating pattern
match=pattern.match("hello world") #text in which we search our match
#returns a match object is match is found 
print(match.span())  #(0, 5) span method returns the index of match in the text

print(pattern.match("rhelloedbededed",pos=1)) #pos and endpos specify the range of match


#search function search("text",pos,endpos)
#here match is checked throughout the text
print(pattern.search("say hello ejdeded hello").span())  #(4, 9) matches only the first occurances  and pos and endpos is for range

#findal("text",pos,endpos)
#Finda all the non overlapping patterns, and returns the list of matched objects
print(pattern.findall("hello deded hello ijdehello"))  #['hello', 'hello', 'hello'] Returns a list

#finditer(text,pos,endpos)
#This will returns a 
match=pattern.finditer("hello hb hellojedjedjnejd hello")
print(type(pattern.finditer("hello hb hellojedjedjnejd hello"))) #returns <class 'callable_iterator'> you can iterate over this , this return the match objects.
for i in match:
    print(i)
# <re.Match object; span=(0, 5), match='hello'>
# <re.Match object; span=(9, 14), match='hello'>
# <re.Match object; span=(26, 31), match='hello'>

#onem more way of doing this is in the module level
re.findall("hello","say jendjedjen hello jned hello") #this is another way of doing things



#important examples
#search for $15 in the text 
txt="This book costs $15"
pattern=re.compile("\$15")   #use \ charecter followed by special character
print(pattern.search(txt)) #none because $ is special character so use escape character
print(pattern.search(txt).span()) #Now you get the match characters

#There are overal  of 12 meta charcaters 
#The backspace escape character \\ you can use a double \
pattern=re.compile("C:\\Windows\\System")
print(pattern.search("C:\\Windows\\System")) #you get none This is because \\ is taken as single \ by the python interpreter so here you need to do double escaping

#There fore you should your search pattern
txt="C:\\Windows\\System"
pattern=re.compile("C:\\\\Windows\\\\System")
print(pattern.search(txt))  #<re.Match object; span=(0, 17), match='C:\\Windows\\System'> Now you get the output

#putting these \\ is very messy,this is back slash plageue

#Raw string
print(r"ed\jd\\dend\\dndk\\\n") #ed\jd\\dend\\dndk\\\n This is very important
pattern=re.compile(r"C:\\Windows\\System")
print(pattern.search(txt)) #This works 
#raw string is sufficient to handle all these matchings

#================================================back slash pleague end===========================================================================

#Character classes 
# [cs]==>c or s
#[0-9] means 0 to 9, [A-Z] [a-zA-z0-9] means a to z A to Z or 0 to 9
text="ejdhededh 1999 duedueudud deded 2013 eduedede 3456 ejdedjedjejdje ehduehdehddhebdhbhdey 2018"
#Write a regex to match the dates
pattern=re.compile("[0-9][0-9][0-9][0-9]")  
print(pattern.findall(text)) #['1999', '2013', '3456', '2018']

#negating 
#this is perform the oppiste of 
# [^A-Z] except A to Z,[^0-9]

#find all the characters used in the text except vowels
pattern=re.compile("[^aeiou]")
print("".join(pattern.findall(text))) #join syntax "<character you want to used to join>".join(listname)

#predefined character classes
# . => match any character except \nonlocal
# \d =matches digit 
# \D =match except digit
# \s=matches white space character [\n\t\r] 
# \S= non white space characters
# \w=matches alphnumeric [A-Za-z0-9]
# \W=non alphanumeric

#imroved pattern
pattern=re.compile("\d\d\d\d")
print(pattern.findall(text))  #['1999', '2013', '3456', '2018']

############################################Alteration###################################################################################
txt="jednejdn and jndjendjor the ebdhebdhbed"
pattern=re.compile("and|or|the") #to match the complete word and | is or operator
print(pattern.findall(txt))  #['and', 'or', 'the']


txt="""
What is your name?
Who is that guy?
"""
#match what is and who is 

pattern=re.compile("What is|Who is")
print(pattern.findall(txt))  #['What is', 'Who is']

####################################Qunatifiers ####################################################################
#to specify the number of times the repeatation will happen
#This apply's on the preceeding characters

#find the matching for dog or dogs
text="xjxjnejnxnenxjnkd dog ededed dogs dedeiodijdijjddog uduhdudhdogs"
pattern=re.compile("dog|dogs")
print(pattern.findall(text)) #['dog', 'dog', 'dog', 'dog'] This is not matching the dogs since dogs has dog in it , it considers dog and goes for the next one 

pattern=re.compile("dogs?")# s can be repeated 0 or 1 time
print(pattern.findall(text)) #['dog', 'dogs', 'dog', 'dogs']

#find the files that ends with .txt
files="""
fileuhdi.txt
fileediejdi1.txt
file4.txt
file.xml
file5.py
"""

#* means 0 or many occurances, the preceeding character can occur 0 or mutiple times
pattern=re.compile("file\w*\.txt")   
print(pattern.findall(files))

# + means one or more occurance of the precedin character

#Curly bracket syntaxes {}
#{n} exactly n repeation {n,}atleast n times {,n}atmost n times {n,m} 

txt="doedededi 2013 idjeijdiej 1999 jiejdiejd 2015 eddedi 1978 123 3444454545 "
pattern=re.compile("[1-9]\d{,3}")
print(pattern.findall(txt))  #['2013', '1999', '2015', '1978']

#New Exercise ####################################################
txt="""
555-555-5555
555 555 5555
5555555555
"""
#Wriite a pattern to match all these formats
pattern=re.compile("\d{3}.?\d{3}.?\d{4}")
print(pattern.findall(txt)) #['555-555-5555', '555 555 5555', '5555555555']


###############Greedy and non greedy behaviour#######################################
txt="""<html><head><title>Title</title>"""
pattern=re.compile("<.*>")  #our aim is to get <content> as we parse it
print(pattern.findall(txt)) #['<html><head><title>Title</title>'] This output is due to  the greedy behaviour instaed of givig us <html> it goes all over the string to match 

#Non greedy method
pattern=re.compile("<.*?>") #adding ? makes it non greedy
print(pattern.findall(txt)) #['<html>', '<head>', '<title>', '</title>']


#==================Boundary matches==================================================================================
#suppose you want to match "and" "or" in a text using (and|or) in the pattern but it will match in lorem as it has or in it, we do not want to match way ,instaed we only want to match "and" "or" as a seperate word , 


text="lorem dheh and jebdj or andani idied lorems oranges"
#\b is a meta character to add boundary \b<content>\b
#\b will be taken as escape sequence for boundary so use \\b \\b
pattern=re.compile("and|or|the")   
print(pattern.findall(text))  #['or', 'and', 'or', 'and', 'or', 'or'] gives all words that has or or and in it

#if you want to match the exact wodrd use boundary

pattern=re.compile("\\b(and|or|the)\\b")  #['and', 'or']
print(pattern.findall(text))


#####################List of boundary matches######################
# ^hello =>text that starts with hello
# hello$=>matchs if the line is ending with hello
# \B =>opposite of \b

text="""
Name: Rahul
Age:89
Grade:S

Name: RAshmi
Age:92
Grade:Splus

Name: Lifi
Age:17
Grade:F
"""

#print the content that starts with Name: 
pattern=re.compile("^Name: .",flags=re.M) #flag re.M tells regex to see multi line by default regex takes single line
print(pattern.findall(text))  #['Name: ', 'Name: ', 'Name: ']

####################spli using Regex######################################
#split function
txt="""
Beautiful is better than ugly
Explicit is better than implicit
Simple is better than complex
Complex is better than complicated
"""
pattern=re.compile("\n")
print(pattern.split(txt)) #returns a list ['', 'Name: Rahul', 'Age:89', 'Grade:S', '', 'Name: RAshmi', 'Age:92', 'Grade:Splus', '', 'Name: Lifi', 'Age:17', 'Grade:F', '']

pattern=re.compile("\W") #based on the non alphanumeric values
print(pattern.split(txt))  #let us filter out the space elements
print(list(filter(lambda x: x!=" ", pattern.split(text) )))

#split(txt,max=3) max means max number of splits you want to perform


#####################very important regex for substitution####################################################
#sub("replacement",txt)
txt="100 cats, 23 dogs, 3 rabbits"
pattern=re.compile("\d+")
print(pattern.findall(txt))
print(pattern.sub('-',txt))


#subn(replacement,txt) gives the number of substitution 

text="This$#is% Matrix#  %!"

#This is Matrix#  %!

pattern=re.compile("\w\W\W\w")
l1=pattern.findall(text)
print(l1)
x=""
print("=============")
x=text.replace(l1[0],l1[0][0]+" "+l1[0][-1])
y=x.replace(l1[1],l1[1][0]+" "+l1[1][-1])

for i in l1:
    temp=text.replace(i,i[0]+" "+i[-1])
    text=temp

print(text)

#============compilation flags==============================#
#these are the flasg which we can pass to modify the compilation pattern
#There are 8 different flags
# re.I =>makes case insensitive  
#syntax= re.compile("pattern",flags=re.I# )
#re.M => This is multiline flas=g , by default regex engine considers the entire string this flag changes the engine to multiline

#re.S =>

#re.U this is a default flag 

#================Grouping=====================================================
#To match only some part of the regular expression that can be obtained using grouping  usijg () this paranthesis
print("==================grouping==========================")
txt="abbbbbbbbbbbbbbbbb"
#match the repeation of ab
pattern=re.compile("a(b)+")
print(pattern.findall(txt))

target_string = "The price of ice-creams PINEAPPLE 20 MANGO 30 CHOCOLATE 40"
pattern=re.compile("([A-Z]+).(\d+)")
print(pattern.findall(target_string))


txt="ababababababababab"
#txt="abbbbbbbbbbbbbbbbb"
pattern=re.compile("(ab+)")
print(pattern.findall(txt))

# ['ab', 'ab', 'ab', 'ab', 'ab', 'ab', 'ab', 'ab', 'ab']
# ['ab', 'ab', 'ab', 'ab', 'ab', 'ab', 'ab', 'ab', 'ab']

txt="abccccccccccccccccccccccc"
pattern=re.compile("(abc+)")
print(pattern.findall(txt))


txt="""
my name is ram
my name is sam
"""
#pattern=re.compile("my name is ram|sam")
pattern1=re.compile("\w+ \w+ \w+ \w+|\w+")

#print(pattern1.findall(txt))  #['my name is ram', 'sam']
match=pattern1.findall(txt)
print(match)
txt="12-02-2019"
pattern=re.compile("(\d{2})-(\d{2})-(\d{4})")  #This is how you can capture the elements 
match=pattern.match(txt)
print(match.group(0)) ##12-02-2019
print(match.group(1)) #12
print(match.group(2))# 02
print(match.group(3))#2019

print(match.groups())  #('12', '02', '2019') This returns a tuple 

#Write a regex pattern to extact name from the given text

txt="""
Name: Rahul
Age: 24
Roll: 34
Grade: 1

Name: Rashmi
Age: 24
Roll: 33
Grade: 2

Name: Kavya
Age: 24
Roll: 20
Grade: 3

"""

pattern=re.compile("Name: (\w+)",re.M)
print(pattern.findall(txt)) #['Rahul', 'Rashmi', 'Kavya'] This is one way of capturing elements inside
print(pattern.findall(txt)) #['Rahul', 'Rashmi', 'Kavya']


#Back referncing in python

txt="""
hello hello
how are you 
bye bye
"""
pattern=re.compile(r"(\w+) \1")  #What ever comes inside the ()  makes group if you ()( ) Means you have 2 groups , using raw string in  regex is more preffered
print(pattern.findall(txt))  #['hello', 'bye']

#in the given text below find the match for dd/mm/yyyy and change the pattern to yyyy/mm/dd

txt="""
today is 23/02/2019
yesterday was 22/02/2019
tommorow is 24/02/2019
"""

pattern=re.compile(r"(\d{2})/(\d{2})/(\d{4})")
print(pattern.findall(txt))

print(pattern.sub(r"\3-\2-\1",txt))
# output
# today is 2019-02-23
# yesterday was 2019-02-22
# tommorow is 2019-02-24

##############################Names groups in python###########################
#if you want to refer to a group using name instead of \1 \2 etc

txt="Rashmi Rahul"
pattern=re.compile("(?P<first>\w+) (?P<last>\w+)")  #  (?P<name>w+)
match=pattern.match(txt)
print(match.group('first'))  #Rashmi
print(match.group('last'))   #Rahul

print(match.group(1))     #Rashmi
print(match.group(2))     #Rahul

#both gives you same result ,so like this instead of using the index number you can also use the name in groups

#Swap first and last name
print(pattern.sub(r"\g<last> \g<first>",txt)) #This will swap the first and the last name ,<output>===> Rahul Rashmi


#check if the person has same first and last name
txt="Rahul Rahul"
pattern=re.compile("(?P<first>\w+) (?P=first)")
match=pattern.match(txt)
print(match)   #<re.Match object; span=(0, 11), match='Rahul Rahul'> you got the match


####group dict######################
print(match.groupdict()) #returns in the for of a dictionary {'first': 'Rahul'}



##########Non capturng groups ####################
#syntax (?:pattern)
txt="""
i love cats
i love dogs
"""

pattern=re.compile("i love (?:dogs|cats)")
print(pattern.findall(txt))  #['i love cats', 'i love dogs']  This is the output i have been waiting for
match=pattern.match(txt)
print(match)

##########zero width assertion #############
#^ $ /b all these are zero width asserttion as they don't consume any space 

##############look around#####################
#This will if there is a particular pattern present a particular regular expression and after a regular expression
##<non consuming expression><actula expression><non consuming expression>

                                    #       Look around
                                    #   Look ahead    Look behind
                                    #   +ve   -ve      +ve   -ve


#look Ahed expression
#+ve look ahead
#syntax A(?=B)
txt="i love python, i love regex"
pattern=re.compile("love(?=\sregex)")
match=pattern.search(txt)
print(match) #<re.Match object; span=(17, 21), match='love'>
print(pattern.findall(txt)) #['love']

#find all the words that has , or . suffiexed
txt="My favorite colors are red, green, and blue."
pattern=re.compile("\w+(?=\.|,)")  
print(pattern.findall(txt))  #['red', 'green', 'blue']


###Negative look ahead#####################
txt="i love python, i love regex"
pattern=re.compile("love(?!\sregex)")
print(pattern.findall(txt)) #['love]


#########################################Last lectue in  regular expression#####################################
#syntax (?<=)
txt="love regex or hate regex,can't ignore"
pattern=re.compile("(?<=love\s)regex")
print(pattern.findall(txt))  #['regex']


#Negative look behind (?<!)


#############################################Regex completed##############################














