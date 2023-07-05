T = int(input())
for tc in range(T):
    X=int(input())
    remainder=X%4
    if(remainder==0):
        print("GOOD")
    else:
        print("NOT GOOD")
