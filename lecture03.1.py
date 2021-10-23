try:
    N = int(input('Введите число больше нуля '))
except:
    print('Это не число')
    exit()
if N<0:
    print('Не то число')
    exit()
L=[]
p=2
for i in range(0, N+1):
    L.append(i)
while p+2 < N ** 1/2:
    for t in range(p*p, N+1, p):
        L[t]=0
    p+=1
    while L[p]==0:
        p+=1
for i in L:
    if i>0:
        print(i)
