#Problem : We have given two rectangle's coordinates top left and bottom right 
# l1 and l2 are top left corner coordinates of two rectangle 
# r1 , r2 are the bottom right coordinates of two rectangles 

# We can say the rectanlges overlap when the corner's coordinate exists inside of 
# another rectangle space , We can also conclude that if they are't overlapping if they are 
# side-by-side or top and down of each other 

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
def do_overlap(l1,r1,l2,r2):
    if l1.x > r2.x or l2.x>r1.x:
        return False
    if r1.y > l2.y or r2.y > l1.y:
        return False
    return True 
if __name__ == "__main__":
    l1 = Point(0,10)
    r1 = Point(10,0)
    l2 = Point(5,5)
    r2 = Point(15,0)
    if do_overlap(l1,r1,l2,r2):
        print("rectangles overlap")
    else:
        print("They do not overlap")
    l1 = Point(9,10)
    r1 = Point(10,20)
    l2 = Point(5,57)
    r2 = Point(15,53)
    if do_overlap(l1,r1,l2,r2):
        print("rectangles overlap")
    else:
        print("They do not overlap")