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