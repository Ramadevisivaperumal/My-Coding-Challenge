T = int(input())
for tc in range(T):
    X,A,B= map(int, input().split())
    total=(A*1)+(B*2)
    if(total>=X):
        print("Qualify")
    else:
        print("NotQualify")
