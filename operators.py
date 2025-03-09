# class Assignment No 02

# In python, an operator is a symbol that performs an operations on one or more operands.

# there are several types of operators in python:

# 1- Arithmetic operators
# 2- Assignment operators
# 3- Comparison operators
# 4- Logical operators
# 5- Identity operators
# 6- Membership operators
# 7- Bitwise operators




# - Arithmetic Operators: 
# Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, etc.
# 1- Addition (+) add two operands
a = 5
b = 4
result1 = a + b
print(result1) # 9

# 2- Subtraction (-) subtract two operands
result2 = a - b
print(result2) # 1

# 3- Multiplication (*) multiply two operands
result3 = a * b
print(result3) # 20

# 4- Division (float) (/) divide two operands
result4 = a / b 
print(result4) # 1.25

# 5- floor Division (//) divide two operands but removes decimal
result5 = a // b
print(result5) # 1 

# 6- Exponentiation (**) raise a number to the power of another
result6 = a ** b
print(result6)  # 625

# 7- Modulus (%) returns the remainder of the division of the two operands
result7 = a % b
print(result7) # 1






# - Assignment Operators:
# Assignment operators are used to assign values to variables.

# 1- Assign (=) Assigns operator is used to assign value right to left side of variable
c = 10
d = 15

# 2- add and assign (+=):
c += 5
print(c)  # 15

# 3- subtract and assign (-=):
c -= 7
print(c)  # 8

# 5- multiply and assign (*=):
c *= 2
print(c) # 16

# 6- divide and assign (/=):
c /= 5
print(c) # 3.2

# 7- floor divide and assign (//=):
d //= 6
print(d) # 2

# 8- exponentiation and assign (**=):
d **= 3
print(d) # 8

# 9- modulus and assign (%=):
d %= 3
print(d) # 2







# - Comparison Operators

e = 10
f = 7

# 1- Equal too (==)
# we print the the condition by using comparison ((==) equal to ) operator if condition true print true otherwise false
print(e == f)

# 2- not equal to (!=)
# we print the the condition by using comparison ((!=)not  equal to ) operator if condition true print true otherwise false
print(e != f)


# 3- Greater then (>)
# we print the the condition by using comparison ((>) greater then ) operator if condition true print true otherwise false
print(e > f)

# 4- less then(<)
# we print the the condition by using comparison ((<) less then ) operator if condition true print true otherwise false
print(e < f)

# 5- greater then or equal to (>=):
# we print the the condition by using comparison ((>=) greater then or equal to ) operator if condition true print true otherwise false
print(e >= f)

# 6- less then or equal to (<=):
# we print the the condition by using comparison ((<=) less then or equal to ) operator if condition true print true otherwise false
print(e <= f)






# - Logical Operators:
g = 5
h = 12
# 1- and  
#  (and) operator return true if both condition left and right are true otherwise false.
condition1 = g == h and g != h
print(condition1) # false

# 2- or 
# (or) operator return true if any of one condition left or right are true otherwise false.
condition2 = g > h or g < h
print(condition2) # true

# 3- not 
condition3 = not(g == h) 
print(condition3) # true






# - Identity Operators:
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.

# 1 - (is) Returns True if both variables refer to the same object or and same memory location.
# 2- (is not) Returns True if both variables refer to the different object or and different memory location even they have same value.

# understand is and is not by example:

i = ["mango", "banana", "orange"]

j = i # Both 'i' and 'j' point to the same list in memory

k = ["mango", "banana", "orange"] # 'k' is a new list with the same values but a different memory location

print(i is j) # True (same memory location)

print(i is k) # False (different memory location)

print(i is not k) # True (different memory location)




# - Membership Operators:

#Membership operators is used to check whether a value exists in a sequence like a ( list, tuple, or string)

# 1 = (in) used to return true if the value exists in the sequence.

# 2- (not in) used to return true if the value does not exists in the sequence.

# understand in and not in by example:

city: list[str] = ["seoul", "karachi", "Makkah", "Madina"]

print("seoul" in city) # seoul exist in the list that print return True

print("karachi" not in city) # karachi exist in the list that print return False because the the condition says karachi is not exist in city list



# - Bitwise Operators:

# Bitwise operators are used to perform bitwise calculations on integers or Bitwise operators are used to compare (binary) numbers.
l = 5
m = 3

# 1- Bitwise AND (&) :
# Sets each bit to 1 if both bits are 1
print("l & m:", l & m)

# 2- Bitwise OR (|) :
print("l | m:", l | m)

# 3- Bitwise XOR (^) :
# Sets each bit to 1 if the bits are different
print("l ^ m:", l ^ m)

# 4- Bitwise NOT (~) :
# Inverts all the bits
print("~l:", ~l)

# 5- Bitwise left shift: (<<) :
#Shifts bits to the left (multiplies by 2)
print("l << m:", l << 1)

# 6- Bitwise right shift: (>>) :
# Shifts bits to the right (divides by 2)
print("l >> m:", l >> 1)























 




