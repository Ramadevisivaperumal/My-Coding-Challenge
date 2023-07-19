'''Pattern 1 Output:
    *
   ***  
  *****
 *******
*********'''
n=int(input())
k=1
for i in range(n-1,-1,-1):
    print(" "*i,end='')
    print(k*"*")
    k=k+2



'''pattern 2 output           
*********
 *******
  *****
   ***
    *   '''

n=int(input())
k=2*n-1
for i in range(0,n):
    print(" "*i,end='')
    print(k*"*")
    k=k-2
'''Pattern 3 Output:
    *
   ***  
  *****
 *******
*********
*********
 *******
  *****
   ***
    *  '''
n=int(input())
k=1
for i in range(n-1,-1,-1):
    print(" "*i,end='')
    print(k*"*")
    k=k+2
k=2*n-1
for j in range(0,n):
    print(" "*j,end='')
    print(k*"*")
    k=k-2












    
