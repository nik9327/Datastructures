#!/usr/bin/env python
# coding: utf-8

# In[1]:




class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head=None


# In[2]:


ll=linkedlist()
ll.head = node(1)


# In[4]:


second = node(2)
third = node(3)


# In[6]:


ll.head.next = second
second.next = third


# In[1]:


stack = ['amar','ram','lucky']
stack.append('manish')
stack.append('raveena')
stack.append('rita')
stack.pop()


# In[ ]:





# In[26]:


queue = ['parshant','sunil','akram','madhu','nik','ishu']
queue.append('manish')


# In[27]:


queue.pop(0)
queue


# In[32]:


week =['mon','tue','wed','thurs','fri','sat','sun']
listset = tuple(week)
listset


# In[35]:


import numpy 
numpy.array([])


# In[38]:


a=[15,52,65]
print(a[-3])
print(a[-2])


# In[66]:


k=1000
count=0
for i in range(1+1):
    if i%2 != 0:
        count+=1
print(count*k)  
        


# In[243]:


arr=[4,2,7,6,9]
maxi=0
for i in range() 5<=1:
    x=min(arr)
    arr.remove(x)
    y=min(arr)
    arr.remove(y)
    z=x+y
    maxi+=z
    arr.append(z)


# In[244]:


maxi


# In[6]:


class Solution:
    def minCost(self,arr,n) :
        global maxi
        maxi=0
        x=min(arr)
        arr.remove(x)
        y=min(arr)
        arr.remove(y)
        z=x+y
        maxi=z
        arr.append(z)
        if len(arr)>1:
            z=maxi
            z+=z
            return Solution.minCost(Solution,arr,n)
    
n=6
arr=[4,2,7,6,9]
ob=Solution()
print(ob.minCost(arr,n))


# 18%4

# In[2]:


18%4


# In[154]:


def is_leap(year):
    if year%100==0:
        if year%400==0:
            return True
        else:
            return False
    else:
        if year %4 ==0:
            return True
        else:
            return False
    # Write your logic here
    

year = int(input())
print(is_leap(year))


# In[157]:


x=int(input())


# In[165]:


x=list(map(int,input().split()))
z=10
for i in range(len(x)):
    
    print(x[i])
    z=z+x[i]
print(z)


# In[182]:


x=list(map(int,input().split()))
def avg(x):
    z=0
    for i in range(len(x)):
        z+=x[i]
    print("{0:.2f}".format((z/len(x))))
avg(x)


# In[20]:


#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    new=" "
    a=sentence.split()
    print(a)
    a.reverse()
    new=new.join(a)
    return new.swapcase()
sentence = input()
result = reverse_words_order_and_swap_cases(sentence)
result


# In[15]:


str=['sca','cass','ass']
a=' '
a=a.join(str)
a


# In[26]:


x=map(int,input().split())


# In[30]:


def compute(n, k):

    subsets, offsets = [0]*k, [0]*k

    for i in range(1,n+1):
        subsets[pow(i, i, k)] += 1

    offsets[0] = 1
    for i in range(k):
        for j in range(subsets[i]):
            offsets = [(offsets[j] + offsets[(j-i)]) % 10**9 for j in range(k)]

    return str(offsets[0]-1)

if __name__ == "__main__":
    
    n, k = list(map(int,input().split(" ")))
    print(compute(n, k))


# In[35]:


n=int(input())
ar
arr.insert(0, 5)
arr.insert(0, 10)
arr.sort()


# In[47]:


if __name__ == '__main__':
    N = int(input())
    arr=[]
    for i in range(N):
        if i==0:
            arr.insert(0,5)
        if i==1:
            arr.insert(1,10)
        if i==2:
            arr.insert(0,6)
        if i==3:
            print(arr)
        if i==4:
            arr.remove(6)
        if i==5:
            arr.append(9)
        if i==6:
            arr.append(1)
        if i==7:
            arr.sort()
        if i==8:
            print(arr)
        if i==9:
            arr.pop()
        if i==10:
            arr.reverse()
        if i==11:
            print(arr)


# In[50]:


(12*20)/100


# In[52]:


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    tip=(meal_cost*tip_percent)/100
    tax=(meal_cost*tax_percent)/100
    print(round(meal_cost+tip+tax))

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)

    


# In[53]:


