#**** Naive Approach *****

def summation1(n):
    return sum([i**2 for i in range(1, n + 1)])
#**** Using Mathematical Formulae ***

def summation2(n):
    return (n * (n + 1) * 
           (2 * n + 1)) / 6

if __name__ == "__main__":
    n = 2
    print(summation1(n)) #gives the integer point number output
    print(summation2(n)) #gives the floating point number output 