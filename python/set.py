#set    unordered and mutable
s={1,3,2}
print(s)
print(type(s))
print(len(s))



s= {"hi","hello"}
s.remove("bh")     #it will give erroe oif we give any other value rather then values in set
#s.discard("hi")  #difference btw remove and discard in that>>> remove will show error if values is not presnt in set but discard will not show errer if vzlue is not present in set
print(s)

s.discard("df")