i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
a=int(input())
b=float(input())
c=input()
# Read and save an integer, double, and String to your variables.
print(a+i)
# Print the sum of both integer variables on a new line.
print(d+b)
# Print the sum of the double variables on a new line.
print(s+c)
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.


# In[61]:


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    if N%2!=0:
        print("Weird")
    else:
        if N>=2 and N<=5:
            print("Not Weird")
        elif N>=6 and N<=20:
            print("Weird")
        else:
            print("Not Weird")     


# In[4]:


class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge < 0:
            
            print("Age is not valid, setting age to 0.")
            self.age=0
        else:
            self.age=initialAge
    def amIOld(self):
            # Do some computations in here and print out the correct statement to the console
        if self.age<13:
            print("You are young.")
        elif self.age>=13 and self.age <18:
            print("You are teenager.")
        else:
            print("You are old.")
    def yearPasses(self):
            # Increment the age of the person in here
        self.age+=1

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")


# In[1]:


class Person:
    def __init__(self, initialAge):
        if initialAge > 0:
            self.age = initialAge
        else:
            print("Age is not valid, setting age to 0.")
            self.age = 0

    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        self.age += 1


t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")


# In[58]:


a=int(input())
x=list(input())
y=list(input())


def funcall(x):
    m=[]
    n=[]
    o=[]
    for i in range(len(x)):
        if i%a==0:
            m.append(x[i])
        elif i%a==1:
            n.append(x[i])
        else:
            o.append(x[i])
    s=''
    t=''
    u=''
    s=s.join(m)
    t=t.join(n)
    u=u.join(u)
    print(s+" "+ t+" "+u)
    
funcall(x)
funcall(y)


# In[2]:


a=int(input())

for i in range(a):
    m=[]
    n=[]
    str=input()
    for j in range(len(str)):
        if j%2==0:
            m.append(str[j])            
    
    
    for k in range(len(str)):
        if k%2!=0:
              n.append(str[k])    
    s=''
    s=s.join(m)
    t=''
    t=t.join(n)

    print(s+" "+ t)    
 


# In[41]:


#!/bin/python3

import math
import os
import random
import re
import sys

    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    a=arr[::-1]
    print(a)


# In[23]:


def convert(lst):
      
    return ' '.join(lst)
      
# Driver code
lst = ['geeks', 'for', 'geeks']
print(convert(lst))


# In[78]:


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
a =  arr[::-1]
print (" ".join(str(x) for x in a))


# In[ ]:





# In[ ]:





# In[ ]:


phonebook = {}
entries = int(input())

for n in range(entries):
    name, num = input().strip().split(' ')
    name, num = [str(name), int(num)]
    phonebook[name] = num

while True:
    try:  
        search = str(input())

        if search in phonebook.keys():
            #output = ''.join('%s=%r' % (search, phonebook[search]))
            output = search+"="+str(phonebook[search])
            print(output)
        else:
            print("Not found")
    except EOFError:
        break


# In[6]:


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    # Write your code here
    if n==1:
        return n
    else:
        return n* factorial(n-1)
if __name__ == '__main__':
    

    n = int(input().strip())

    result = factorial(n)
    print(result)
    


# In[15]:


n=int(input())
arr=[]
def binary(n):
    if n>=1:
        binary(n//2)
    arr.append(n%2)
    
binary(n)


# In[19]:



# Python program to find
# length of the longest
# consecutive 1s in
# binary reprsentation of
# a number.
 
def maxConsecutiveOnes(x):
 
    # Initialize result
    count = 0
  
    # Count the number of iterations to
    # reach x = 0.
    while (x!=0):
     
        # This operation reduces length
        # of every sequence of 1s by one.
        x = (x & (x << 1))
  
        count=count+1
     
    return count
 
# Driver code
 
print(maxConsecutiveOnes(4))
print(maxConsecutiveOnes(222))


# In[24]:


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    count = 0
    while (n!=0):
        n=(n &(n << 1))
        count+=1
    print(count)


# In[5]:


#!/bin/python3

import math
import os
import random
import re
import sys


arr = []
for arr_i in range(6):
    arr_temp = map(int,input().strip().split(' '))
    arr.append(arr_temp)
res = []

for x in range(0, 4):
    for y in range(0, 4):
        s = sum(arr[x][y:y+3]) + arr[x+1][y+1] + sum(arr[x+2][y:y+3])
        res.append(s)

print(max(res))


# In[ ]:





# In[ ]:




