# **** Using RECURSION Method ***
def sum_of_digits(m):
    if m == 0:
        return 0
    return m % 10 + sum_of_digits(m//10)

if __name__ == "__main__":
    print(sum_of_digits(9999999))
    print(sum_of_digits(9999997))
    print(sum_of_digits(9999996))


# *** Digits Extraction Method ***

def sumOfDigits(n):
    sum = 0
    while n != 0:

        last = n % 10
        sum += last
        n //= 10
    return sum

if __name__ == "__main__":
	n = 12345
	print(sumOfDigits(n))
     


# My favourite String method 
number = "29783569283"
sum:int=0
for ch in number:
     sum += int(ch)
print(sum)