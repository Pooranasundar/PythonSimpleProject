from array import *

print("Welcome to Student Percentage Calculator")

subLen = int(input("Enter Total number of subject : "))
arr = array('i', [])

for i in range(subLen):
    a = int(input("Enter Your Value : "))
    arr.append(a)

totalsum =0

for z in range(arr.__len__()):
    totalsum += arr[z]
    
percentageCal = totalsum/subLen

print("Total Mark is : ",totalsum, "And Your Percentage is : ",percentageCal,"%")
