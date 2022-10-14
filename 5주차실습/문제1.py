# 2019112018 원규진
print('2019112018 원규진')
# print('문제1-1 최소값과 최대값 찾기\n')
print('문제1-2 동시에 최소값과 최대값 찾기\n')

import random

# 최소값 찾기
def Minimum(arr):
    result = arr[0]
    for i in range(len(arr)):
        if result > arr[i]: # 더 작다면 대입
            result = arr[i]
    return result

# 최대값 찾기
def Maximum(arr):
    result = arr[0]
    for i in range(len(arr)):
        if result < arr[i]: # 더 크다면 대입
            result = arr[i]
    return result

# 동시에 최소값과 최대값 찾기
def FindMinMax(arr):
    mini = arr[0]
    maxi = arr[0]
    for i in range(0, len(arr)-1, 2):
        if arr[i] < arr[i+1]: # 원소 쌍끼리 먼저 비교
            small = arr[i]
            large = arr[i+1]
        else:
            small = arr[i+1]
            large = arr[i]
        if small < mini: mini = small
        if large > maxi: maxi = large
    return [mini, maxi]


A = [random.randrange(1, 10000) for _ in range(1000)]

# min = Minimum(A)
# max = Maximum(A)
min, max = FindMinMax(A)
print('최소:', min, '최대:', max)
print()
print(A)