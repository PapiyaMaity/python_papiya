#!/usr/bin/env python
# coding: utf-8

# ## QUESTION 1
# ### count the number of perfect square numbers in a given range, range is take as input from user
# 

# In[2]:


s=int(input("Enter the starting range: "))
e=int(input("Enter the ending range: "))
print("Perfect squares are:")
for i in range(s,e):
    for j in range(i):
        if j**2==i:
            print(i)


# ## QUESTION 2
# ### Write a python program to generate the following pattern
#     *
#     * *
#     * * *
#     * * * *
#     * * * * *
#     * * * *
#     * * *
#     * *
#     *
# 

# In[2]:


n=int(input("Enter the no. of rows: "))
for i in range(0,n):
    if i<=n//2:
        for j in range (0,i+1):
            print("*",end=" ")
        print("\n")
    else:
        for j in range (n-i+1,1,-1):
            print("*",end=" ")
        print("\n")


# ## Question 3:
# ### Take a number as input from user and display whether it is prime or not
# 

# In[8]:


n=int(input("Enter a number: "))
c=0
print("The number",n," is ",end="")
for i in range(2,n):
    if n%i==0:
        c=1
        break;
    else:
        c=0
if c==0:
    print("prime")
else:
    print("not prime")        


# In[ ]:





# In[ ]:




