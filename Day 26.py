'''
Program 1 Output:
* * * * *
* * * * 
* * * 
* *  
*
'''

n=int(input())
num=n+1
for i in range(n):
    num=num-1
    for j in range(1,num+1):
        print("* ",end='')
    print()
'''
Program 2 Output:
1
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
'''
M=int(input())
num=1
for i in range(1,M+1):
    num=num+1
    for j in range(1,num):
        print(str(i),'',end='')
    print()



'''
 program 3 Output:
1
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
'''
N=int(input())
num=1
for i in range(N):
    num=num+1
    for j in range(1,num):
        print(str(j),'',end='')
    print()

'''    
program 4 Output:
1 2 3 4 5
1 2 3 4
1 2 3 
1 2  
1 
'''

N=int(input())
num=N+1
for i in range(N):
    num=num-1
    for j in range(1,num+1):
        print(str(j),'',end='')
    print()
















    
    


