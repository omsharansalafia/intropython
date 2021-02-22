# Solution to Exercise 1

# define n_th root function
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


# create lists containing the first 5 odd numbers and their sums
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

# compute the square roots of the sums of the first 5 odd numbers
roots = [nth_root(x,2) for x in sums]

print(roots)

# demonstrate the internal checks in the function
nth_root(-2,2)
nth_root(4,2.0)

    
