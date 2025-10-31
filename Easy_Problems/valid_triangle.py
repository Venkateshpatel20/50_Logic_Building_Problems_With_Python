def checkValidity(a, b, c): 
     
    if (a + b <= c) or (a + c <= b) or (b + c <= a) :
        return False
    else:
        return True        
a = 7
b = 10
c = 5
if checkValidity(a, b, c):
    print("Valid") 
else:
    print("Invalid")

    # condition to form a triangle is the sum of any two sides length should be greater than third side legth