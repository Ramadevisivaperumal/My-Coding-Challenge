#Reverse the integer
n=int(input())
S=str(n)
R=S[::-1]
s = R.lstrip('0')
print(s)
#Prime or not
n=int(input())
for i in range(2,n):
    if(n%i==0):
        prime=1
        break
    else:
        prime=0
if(prime==1):
    print("0")
else:
    print("1")



