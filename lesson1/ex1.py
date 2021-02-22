def nth_root(x,n):
    """
    Compute the n-th root of x.
    
    Parameters:
    - x: the number the root is to be taken of
    - n: the root index (integer)
    
    Returns:
    - r: the root (float)
    """
    
    if type(n) is not int:
        print('The index must be an integer!')
        return None
    
    if x<0 and n%2==0:
        print('Cannot take an even root of a negative number!')
        return None
    
    return x**(1./n)

odds = []
sums = []

for i in range(10):
    if i%2:
        odds.append(i)

print(odds)

for i in range(len(odds)):
    k = 0
    for j in range(i+1):
        k += odds[j]
        
    sums.append(k)

print(sums)

roots = [nth_root(x,2) for x in sums]

print(roots)
    
