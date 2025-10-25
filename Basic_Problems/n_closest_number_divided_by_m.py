def closest_number(n,m):
    closest = 0
    min_difference = float('inf')
    for i in range(n - abs(m),n+abs(m)+1):
        if i % m ==  0:
            difference  =  abs(n-i)
            if difference < min_difference or (difference == min_difference and abs(i) > abs(closest)):
                closest = i
                min_difference = difference
    return closest


if __name__ == "__main__":
    n = 132
    m = 21
    print(closest_number(n,m))
    print(closest_number(m,n))
