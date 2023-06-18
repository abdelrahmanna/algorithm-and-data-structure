def towerOfHanoi(n, a='1', b='2', c='3'):
    if (n == 1):
        print("move from " + a + " to " + c)
        return
    # move the n-1 top disk to the middle rod
    towerOfHanoi(n-1, a, c, b)
    
    # move the remaining disk to c
    print("move from " + a + " to " + c)
    
    # move the discs in the middle rod to c
    towerOfHanoi(n-1, b, a, c)
    
    
    

if __name__ == "__main__":
    towerOfHanoi(1)
    
    print("--------------------")
    towerOfHanoi(2)
    
    print("--------------------")
    towerOfHanoi(3)
    
    print("--------------------")
    towerOfHanoi(4)
