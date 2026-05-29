#string rules-
#1- sequence of character written inside quotes,
#2- includes letters,numbers,and spaces
#3- string are immutable /unchanged
#4- but we can manipultaes strinf -use method like concatation ,slicing,formatting to create new string
#5- deleted entire sting varibale (pyhton not possible to delet individualcharater)

# a= 'hello'
# print(a)

# b="hello how are you"
# print(b)

# c='''hey how you
# sb badiya 
# main theek hoon'''
# print(c)

# name = "sapna"
# print("My name is : - ",name)

# print("type of my variable :-",type(name))  #type function type check krne k liye
# print("len of my stirng:-",len(name)) #no of char count k liye
      
# upper_case =name.upper()
# print("upper case :-",upper_case)   #upper is used to convert string into capital letter
# lower_case =name.lower()
# print("lower case :-",lower_case)      #lower is used to convrert string into small letter
       
# name = "riya"
# print(name.casefold())  # in lowercaae
# name = "riya"  
# print(name.title())   #first letter of characer in capital
# name ="riya"
# print(name.capitalize())   #fisrt letter of character in capital

# #task ques 1:- differnce between lower and casefold
# a="Straße"
# print(a.lower())
# A="Straße"
# print(A.casefold())
# #lower is used to convert string into small letter and casefold conert into samll letter(but dusre language k lletter ko phle english m change krta h fir small m krega)

# #ques:2- differnce betweentitle and capatalize()
# a = "hello world"
# print(a.title())
# print(a.capitalize())
# #title convert first letter of every word to uppercase but capitalise conert only fisrt letter of string 

# #ques 3:- different way to revese a string inpython
# #method1 - negative indexing
# m="muskan"
# print(m[: : -1])
# #reverse krne ka fastest way h indexing jo stieng reverse krke detah

# #method2 reversed() function using join 
# a="python"
# b= join(reversed(a))
# print(b)

# company_name = "upfalirs"
# print(len(company_name))
# print(company_name.strip())
# print(len(company_name))
#  #intro " hello  hii kese  ho"  ###task3


#  #indexing slcing

# name ="muskan dwivedi"
# print(name[3])    #indexing
# print(name[2:5])   #slicing

# company_name = 'upflairs'
# print(company_name[0])
# print(company_name[7])
# print(company_name[-1])

# print(company_name[0:3])

# #company_name     task4 reverse the string

# name ="ritik"
# last_name ="kumar"
# print(name + " " + last_name)

# str1 ="hi"
# str2 ="hello"
# #print(str1*str2)  #cant multiply sequenc by non int of type "str"
# print(str1 + str2)       #to give space str1 k bad whitespace de skte h or str2 s phle whitespce bhi de skte h
# #print(str1 + 2)
# print(str1 * 2)

# #name ="dev"
# #name ='dev       #ques 5 what is the difference bw them

# intro ="i am girl"  
# print(intro.split())

# intro ="i am girl"
# a=intro.split()
# print(a)

# #ques4;- strip() method can remove spaces btw words inside a strimg?
# a="  hello   good morning   "
# print(a.strip())
# #no strip( ) method dose not remove spaces beteen word inside a string only lest right(age piche spCE) ko hatata h


# name = "Govind"
# address = "jaipur"
# print(f"my name is {name} and i from {address}")    #f function is used to give variable inside string


# #input function is udse to take values by user
# name =input("enter your name :-")
# print(name)
# print(type(name))


# #int is used to define typecasting    ### by default it is stringss
# no1 =int(input("enetr fisrt number:-"))
# no2 =int(input("enter second number:-"))
# print(no1 + no2)
# print(type(no1))
# print(type(no2))
