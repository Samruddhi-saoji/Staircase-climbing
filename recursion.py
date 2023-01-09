#recurion approach

#number of ways to go from stair 0 to stair n
#jumps = list of jumps that are allowed
def ways_to_go(n, jumps) :
    if n<jumps[0] : return False
    if n==jumps[0] : return 1
    #jumps[0] is smallest jump possible
    
    #taking a jump while at stair "src"
    def go(src, jump, ways):
        dest = src + jump
        
        if dest==n :
            #we have reached the destination
            return ways+1
        if dest > n :
            #we have overshot
            #this way doesnt count
            return ways+0
            
        for j in jumps:
            ways = go(dest, j, ways)
            
        return ways
        
    ways = go(0, 0,0)  #initial call, so jump=0
    return ways
#########№########################
          
#array jumps should be in increasing order
jumps = [1,2,3]
ans = ways_to_go(10, jumps)
print(ans)