import random
sample_size=8
p1 = [random.randint(0,1) for _ in range(sample_size)]
p2 = [random.randint(0,1) for _ in range(sample_size)]
print("p1: "+str(p1))
print("p2: "+str(p2))

c11 = []
c12 = []

n = random.randint(1,7)
n2 = 8 - n
print(n)

for x in range(n):
    c11.append(p1[x]) 

# c11.append(7)

for x in range(n2):
    c11.append(p2[x]) 

print("c11: "+str(c11))
