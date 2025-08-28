#change garna milcha 
list=[1,2,3,4,5]
list[0]=10
print(list)

#change garna mildaina 
tuple1=("sunday","monday","tuesday")
tuple1[1]="wednesday"
print(tuple1)

x=2
y=10
x+=y
print(x)


age=17
if(age>=18):
    print("you are eligible to vote")
elif(age<18):
    print("you are not eligible to vote")


test_status="i dont know "
if(test_status == "passed"):
    print("test passed")
elif(test_status== "failed"):
    print("test failed")
else:
    print("test status unknown")

#elif implementation
lunch="burger"
if(lunch=="momo"):
    print("im hungry")
elif(lunch=="pizza"):
    print("im not hungry")
else:
    print("are you hungry?")

#elif implementation
price=66
if(price==40):
    print("no discount")
elif(price >=50):
    print("discount provied") 
else:
    print("whats the price?")


#list out garcha 
list1=["apple","banana","mango","orange","strawberry"]
for list in list1:
  print(list)

#this is implementation of while loop
count=int(input("enter a number:"))
while count <=5:
    print("count is", count)
    count+=1

#list empty cha ki nai bujna lai chai yo logic use garne 
list1=[1,2,3]
if(list1):
    print("list is not empty")




