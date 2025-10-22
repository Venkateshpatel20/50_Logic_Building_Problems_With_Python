# **** First Method ****
def isEven(n):
    rem = n % 2
    if rem == 0:
        return True 
    else:
        return False
#  **** Second Method ****
def isEven2(n):
    if n & 1:
        return False
    else:
        return True


print(isEven(4))   # True
print(isEven(7))   # False
print(isEven2(10)) # True