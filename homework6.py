my_dict={"Denis":1997,"Ivan":1989,"Artem":1993}
print(my_dict)
#словарь
print(my_dict["Denis"])
my_dict["Elena"]=1996
print(my_dict["Elena"])

print(my_dict)

my_dict.update({"Sasha":1990,"Alisa":2019})
print(my_dict)



a=my_dict.pop("Denis")
print(a)
print(my_dict)

#множества
my_set={1,1,2,2,3,3,4,4,True, "mouse",(1,2,3)}
print(my_set)

my_set.update({5,"cat"})
print(my_set)

my_set.discard((1,2,3))
print(my_set)