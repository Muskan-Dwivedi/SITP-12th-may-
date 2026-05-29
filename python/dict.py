#dictionary
student={"name":"muskan",
         "class":"third yaer",
         "branch":"cse",
         "roll no":21,
         "address":"jaipur"}
#name , calss roll no branch ,address >>>>keys    key should be unique
#musakn third year cse 21 jaipur>>>>k]values      it can havw duplicate value
#key + value = "item"
# print(student)
# print("dict keys",student.keys())
# print("dict value",student.values())
# print("dict item",student.items())

# print(student["name"])   #valuse od indivudaual key
# print(student["class"])
# print(student["branch"])

# #add
# student["subject"]="pyhton"
# print(student)
# #task usee append 
#task use from key

# print(student.get("name"))   #get function givethe value of key
# print(student.copy())        #coppy the same the dictionary
# #print(student.clear())
# print(student.pop("name"))    #pop the particular index item
#print(student.popitem())   #pop the last item


# car={"brand":"ford",
#      "modal":"mustang",
#      "year":2023}
# # print(car)
# # x= car.setdefault("color","white")     #
# # print(x)


car={"brand":["ford","honda","hero"],
     "modal":"mustang",
     "year":2200}
print(car) 

# car["year"]=2006 #updation without any update
# print(car)

#for loop
for x in car:
    print(x)
for x in car.items():
    print(x)
for x in car.keys():
    print(x)
for x in car.values():   
    print(x)