import math as mt
#Prime check using the traditional looping /
# Here time complexity is O(n) /
# Space complexity is constant  

class numberSeries():
    def primeCheck(self,num):
        if num < 2:
            return False
        n = 2
        count = 0
        while n < num:
            if num % n == 0:
                count += 1
            if count == 1:
                return False
            n += 1
        return True 
    
if __name__ == "__main__":
    obj = numberSeries()
    print(obj.primeCheck(2341234))
    print(obj.primeCheck(2341231))
    print(obj.primeCheck(23))



#Prime checking using math module 
class primeCheck():
    def isPrime1(self,n):
        if n <= 1:
            return False
        for i in range(2,int(mt.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
    

if __name__ == "__main__":
    obj1 = primeCheck()
    print(obj1.isPrime1(2))
    print(obj1.isPrime1(47))
    print(obj1.isPrime1(1))
    print(obj1.isPrime1(59))


#Optimised method 
class primecheck():
    @classmethod
    def is_prime(cls,n):
        if n == 2 or n == 3:
            return True
        elif n<=1 or n%2 == 0 or n%3 == 0:
            return False
        for i in range(5,mt.sqrt(n)+1,6):
            if n % i == 0 or n % (i+1) == 0:
                    return False
        return True
    
    