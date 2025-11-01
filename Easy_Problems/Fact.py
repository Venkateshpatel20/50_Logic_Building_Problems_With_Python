class numberSeries:
    def factorial(self,num):
        res = 1
        i = 2
        if num == 0 or num == 1:
            return 1
        while (i<= num):
            res = res*i
            i += 1
        return res
    
#Recursive Approach
    def factorial2(self,num):
        if num == 0 :
            return 1
        return num * self.factorial2(num-1)
    



if __name__ == "__main__":
    obj = numberSeries()
    print(obj.factorial(5))
    print(obj.factorial2(5))
    print(obj.factorial(1))
    print(obj.factorial2(1))
    print(obj.factorial(123))
    print(obj.factorial2(123))
    
