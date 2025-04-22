
# Q-48. Python Program to Convert Gray to Binary Code.
	
def gray_to_binary(n):
    """Convert Gray codeword to binary and return it."""
    n = int(n, 2) # convert to int
 
    mask = n
    while mask != 0:
        mask >>= 1
        n ^= mask
 
    return bin(n)[2:]
 
 
g = input('Enter Gray code : ')
b = gray_to_binary(g)
print('In binary :', b)

