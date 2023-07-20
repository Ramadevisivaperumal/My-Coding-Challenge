'''Pattern 1 Output:
* 
* * 
* * * 
* * * * 
* * * * *
* * * *
* * *
* *
*
'''
n=int(input())
for i in range(n+1):
    print(i*"* ")
for j in range(n-1,-1,-1):
    print(j*"* ")
'''pattern 2 Output:
1 
0 1 
1 0 1
0 1 0 1 
1 0 1 0 1'''
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        if(i+j)%2==0:
            print("1"+" ",end='')
        else:
            print("0"+" ",end='')
    print()
      
