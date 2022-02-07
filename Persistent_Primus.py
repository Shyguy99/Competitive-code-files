
import time
from colorama import Fore, Back, Style
import random

time.sleep(5)
t=time.time()
col=[Fore.CYAN,Fore.RED,Fore.BLACK,Fore.YELLOW,Fore.BLUE,Fore.MAGENTA,Fore.GREEN,Fore.WHITE,Fore.LIGHTRED_EX,Fore.GREEN,Fore.CYAN]
while time.time()-t<2:
    print(col[0]+"PLACEMENT SEASON STARTED")
    print("😰"*3)
    time.sleep(0.3)
t=time.time()


while time.time()-t<2:
    print(col[1]+"REJECTED FROM X COMPANY")
    print("😭"*4)
    time.sleep(0.3)
t=time.time()

while time.time()-t<2:
    print(col[2]+"SELECTED IN Y COMPANY BUT NOT SATISFIED")
    print("😭"*2)
    time.sleep(0.3)
t=time.time()

while time.time()-t<2:
    print(col[3]+"REJECTED FROM Z COMPANY")
    print("😭"*4)
    time.sleep(0.3)
t=time.time()

while time.time()-t<2:
    print(col[4]+"REJECTED FROM B COMPANY")
    print("😭"*10)
    time.sleep(0.3)
t=time.time()

while time.time()-t<2:
    print(col[5]+"PERSISTENT ON CAMPUS")
    print("🥺"*6)
    time.sleep(0.3)
t=time.time()

while time.time()-t<2:
    print(col[6]+"CLEARED ROUND 1 OF PERSISTENT!!")
    print("😀"*6)
    time.sleep(0.3)
t=time.time()

while time.time()-t<2:
    print(col[7]+"CLEARED TECHNICAL INTERVIEW!!")
    print("😀"*12)
    time.sleep(0.3)
t=time.time()

while time.time()-t<2:
    print(col[8]+"CLEARED FINAL ROUND!!")
    print("😀"*16)
    time.sleep(0.3)
t=time.time()

while time.time()-t<2:
    print(col[9]+"RECEIVED OFFER LETTER!!!!")
    print("🤩"*16)
    time.sleep(0.3)
t=time.time()

while time.time()-t<2:
    print(col[10]+"EXCITED TO JOIN PERSISTENT!!")
    print("🥳🎊"*16)
    time.sleep(0.3)
t=time.time()

while time.time()-t<2:
    print(col[5]+"THANK YOU PERSISTENT FOR GIVING ME THIS GREAT OPPORTUNITY!!!")
    print("😊"*16)
    time.sleep(0.3)
t=time.time()
o=[[" " for i in range(61)]for j in range(7)]
ch="#"
o[3][10]=ch

o[3][7]=ch

o[4][5]=ch
o[5][4]=ch
o[6][5]=ch
o[6][7]=ch
o[5][10]=ch
o[4][10]=ch

o[2][10]=ch
o[1][10]=ch
o[0][13]=ch
o[0][15]=ch
o[1][16]=ch
o[2][15]=ch
o[3][13]=ch
print(col[2]+"")
for i in range(7):
    for j in range(61):
        print(Fore.YELLOW+Fore.RED+o[i][j],end="")
    print()

print(Fore.BLACK+"   PERSISTENT")
print(Fore.BLACK+Fore.WHITE+"See Beyond, Rise Above")