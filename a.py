import sys
def sol():
    def minop(x):
        y = 0
        i = len(str(x))
        while i != 0:
            if i > 1:
                res = x // 10**((i - 1))
            else:
                res = x
            
            if res % 2 == 1 and i == 1:
                y += 1
            if res % 2 == 1 and i > 1:
                prev = 10** (i - 1) 
                if x % 10**((i - 1)) == 0:
                    y += 1
                    x -= 1
                    i = len(str(x))
                    continue

                elif x - res * prev >= prev * (res + 1) - x and res != 9:
                    y += prev * (res +1) - x 
                    x += prev * (res +1) - x
                    print("+",x,y)
                    
                elif x - res * prev < prev * (res + 1) - x or res == 9:
                    y += x - res * prev
                    x -= x - res * prev
                    x -= 1
                    y += 1
                    print("-",x,y)
                  
            if i > 1:    
                x = x % (10**(i-1))
                i = len(str(x))
            else:
                i = 0

        return y
    def plus(x):
        y = 0
        i = len(str(x))
        while i != 0:
            if i > 1:
                res = x // 10**((i - 1))
            else:
                res = x
            
            if res % 2 == 1 and i == 1:
                y += 1
            if res % 2 == 1 and i > 1:
                prev = 10** (i - 1) 
                if x % 10**((i - 1)) == 0 or res == 9:
                    return float('inf')

                elif res != 9:
                    y += prev * (res +1) - x 
                    x += prev * (res +1) - x
                    
                  
            if i > 1:    
                x = x % (10**(i-1))
                i = len(str(x))
            else:
                i = 0

        return y

    def minus(x):
        y = 0
        i = len(str(x))
        while i != 0:
            if i > 1:
                res = x // 10**((i - 1))
            else:
                res = x
            
            if res % 2 == 1 and i == 1:
                y += 1
            if res % 2 == 1 and i > 1:
                prev = 10** (i - 1) 
                if x % 10**((i - 1)) == 0:
                    y += 1
                    x -= 1
                    i = len(str(x))
                    continue

                else:
                    y += x - res * prev
                    x -= x - res * prev
                    x -= 1
                    y += 1
                  
            if i > 1:    
                x = x % (10**(i-1))
                i = len(str(x))
            else:
                i = 0

        return y
    
    t = int(input()) # read a line with a single integer
    for i in range(1, t + 1):
      x = int(input()) # read a list of integers, 2 in this case
      y = min(plus(x),minus(x))
      print("Case #{}: {}".format(i, y))
      # check out .format's specification for more formatting options
      
      
sol()