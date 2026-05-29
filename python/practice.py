# a = "hello good       morning"
# print(a.strip())
# #strip does not remove between string \.....ony remove left and right space...means age piche
# a ="hello good morning   " 
# print(len(a))
# b=a.strip()
# print(len(b))


# a="hello good morning"
# print(a.split())
# #split....string ko split krta ha single singlrn string m and ans list m ata h

# a="muskan"
# print(a.upper())
# print(a.lower())

# # a = (input("enter your name:"))
# # b = (input("enter your course name:"))
# # c = (input("enter your city:"))
# # print("your name is:",a)
# # print("your course name:",b)
# # print("your city:",c)

# name = (input("enter your name:"))
# age = int(input("enter your age:"))
# print(f"Hello {name}, you are {age} year old")


# name = input("enter a string:-")
# print(name)
# print(name[ : : -1])
# print(len(name))

# a = 10       #integer
# b = 4.6       #float
# c = "muskan"   #string
# d = True       # boolean
# e = [1,2,3]    #list
# f = (5,6,7)    #tuple
# g = {"name" : "muskan" }   #dictionary
# h = 2 + 4j                 #complex
# i = {1,2,3}                #set
# print("Integer number:-",a)
# print("float number:-",b)
# print("string:-",c)
# print("boolean value:-",d)
# print("list item:-",e)
# print("tuple value:-",f)
# print("dictionary value:-",g)
# print("complex number:-",h)
# print("set value:-",i)

# a = input("enter a string:")
# print(a.upper())
# print(a.lower())
# print(len(a))
 
# a = [2,3,4,5,6]
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])

# a = "Good Morning "
# b = "Hello, how are you"
# c = a + b 
# print(c)

# student_name = ["Muskan","Garima","Swati","Priya"]
# student_name.append("Priyanshi")
# print(student_name)

#assignemt 4
# a = 12
# b = 12.3
# c = "hello"
# d = True
# e = [1,2,3]
# f = (1,2,3)
# g = {"name":"muskan"}
# h = {1,2,3}
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)
# print(h)
# print(type(a))
# print(type(b))
# print(type(c)) 
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(g))
# print(type(h))
#list operation
# lst = [1,2,3,6,8,3,9,4]
# lst.append(4.6)
# print(lst)
# lst.remove(2)
# print(lst)
# print(lst[2::2])
# print(lst[::-1])
# print(lst[0:5:2])
#  #tuple indexing
# tup = (1,3,5,2,6,4)
# print(tup[4])
# print(tup[2])
# print(tup[5])
# sat1 = {1,2,3,4}
# sat2 = {3,4,5}
# print(sat1.union(sat2))
# print(sat1.intersection(sat2))

# dict = {"name":"Muskan","branch":"cse","address":"jaipur"}
# print(dict)
# print(dict.keys())
# print(dict.values())
# print(dict.items())

# student = {"name":["muskan","swati","priya","garima"],
#            "roll no":[1,2,3,4],
#            "subject":["GK","Hindi","SST","english"],
#            "address":["jaipur","sikar","jhunjhunu","tonk"]}
# student_marks = [32,24,42,27]
# print(student_marks)
  


class PrimeNumberChecker:
    def prime(self):
       for x in range(1,11):
          if x>1: 
             for i in range(2,x):
               if x%i ==0:
                    break
               else:
                  print(x)
               
a = PrimeNumberChecker()
a.prime()

