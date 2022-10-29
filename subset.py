import itertools
 
def findsubsets(s, n):
    return list(itertools.combinations(s, n))
 
# Driver Code
s = {1, 2, 3}
n = 2
 
print(findsubsets(s, n))
