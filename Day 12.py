T = int(input())
for tc in range(T):
    X,Y= map(int, input().split())
    company1=X*10   #X=100, company1 offer=10%,100*100/10=amount
    company2=Y*5
    if(company1>company2):
        print("FIRST")
    elif(company1<company2):
        print("SECOND")
    else:
        print("ANY")
