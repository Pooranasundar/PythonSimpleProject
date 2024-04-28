print("Welcome to Calculator")

num1 = int(input("Please Enter your First Value : \n"))
num2 = int(input("Please Enter Your Second Value : \n"))
print("1.Addition\n2.Subraction\n3.Multiplication\n4.Division\n5.Modulo")


opration = int(input("Please Select your Operation : \n"))

if(opration == 1):
    print("Your Addition Value is : ",num1 + num2)

elif(opration == 2):
    print("Your Subraction Value is : ",num1 - num2)

elif(opration == 3):
    print("Your Multiplication Value is : ",num1 * num2)

elif(opration == 4):
    print("Your Division Value is : ",num1 / num2)

elif(opration == 5):
    print("Your Modulo Value is : ",num1 % num2)

else:
    print("Invalid Value")


