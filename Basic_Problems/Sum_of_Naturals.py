# **** First Method ****
def findsum(n):
    sum = 0
    i = 1
    while i <= n:
        sum += i
        i += 1

    return sum
if __name__ == "__main__":
    n = 5
    print(findsum(5))
    print(findsum(50))
    print(findsum(500))

# **** Second Method <Recursion>****
def findsum(n):
    if n == 1:
        return 1
    return n + findsum(n - 1)
if __name__ == "__main__":
    n = 5
    print(findsum(5))
    print(findsum(50))
    print(findsum(500))

# **** Third Method <Formula>****
def findsum(n):
    sum = n * (n + 1) // 2
    return sum
if __name__ == "__main__":
    
    print(findsum(5))
    print(findsum(50))  