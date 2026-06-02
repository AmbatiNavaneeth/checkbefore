move zeros
maj element
nearest prime
all permutations of strimg/list

right rotation end to start
d=4
arr=[1,2,3,4,5]
d %= len(arr)
arr.reverse()
arr[:d] = reversed(arr[:d])
arr[d:] = reversed(arr[d:])
print(arr)

# Right rotation
arr[-d:] + arr[:-d]

# Left rotation
arr[d:] + arr[:d]

left rotation start to end 
d=4
arr=[1,2,3,4,5]
d %= len(arr)
arr[:d] = reversed(arr[:d])
arr[d:] = reversed(arr[d:])
arr.reverse()
print(arr)
