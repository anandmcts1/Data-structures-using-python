from itertools import groupby

def lookandsay(s):
	return ''.join(str(len(list(g)))+k for k,g in groupby(s))
n='1'
for i in range(5):
	print(n)
	n=lookandsay(n)
