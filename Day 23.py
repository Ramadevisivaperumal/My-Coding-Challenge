T = int(input())
for tc in range(T):

	X,Y,Z= map(int, input().split())
	S=X+Y+Z-max(X,Y,Z)-min(X,Y,Z)
	print(S)
