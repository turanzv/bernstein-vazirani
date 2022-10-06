# Input is a function that takes a bitstream length n
# and returns {0,1}.

# Input function performs the operation: a * x + b
# a is a bitstring length n
# b is an unknonwn single bit
# * is inner product mod 2
# + is addition mod 2

# Bernstein-Vazirani takes in a function of the
# above description and returns unknown contants a 
# and b.

# This can be interpreted as the quantum equivalent
# of deriving m and b from y = m * x + b.

# Input func, n
def bernsteinvazirani(func, n):
    
    a = []
    base_bits = [0 for _ in range(n)]

    # find b using func([0]*n)
    # a * 0 + b
    # 0 + b
    # (0 + b) % 2
    # b
    b = func(base_bits)

    # find a by using func(i) - b
    # i is a bitstream with one 1 in the jth place
    
    # by taking the inner product of a and i, we can
    # isolate a[j] and recreate a
    
    # (a * i + b) - b
    # a * i
    # a[j]

    # repeat for all j in n and join -> a

    base_bits = [0 for _ in range(n)]
    
    for j in range(n):
        base_bits[j] = 1

        res = func(base_bits)

        # b XOR res => a * i
        a[j] = int(b != res)

    return (a, b)



# lazy function to calculate dot product without complex conj.
def lazy_dot(a, b):
    return sum(ai * bi for ai, bi in zip(a, b))

