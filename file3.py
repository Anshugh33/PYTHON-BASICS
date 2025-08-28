# #creating a file and addign data
# file = open("test_data.txt", "w")
# file.write("TC001: Login Test\n")
# file.write("TC002: Search Feature\n")
# file.write("TC003: Cart Feature\n")
# file.close()
# print("File created and data written.")


# #read 
# file = open("test_data.txt", "r")
# print(file.read())
# file.close()

# #APPEND (ADDS DATA IN EXISTING FILE)
# file = open("test_data.txt", "a") 
# file.write("TC003: Payment Gateway\n")
# file.close()

# file = open("try.txt", "w")
# file.write("test1: write a test case\n")
# file.write("test2: make an jiraa acc\n")
# file.write("test3: write bug report\n")
# file.close()

# file=open("try.txt","r")
# print(file.read())
# file.close()

# file=open("try.txt","a")
# file.write("test4: write second test case \n")
# file.close()


#exception handelling
      
# try:
#     num = int(input("Enter a number: "))
#     print(10 / num)
# except ZeroDivisionError: #error aayo vane ya nera aayera bascha
#     print("❌ Cannot divide by zero.")
# except ValueError:
#     print("❌ Invalid input.")
# else:
#     print("division successful")

# finally:
#     print("execution completed")


#MISSING FILE 
try:
    with open("missing_file.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("❌ Test data file not found.")





#ERROR /CRASH id divided by 0
# num=int(input("enter a number: "))
# print(10 / num)




