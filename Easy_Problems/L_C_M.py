#Finding the LCM < least common faactor > of two numbers 

class numberSeries:
    # Optimal approach
    # function for gcd
    # Time Complexity: O(log(min(a,b))
    # Auxiliary Space: O(log(min(a,b))
    def gcd(self,a, b):
        return a if b == 0 else self.gcd(b, a % b)

    def lcm(self,a, b):
        return (a // self.gcd(a, b)) * b


    

    #Brute force approach
    # Time Complexity: O(min(a,b))
    # Auxiliary Space: O(1)

    def find_lcm(self,a,b):
        small_num = min(a,b)
        large_num = max(a,b)

        # loop through range(max,max*min+1,max)
        for num in range(large_num,large_num * small_num + 1,large_num):
            if num % small_num == 0:
                lcm = num
                return lcm

if __name__ == "__main__":
    a , b = 12 , 4
    c , d = 11 , 7
    obj = numberSeries()
    print(obj.lcm(a,b))
    print(obj.lcm(c,d))
    print(obj.find_lcm(a,b))
    print(obj.find_lcm(c,d))



