'''Pattern 1 Output:
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15'''
n=int(input())
num=1
a=1
for i in range(n):
    num=num+1
    for j in range(1,num):
        print(str(a)+" ",end='')
        a=a+1
    print()
'''pattern 2 Output:
1                 1
1 2             2 1
1 2 3         3 2 1
1 2 3 4     4 3 2 1
1 2 3 4 5 5 4 3 2 1
'''
n=int(input())
num=1
a=0

for i in range(1,n+1):
    num=num+1
    a=a+1
    for j in range(1,num):
        print(str(j)+" ",end='')
        
    for k in range(0,4*(n-i)):
        print(" ",end='')
    
    for m in range(a,0,-1):
        print(str(m)+" ",end='')
       
    print()







        
