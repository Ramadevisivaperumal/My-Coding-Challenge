T = int(input())
for tc in range(T):
    X,Y= map(int, input().split())
    if(Y%X==0):
        print("YES")
    else:
        print("NO")
