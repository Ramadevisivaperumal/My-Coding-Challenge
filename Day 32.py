'''Pattern Output:
4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4
'''
n=int(input())
num=n
k=2*n
s=n+1
p=n
for i in range(0,n):
    num=num-1
    k=k-2
    s=s-1
    for j in range(n,num,-1):
        print(str(j)," ",end='')
    for j in range(k,1,-1):
        print(str(s)," ",end='')
    for j in range(i+1):
        m=n-i+j
        if m==1:
            continue
        print(str(m)+" ", end=" ")
    print()
s=1
m=1
for i in range(1,n):
    s=s+1
    m=m+2
    for j in range(n,i,-1):
        print(str(j)+"  ",end='')
    for j in range(m,2,-1):
        print(str(s)+"  ",end='')
    for j in range(i,n):
        print(str(j+1)+" ", end=' ')
    print()

    

