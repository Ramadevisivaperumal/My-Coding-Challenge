#palindrome number
S=int(input())
S=str(S)
M=S[::-1]
if(M==S):
    print("True")
else:
    print("False")
#Armstrong number
N=int(input())
M=str(N)
sum=0
for i in M:
    m=int(i)
    sum=sum+m*m*m
if sum==N:
    print("YES")
else:
    print("NO")

