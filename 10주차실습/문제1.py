# 2019112018 원규진
print('2019112018 원규진')
print('두 직선의 교차 여부\n')

def Intersection(AB, CD):
    if (Direction(AB[0], AB[1], CD[0])*Direction(AB[0], AB[1], CD[1]) <= 0) and (Direction(CD[0], CD[1], AB[0])*Direction(CD[0], CD[1], AB[1]) <= 0):
        return True
    else:
        return False

def Direction(A, B, C):
    dxAB, dyAB = B[0] - A[0], B[1] - A[1]
    dxAC, dyAC = C[0] - A[0], C[1] - A[1]
    
    if dxAB*dyAC < dyAB*dxAC:
        return 1
    if dxAB*dyAC > dyAB*dxAC:
        return -1
    if dxAB*dyAC == dyAB*dxAC:
        if (dxAB == 0) and (dyAB == 0):
            return 0
        if (dxAB*dxAC < 0) or (dyAB*dyAC < 0):
            return -1
        elif (dxAB*dxAB + dyAB*dyAB) >= (dxAC*dxAC + dyAC*dyAC):
            return 0
        else:
            return 1

print("1)", end=" ")
print(Intersection([(2, 1), (-1, 3)], [(-1, 1), (2, 3)]))

print("2)", end=" ")
print(Intersection([(-3, 0), (1, 1)], [(-4, 1), (-6, 3)]))

print("3)", end=" ")
print(Intersection([(-2.2, 0), (0, 3.3)], [(-1, 4), (-0.5, -2.3)]))