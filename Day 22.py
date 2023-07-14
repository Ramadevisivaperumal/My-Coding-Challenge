T = int(input())
for tc in range(T):
    N=int(input())
    array=list(map(int,input().split()))

    for i in range(N-1,-1,-1):
        if array[i]!=0:
            answer=i
            break
    print(answer)
