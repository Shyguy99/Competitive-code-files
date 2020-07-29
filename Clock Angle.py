t=int(input())
lo=float(input())
f=((t/360)*lo)%12
h=int(f)
m=((f-h)*60)
a1=(h*30)+m*0.5
a2=m*6
diff=(abs(a1-a2))
if diff>180:
    diff=360-diff
print("{:.2f}".format(diff))