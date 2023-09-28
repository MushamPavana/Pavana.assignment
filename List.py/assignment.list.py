#remove duplictes
list = [2,6,8,9,55,4,3,9,55,90,888]

result=[]
for i in list:
    if i not in result:
        result.append(i)

print(result)

list = [24,45,90,87,54,65,24,99,54,45,27,65]

result=[]
for i in list:
    if i not in result:
        result.append(i)

print(result)        

# to find list of elements 
list = [10,20,30,40,50]
sum=0
for i in list:
    sum=sum+1
print("sum of list is:" ,sum) 

#to merge two lists
class1 = ["pavana","shirisha","laxmi"]
class2 = ["naree","srinu","madhu"]
class1.extend(class2)
print(class1)

student = ["yeshu","sneha","shraddha"]
marks = [80 , 60 , 85]
student.extend(marks)
print(student)

#list of multiple integers into single integers
list = [101,202,303]
print("original list:",list)
X = int("" .join(map(str,list)))
print("single integer:",X)

list = [56,90,888]
print("original list:", list)
Y = int("" .join(map(str,list)))
print("single integer", Y)


#to delete given element from the list
list1 = [20,30,50,60]
del list1 [1]
print (list1)

list2 = [444,66,80,67]
del list2 [0]
print (list2)

#to print even and odd numbers separatly in the list
list = [2,1,5,57,64,34,3,6,52,56]
for i in list:
    if(i%2==0):
        print(i,"is even")
    else:
        print(i, "is odd" )

list =[23,45,78,56,90,123,509,34,29]
for i in list:
    if(i%2==0):
        print(i, "is even")
    else:
        print(i, "is odd")

# to delete element of given index in the list

workdays =["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
workdays.remove("sunday")
print(workdays)        

list= ["shreya","shruthi","vinod"]
list.remove("vinod")
print(list)

# to insert an element at given index location
fruits = ["apple","banana","orange"]
fruits.append("dragonfruit")
print(fruits)
fruits.insert(1,"grape")
print(fruits)

vegetables = ["tomato","corrindar","beans"]
print(vegetables)
vegetables.insert(2,"bringal")
print(vegetables)
   
#to check the size of the given two list are same
X = [11,22,33,44]
Y =  [33,44,55,66]
result = False
for x in list1:
    for y in list2:
        if(x==y):
            result=True
print("list have common elements") 

list1 = [12,13,14,15,16]
list2 = [10,11,12,13,14]
result = False
for x in list1:
    for y in list2:
        if(x==y):
            result=True
print("list have common elements") 

#function that takes to lists an return true if they have atleast one common member
list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9]
for x in list1:
    for y in list2:
        if(x==y):
            print("true")

x = [22,33,44,55,66]
y = [11,44,77,55,22]
for x in list1:
    for y in list2:
        if(x==y):
            print("true") 