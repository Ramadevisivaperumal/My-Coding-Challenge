n=int(input())
for i in range(0,n):
    for j in range(0,n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end='')
        else:
            print(" ",end='')
    print()
'''Pattern 1 otuput:
****
*  *
*  *
****'''

n=int(input())
num=n+2
s=n+2
for i in range(n):
    num=num-1
    for j in range(1,num):
        print("*",end='')
    for m in range(1):
        print(" "*2*i,end='')
        s=s-1
    for j in range(1,s):
        print("*",end='')
    print()
num=1
s=1
k=2*n
for i in range(n):
    num=num+1
    k=k-2
    for j in range(1,num):
        print("*",end='')
    for m in range(1):
       
        print(" "*k,end='')
        s=s+1
    for j in range(1,s):
        print("*",end='')
    print()
'''pattern 2 output:

**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
'''

