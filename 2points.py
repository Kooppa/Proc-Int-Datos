import random
sample_size=8
p1 = [random.randint(0,1) for _ in range(sample_size)]
p2 = [random.randint(0,1) for _ in range(sample_size)]
print("p1: "+str(p1))
print("p2: "+str(p2))

c21 = []
c22 = []

n = random.randint(1,6)
n0 = random.randint((n+1),7)
n2 = n0 - n
n3 = (8 - n2) - n
print(n)
# print(n2)
print(n2)
print(n3)

for x in range(n):
    c21.append(p1[x]) 

# c11.append(7)

for x in range(n2):
    c21.append(p2[x]) 

# c11.append(7)

for x in range(n3):
    c21.append(p1[x])

print("c22: "+str(c21))
