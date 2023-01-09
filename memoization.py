import numpy as np

#number of ways to go from stair 0 to stair n
#jumps = list of jumps that are allowed
def ways_to_go(n, jumps) :
    if n<jumps[0] : return False
    if n==jumps[0] : return 1
    #jumps[0] is smallest jump possible

    #array for storing cache
    cache = np.zeros(n+1)
    #cache[i] = number of ways to go from stair i to stair n
    cache[n] = 1
    cache[n-1] = 1
    
    #taking a jump while at stair "src"
    def go(src, jump, ways):
        dest = src + jump
        
        if dest==n : #desired estination
            return ways+1 #new way found
        if dest > n : #overshot
            #this way doesnt count
            return ways

        #if we have already found the number of ways to go to stair n from dest
        if cache[dest] != 0 :
            return ways + cache[dest]
            
        #from this stair, make all possible jumps
        for j in jumps:
            ways = go(dest, j, ways)

        #we have now found the tot ways to go from stair "dest" to stair n
        cache[dest] = ways
            
        return ways
        
    ways = go(0, 0,0)  #initial call, so jump=0
    return int(ways)
#########№########################
          
#array jumps should be in increasing order
jumps = [1,2]
ans = ways_to_go(35, jumps)
print(ans)