# slicing on list
import copy
name=[['rohan' ,'sohan'],["anant","ravi","kavi","suraj"]]
# for i in range (len(name)):
#     print(str(i)+"."+name[i])
# for index ,item in enumerate(name):
#     print(str(index+1)+"."+item) 
# person1,person2,person3,person4=name
# print(person2)
# x=name.append("shiv")
# print(x)
# name.remove("kavi")
# name.clear()
# print(name)
house=copy.deepcopy(name)
del name[0][0]
print(house)
print(name)
print(id(name))
print(id(house))
