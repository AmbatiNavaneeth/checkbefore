longest palindromic substring
longest palindorme can make from a string

move zeros

maj element
nearest prime
all permutations of strimg/list
from itertools import permutations
s = "ABC"
for p in permutations(s):
    print("".join(p))

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

nearest prime
n=10
def is_prime(n):
  if n<2:
    return False
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
  else:
    return True
def nearest_prime(n):
  if is_prime(n):
        return n
  left=n-1
  right=n+1
  while True:
    if left>=2 and is_prime(left):
      return left
    if right>=2 and is_prime(right):
      return right
    left-=1
    right+=1








  

    
