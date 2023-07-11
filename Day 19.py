T = int(input())
for tc in range(T):
    N,Y= map(int, input().split())
    if (Y>=N):
        print(N)
    elif (Y<N):
        print(N+(N-Y))
