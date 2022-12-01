# 2019112018 원규진
print('2019112018 원규진')
print('막대자르기\n')

def CutRod(p, n):
    if n==0: return 0
    
    q = float('-inf')
    for i in range(1, n+1):
        q = max(q, p[i]+CutRod(p, n-i))
    
    return q

def MemorizedCutRod(p, n):
    r = [float('-inf')]*(n+1)
    return MemorizedCutRodAux(p, n, r)

def MemorizedCutRodAux(p, n, r):  
    if r[n]>=0: 
        return r[n]
    if n==0: 
        q = 0
    else:
        q = float('-inf')
        for i in range(1, n+1):
            q = max(q, p[i]+MemorizedCutRodAux(p, n-i, r))
    r[n] = q
    print(r)
    
    return q


price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

# print(CutRod(price, 4))
print(MemorizedCutRod(price, 10))