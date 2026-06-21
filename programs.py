longest palindromic substring
longest palindorme can make from a string

anagram
strs = ["eat","tea","tan","ate","nat","bat"]
from collections import defaultdict
def groupAnagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        groups[key].append(s)
    return list(groups.values())
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))

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

nums=[0,1,2,0,1,2]

low, mid, high = 0, 0, len(nums) - 1
while mid <= high:
    if nums[mid] == 0:
        nums[low], nums[mid] = nums[mid], nums[low]
        low += 1
        mid += 1
    elif nums[mid] == 1:
        mid += 1
    else:
        nums[mid], nums[high] = nums[high], nums[mid]
        high -= 1
print(nums)


nums=[1, 3, 20, 4, 1, 0,1,8,2]
n=len(nums)
if n<3:
    print(False)
i=1
for i in range(n-1):
    if nums[i-1]>nums[i]:
        i+=1
    elif nums[i]<nums[i+1]:
        i+=1
    elif nums[i-1]<nums[i]>nums[i+1]:
        print(nums[i],end=' ')


nums= [1, [2, [3, [4]], 5]]
ans=[]
for i in range(len(nums)):
    for j in range(i):
        ans.append(i)
print(ans)

nums=[1,2,0,2,1,0]
j=0
for i in range(len(nums)):
    if nums[i]==0:
        nums[i],nums[j]=nums[j],nums[i]
        j+=1
j=len(nums)-1
for i in range(len(nums)-1,-1,-1):
    if nums[i]==2:
        nums[i],nums[j]=nums[j],nums[i]
        j-=1
print(nums)
nums=[1,2,0,2,1,0]
low=0
mid=0
high=len(nums)-1
while mid<=high:
    if nums[mid]==0:
        nums[low],nums[mid]=nums[mid],nums[low]
        low+=1
        mid+=1
    elif nums[mid]==1:
        mid+=1
    else:
        nums[mid],nums[high]=nums[high],nums[mid]
        high-=1
print(nums)   

Group Anagrams
Problem: Write a function to group anagrams from an array of strings.
Testcase 1:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]


strs = ["eat","tea","tan","ate","nat","bat"]
from collections import defaultdict
def groupAnagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        groups[key].append(s)
    return list(groups.values())
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))

Longest Increasing subsequence in an array.
Testcase 1:
Input: [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4

def lengthOfLIS(nums):
    n = len(nums)
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(lengthOfLIS(nums))


 Convert the given Input Empty String into the given Output
    Testcase 1:
    Input : [ ]
    Output : [[1,2,3][4,5,6][7,8,9]]

arr=[]
num=1
for i in range(3):
    row=[]
    for j in range(3):
        row.append(num)
        num+=1
    arr.append(row)
print(arr)
   
You are given an array of integers. Rearrange the array such that:
All even numbers appear before all odd numbers.
Within the even and odd groups, numbers should maintain their relative order from the original array.
The rearrangement must be done in-place (without using extra arrays).
Output: [2, 4, 6, 3, 1, 7, 5]
     
arr = [3, 1, 2, 4, 7, 6, 5]
even_pos = 0
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        temp = arr[i]
        j = i
        while j > even_pos:
            arr[j] = arr[j - 1]
            j -= 1
        arr[even_pos] = temp
        even_pos += 1
print(arr)

Find the Longest Word
Problem: Write a function to find the longest word in a string.
Testcase 1:
Input: "The quick brown fox jumps over the lazy dog"
Output: "jumps"

Check for Anagrams

Problem: Write a function to check if two strings are anagrams of each other.
Testcase 1:
Input: "listen", "silent"
Output: true

s="liten"
t="silnt"
c=[0]*26
for i in range(len(s)):
    c[ord(s[i])-97]+=1
    c[ord(t[i])-97]-=1
for a in c:
    if a!=0:
        print(False)
        break
else:
    print(True)


Find the First Non-Repeating Character
Problem: Write a function to find the first non-repeating character in a string.
Testcase 1:
Input: "swiss"
Output: 'w'

s="swiss"
freq={}
for ch in s:
    freq[ch]=freq.get(ch,0)+1
for i in freq:
    if freq[i]==1:
        print(i)
        break


Check if String is a Valid Number
Problem: Write a function to check if a string is a valid number.
Testcase 1:
Input: "123.45"
Output: true

s="123.45"
try:
    float(s)
    print(True)
except:
    print(False)
s="123.4"
valid=True
dot=0
for ch in s:
    if ch==".":
        dot+=1
        if dot>1:
            valid=False
    elif not ch.isdigit():
        valid=False
print(valid)

Check if a String is a Rotation of Another String
Problem: Write a function to check if one string is a rotation of another string.
Testcase 1:
Input: "abcde", "cdeab"
Output: true

s= "abcde"
t="cdeab"

if t in s+s:
    print(True)
else:
    print(False)


Reverse Words in a String
Problem: Write a function to reverse the order of words in a given string.
Testcase 1:
Input: "hello world"
Output: "world hello"

s="hello world"
ss=s.split()
print(ss)
ans=''
res=[]
for w in ss[::-1]:
    res.append(w) 
print(" ".join(res))


s="hello world"
ss=s.split()
print(ss)
ans=''
res=[]
for w in ss:
    res.append(w[::-1])  #olleh dlrow
print(" ".join(res))
    

String Compression
`Problem: Write a function to perform basic string compression using the counts of repeated characters.
Testcase 1:
Input: "aabcccccaaa"
Output: "a2b1c5a3"

s="aabcccccaaa"
ans=""
c=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        c+=1
    else:
        ans+=s[i-1]
        ans+=str(c)
        c=1
ans+=s[i]
ans+=str(c)
print(ans)


Find All Permutations of a String

Problem: Write a function to find all permutations of a given string.
Testcase 1:
Input: "abc"
Output: ["abc", "acb", "bac", "bca", "cab", "cba"]

def permute(s,ans=""):
    if len(s)==0:
        print(ans)
        return
    for i in range(len(s)):
        ch=s[i]
        rem=s[:i]+s[i+1:]
        permute(rem,ans+ch)
permute("abc")


Find the Longest Substring Without Repeating Characters
Problem: Write a function to find the length of the longest substring without repeating characters.
Testcase 1:
Input: "abcabcbb"
Output: 3

# Convert Roman Numerals to Integer
# Problem: Write a function to convert a Roman numeral string to an integer.
# Testcase 1:
# Input: "MCMXCIV"
# Output: 1994
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

s="MCMXCIV"
m={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
ans=0
for i in range(len(s)):
    if i+1<len(s) and m[s[i]]<m[s[i+1]]:
        ans-=m[s[i]]
    else:
        ans+=m[s[i]]
print(ans)


# Check if Two Strings are Isomorphic
# Problem: Write a function to check if two strings are isomorphic (each character in one string can be mapped to a character in the other string, preserving order).
# Testcase 1:
# Input: "egg", "add"
# Output: true

s="egg"
t="add"  
if len(s)!=len(t):
    print(False)
else:
    s_t={}
    t_s={}
    for c1,c2 in zip(s,t):
        if c1 in s_t and s_t[c1]!=c2:
            print(False)
        elif c2 in t_s and t_s[c2]!=c1:
            print(False)
        s_t[c1]=c2
        t_s[c2]=c1
    else:
        print(True)

















  

    
