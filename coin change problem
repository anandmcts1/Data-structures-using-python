#Coin change dynamic programming
coins=[1,2,5]
a=11
l=[0]
for i in range(1,a+1):
	l.append(a+1)
print(l)
for i in range(0,a+1):
	for c in coins:
		if i-c>=0:
			l[i]=min(l[i-c]+1,l[i])
print(l)
