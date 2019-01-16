var1 = 43
var2 = int(input())

if var2>var1:
    print("Var2 is greater")

elif var2 == var1:
    print("Equals")

else:
    print("var1 is greater")

list1 = [4, 8, 17]
if 4 in list1:
    print("Yes 4 is in the list")
if 12 not in list1:
    print("No its not in the list")


#Quiz

print("Enter the age of the person")
age = int(input())
if age>6 and age<90:
    if age>18:
        print("You are eligible for driving")
    elif age == 18:
        print("Can't decide, visit and check your eligibility")
    else:
        print("you are not eligible for driving")
else:
    print("Enter your real age")