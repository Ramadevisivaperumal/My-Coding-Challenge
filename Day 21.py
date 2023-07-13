T = int(input())
for tc in range(T):
    Y=int(input())
    salary1=Y+((10/100)*Y)+((90/100)*Y)
    salary2=Y+((98/100)*Y)+500
    if (Y<1500):
        print(salary1)
    else:
        print(salary2)
	
