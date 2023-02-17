import random
sample_size=8
p1 = [random.randint(0,1) for _ in range(sample_size)]
p2 = [random.randint(0,1) for _ in range(sample_size)]
p3 = [random.randint(0,1) for _ in range(sample_size)]
p4 = [random.randint(0,1) for _ in range(sample_size)]
p5 = [random.randint(0,1) for _ in range(sample_size)]

print("p1: "+str(p1))
print("p2: "+str(p2))
print("p3: "+str(p3))
print("p4: "+str(p4))
print("p5: "+str(p5))

fp1 = p1.count(1)
fp2 = p2.count(1)
fp3 = p3.count(1)
fp4 = p4.count(1)
fp5 = p5.count(1)

cie = random.randint(1,8)
print("Limite es " + str(cie))


print("fp1: "+str(fp1))
print("fp2: "+str(fp2))
print("fp3: "+str(fp3))
print("fp4: "+str(fp4))
print("fp5: "+str(fp5))

def cierre (fpx, cie, n):
    if (fpx < cie):
        print("fp"+str(n) + " fue eliminado")

cierre(fp1, cie, 1)
cierre(fp2, cie, 2)
cierre(fp3, cie, 3)
cierre(fp4, cie, 4)
cierre(fp5, cie, 5)

