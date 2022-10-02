# 2019112018 원규진
import random

# [선택정렬]
# 오름차순으로 정렬한다고 할 때, 리스트에서 최소값을 찾아 0번째 
# 값과 자리바꿈한다. 자리바꿈이 되었으면 정렬이 완료되었다고 
# 판단하고 그 다음 인덱스부터 나머지 리스트에서 최소값을 찾아 
# 해당 인덱스의 값과 자리바꿈하고 이를 반복한다.

def selectionSort(arr, cnt):
    # 길이 n의 배열은 최대 n-1번 정렬해야함
    for i in range(len(arr)-1):
        # 최소값의 인덱스
        minIdx = i
        # 정렬이 완료된 i번째 이후로 부터 다시 최소값 찾기
        for j in range(i+1, len(arr)):
            # 현재 최소값보다 작은 값을 발견시 minIdx 업데이트
            if arr[j] < arr[minIdx]:
                minIdx = j
        # 발견한 최소값과 그 값이 들어갈 위치의 값을 swap
        if minIdx != i:
            arr[i], arr[minIdx] = arr[minIdx], arr[i]
            cnt = cnt+1
            print(cnt, arr)
            
            
A = [random.randrange(1, 1000) for _ in range(100)]
cnt = 0

print('A =', A)
selectionSort(A, cnt)