T = int(input())
for tc in range(T):
    X=int(input())
    if(X%10)==0:
        print(X//10)
    elif(X%5)==0:
        rem=X%10
        print((X//10)+(rem//5))
    else:
        print("-1")
        
