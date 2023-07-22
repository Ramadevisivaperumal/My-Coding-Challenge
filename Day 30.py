
'''Pattern 1 Output:
A
AB
ABC
ABCD
ABCDE
'''

num=1
n=int(input())
for i in range(n):
    num=num+1
    a=65
    for j in range(1,num):
        print(chr(a),end='')
        a=a+1
    
    print()
    
