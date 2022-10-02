# 2019112018 원규진
import random

print('2019112018 원규진')
print('문제1-2 비순환적 퀵정렬\n')

# 파티션 함수
# 피봇을 기준으로 작은 값은 왼쪽 리스트로, 큰 값은 오른쪽 리스트로 옮긴다.
def partition(arr, start, end):
    pivot = arr[start]
    left, right = start+1, end
    while True:
        while left <= right and arr[left] >= pivot:
            left += 1
        while left <= right and arr[right] < pivot:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            print(arr) 
        else: break
    arr[start], arr[right] = arr[right], arr[start]
    print(arr)
    return right

# 순환적 퀵정렬
# 피봇의 위치를 기준으로 왼쪽과 오른쪽 리스트를 순환적으로 호출하여 정렬한다.
def recursiveQuickSort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        recursiveQuickSort(arr, 0, pivot-1)
        recursiveQuickSort(arr, pivot+1, end)
      
# 비순환적 퀵정렬
# 범위의 시작과 끝 인덱스를 스택에 넣고 파티션함수에 사용하면서 정렬한다.
def quickSort(arr, start, end):
    stack = []
    stack.append(start)
    stack.append(end)
    
    while stack:
        end = stack.pop()
        start = stack.pop()
        pivot = partition(arr, start, end)
        if pivot-1 > start:
            stack.append(start)
            stack.append(pivot-1)
        if pivot+1 < end:
            stack.append(pivot+1)
            stack.append(end)
    
A = [random.randrange(1, 10000) for _ in range(10)]

# recursiveQuickSort(A, 0, len(A)-1)
quickSort(A, 0, len(A)-1)