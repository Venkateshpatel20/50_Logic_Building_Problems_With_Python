#Finding the LCM < least common faactor > of two numbers 
#Brute force approach

class numberSeries:
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
    print(obj.find_lcm(a,b))
    print(obj.find_lcm(c,d))
