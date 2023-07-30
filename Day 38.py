#Decimal to Binary
n =int(input())
print('{0:b}'.format(n))
#Binary to Decimal
binary = input()
decimal = 0
for digit in binary:
    decimal = decimal*2 + int(digit)
print(decimal)

