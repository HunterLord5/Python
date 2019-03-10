#FAULTY CALCULATOR

print("Ener the first number")
num1 = int(input())
print("Enter the second number")
num2 = int(input())
print("Enter the operator in order to perform the operation")
op = input()
if(num1==45 and num2==3 and op=='*'):
    result = 555
elif(num1==56 and num2==9 and op=='+'):
    result = 77
elif(num1==56 and num2==6 and op=='/'):
    result = 4
else:
    if op == '+':
        result=num1+num2
    elif op == '-':
        result=num1-num2
    elif op == '*':
        result = num1*num2
    elif op == '/':
        result = num1/num2
    else:
        print("Enter the correct values")
print("The result is: ", result)
print()
