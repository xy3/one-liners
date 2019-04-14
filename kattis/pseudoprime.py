[(lambda p,a:print('yes'if pow(a,p,p)==a and len([False for i in range(2,int(p**0.5+1))if p%i==0])else'no'))(*map(int,l.split()))for l in(__import__('sys')).stdin.readlines()[:-1]]
	