import math
for _ in range(int(input())):
               n=int(input())
               s=n/2
               if n%2==0:
                   print(int(s-1))
               else:
                   s=int(math.ceil(s))
                   print(s)