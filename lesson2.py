try:
    if name <3:
        print("hello world")
except:
    print("oops! Something went wrong")

# Create function
def name():
    print("Enter your name:")
    name = input()
    print ("Hi,",name)
name()

def addition(a,b):
    print("The addition is :",a+b)
addition(12,15)

def returnadd(num1,num2):
    return(num1+num2)
sum=returnadd(32,41)
print(sum)
