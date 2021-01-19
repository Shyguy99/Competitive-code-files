def SieveOfEratosthenes(n):
	global all_p
	prime = [True for i in range(n + 1)]
	p = 2
	while (p * p <= n):


		if (prime[p] == True):

			for i in range(p * p, n + 1, p):
				prime[i] = False
		p += 1

	# Print all prime numbers
	for p in range(2, n + 1):
		if prime[p]:
			all_p.append(p)
all_p=[]
SieveOfEratosthenes(3*10000)
for _ in range(int(input())):
	d=int(input())


	def next(arr, target):
		start = 0
		end = len(arr) - 1

		ans = -1
		while (start <= end):
			mid = (start + end) // 2

			# Move to right side if target is
			# greater.

			if (arr[mid] < target):
				start = mid + 1

			# Move left side.
			else:
				ans = mid
				end = mid - 1

		return ans
	d1=all_p[next(all_p,1+d)]
	d2=all_p[next(all_p,d1+d)]
	print(d1,d2)
