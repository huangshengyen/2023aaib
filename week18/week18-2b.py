a,b=list(map(int,input().split()))
print('Enter two integers: ')
def gcd(a,b):
	if a==0:return b
	if b==0:return a
	return gcd(b,a%b)
print(f'The greatest common divisor of {a} and {b} is {gcd(a,b)}')