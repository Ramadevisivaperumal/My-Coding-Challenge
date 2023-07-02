T = int(input())
for tc in range(T):
    X,Y,Z= map(int, input().split())
    P=Y*Z
    if(X<=P):
        print("YES")
    else:
        print("NO")
