def combinedResistanceParallel(r1,r2,r3):
    try:
        return round((r1*r2*r3)/(r1*r2+r2*r3+r3*r1),6)
    except:
        return -1
print("%1.6e"% combinedResistanceParallel(r1,r2,r3))