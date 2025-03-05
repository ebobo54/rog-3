# # Python3 code to find the nth term of the
# # Baum Sweet Sequence
# def baumSweet(n):

# 	# bitset stores bitwise representation
# 	bs = list(bin(n)[2::])

# 	baum = 1 # nth term of baum sequence
# 	for i in range(len(bs)):
# 		j = i + 1
		
# 		# enter into a zero block
# 		if (bs[i] == '0'): 
# 			cnt = 1

# 			# loop to run through each zero block
# 			# in binary representation of n
# 			for j in range(i + 1, len(bs)):

# 				# counts consecutive zeroes 
# 				if (bs[j] == 0):				 
# 					cnt += 1
# 				else:
# 					break
			
# 			# check if the number of consecutive
# 			# zeroes is odd
# 			if (cnt % 2 == 1):
# 				baum = 0
		
# 		i = j
# 	return baum

# # Driver Code

# print(baumSweet(17))
# print(baumSweet(4))
# print(baumSweet(10))
# print(baumSweet(9))
# print(baumSweet(54))

def baumSweet(n: int) -> int:
    binary = bin(n)[2:]
    zero_blocks = binary.split('1')
    
    for block in zero_blocks:
        if len(block) % 2 == 1:
            return 0
    return 1

print(baumSweet(17))
print(baumSweet(4))
print(baumSweet(10))
print(baumSweet(9))
print(baumSweet(54))
