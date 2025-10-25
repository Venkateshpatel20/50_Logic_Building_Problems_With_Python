# **** Using RECURSION Method ***
def sum_of_digits(m):
    if m == 0:
        return 0
    return m % 10 + sum_of_digits(m//10)

if __name__ == "__main__":
    print(sum_of_digits(9999999))
    print(sum_of_digits(9999997))
    print(sum_of_digits(9999996))
