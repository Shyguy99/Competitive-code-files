for _ in range(int(input())):
	n=int(input())
	a=input()
	s=""
	p=[]
	for i in range(n):
		if i==0:
			s+='1'
			p.append(int(a[i])+1)
		else:
			if p[-1]==1 and a[i]=='1':
				s+='1'
				p.append(int(a[i])+1)
			elif p[-1]==1 and a[i]=='0':

				s+='0'
				p.append(int(a[i])+0)
			elif p[-1]==0:
				s += '1'
				p.append(int(a[i]) + 1)
			elif p[-1]==2 and a[i]=='1':
				s+='0'
				p.append(int(a[i])+0)
			else:
				s+='1'
				p.append(int(a[i])+1)
	print(s)




