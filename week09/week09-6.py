a = input().split()
N = len(a)
for i in range(N):
	a[i]=int(a[i])

for k in range(N-1):
	for i in range(1,N):
		if a[i] < a[i-1]:
			a[i], a[i-1] = a[i-1], a[i]
			
for i in range(N):
	print(a[i])