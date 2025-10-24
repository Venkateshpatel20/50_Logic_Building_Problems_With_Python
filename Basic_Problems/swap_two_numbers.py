# Built-in Swap

a = 10
b = 20
print("a =", a, " b =", b)
a , b = b , a # swaps a = 20 , b = 10
print("a =", a, " b =", b)
 
# Using third variable
a = 45
b = 55
print("a =", a, " b =", b) #
temp = a
a = b 
b = temp
print("a =", a, " b =", b) # prints a = 55 , b = 45 

#Without using third variable


# A> Using Arithmatic Operators

a = 20 
b = 43

print("a =", a, " b =", b)# prints a = 20 , b = 43 

a = a + b
b = a - b
a = a - b

print("a =", a, " b =", b)# prints a = 43 , b = 20

# B> Using XOR Operator , it return 1 only when bits are different
a = 5  # 0101
b = 9  # 1001
print("a =", a, " b =", b)# prints a = 5 , b = 9
a = a ^ b #0101 ^ 1001 = 1100 a becomes 12
b = a ^ b #1100 ^ 1001 = 0101  b becomes 5 (original a)
a = a ^ b #1100 ^ 0101 = 1001   a becomes 9 (original b)
print("a =", a, " b =", b)# prints a = 9 , b = 5