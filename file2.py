# def greet():
#     print("hello form file3.py")

# greet()



#function with parameter
# def greet_user(name):
#   print("hello",name)

# greet_user("ram")



#taking input form user 

# def greet_user(name):
#     print("hello",name)
# name=input("enter your name:")
# greet_user(name)



#TAKE AGE AND NAME INPUT FROM USER yesma f vaneko string formatting

# def greet_user(name,age):
#     print(f"hello {name},you are {age} years old") #print vitra f lekheko ani parmeter pass gareko 
#     print(type(age))

# name=input("enter your name:")
# age=input("enter your age:") #data type int ho but str nai lirako huncha 
# greet_user(name,age)




#add 2 numbers 
# def add(x,y):
#    return x+y

# result=add(2,4) #parameter aafai pathako 
# print(f"your result is {result}")




#DIFFERENCE 
# def diff(x,y):
#    return x-y

# result=diff(4,2) #parameter aafai pathako 
# print(f"your result is {result}") 


#built in function


# import math
# print(math.e)

# list1=[1,2,3,4,5,6,7,8,]
# print(len(list1)) #length count 
# print(max(list1)) #largest number
# print(sum(list1)) #sum of list 

#function banayera loop lagako 
# def implement():
#     days=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
#     for day in days:
#         print(day)
# implement()

#simple game by using all that we learnt 

# import random/some error dosnt show try again 

# def random_game(): #create function
#     number=random.randint(1,5) 
#     userguess=None
#     while(number!=userguess):
#       userguess=int(input("guess a number between 1 and 5: "))
#     if(number==userguess):
#         print("congratulations! you guessed the number")
#     else:
#         print("try again")
# random_game() #call function




#correct shows try again 
# import random

# def random_game():
#     number = random.randint(1, 5)
#     userguess = None
#     while userguess != number:
#         userguess = int(input("Guess a number between 1 and 5: "))
#         if userguess == number:
#             print("Congratulations! You guessed the number.")
#         else:
#             print("Try again")

# random_game()





