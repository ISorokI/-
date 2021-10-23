import random
def a (q):
   for i in range(1,N):
       if q[i] < q[i-1]:
           return False
   return True
L = []
N=int(input())
for i in range(N):
    L.append(random.randint(0, 1000))
while a(L) != True:
    random.shuffle(L)
print(L)