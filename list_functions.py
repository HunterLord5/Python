tibil = ["Employees", "Systems", "Management", "HR"]
numbers = [12, 65, 543, 32, 76, 21]
num = []
print(numbers)
print(numbers[2])
print(min(numbers))
print(max(numbers))
print(len(numbers))
print(tibil[1:5:2])
print(numbers[::-1])
print(tibil[::-1])
numbers.sort()
print(numbers)
numbers.append(65)
num.append(12)
num.append(23)
print(numbers)
print(num)
num.insert(1, 62)
print(num)
numbers.remove(76)
print(numbers)
numbers.pop()
print(numbers)

#TUPLES

tp = (1, 32, 54)  #tuples are indicated through parenthesis;  Tuples are immutable
print(tp)
#  p[1] = 8       # This will throw an error  as tuples are immutable

# SWAPPING WAS NEVER BEEN SO EASY AS IN PYTHON.  WITNESS THE BELOW CODE

a = 1
b = 8

"""temp = b
b = a
a = temp
print(a, b)"""      # Normal way

a, b = b, a         # This is the python way to implement swapping
print(a, b)
