# 2019112018 원규진

print('2019112018 원규진')
print('문제3-1 순환적 합병정렬\n')

# 합병 함수
# 두 리스트를 합병하여 정렬된 하나의 리스트로 반환한다.
def merge(left, right):
    merged = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1
    merged += left[l:]
    merged += right[r:]
    print(merged)
    return merged

# 순환적 합병정렬
# 리스트의 가운데 요소를 기준으로 왼쪽과 오른쪽으로 나누는 것을 반복하고
# 나눈 리스트를 다시 정렬하여 합치는 것을 순환적으로 반복하며 진행한다.
def recursiveMergeSort(arr):
    print(arr)
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    left_arr = recursiveMergeSort(arr[:mid])
    right_arr = recursiveMergeSort(arr[mid:])
        
    merged = merge(left_arr, right_arr)
    return merged
          
# 비순환적 합병정렬
# 리스트의 앞에서부터 두 쌍씩 정렬하여 합치는 것을 반복하며 진행한다.
def mergeSort(arr):
    merged = [[n] for n in arr]
    
    while len(merged) > 1:
        temp = []
        for i in range(0, len(merged), 2):
            if i+1 < len(merged):
                temp.append(merge(merged[i], merged[i+1]))
            else:
                temp.append(merged[i])
        merged = temp
        print(*merged)
    
A = [30, 20, 40, 35, 5, 50, 45, 10, 25, 15]

recursiveMergeSort(A)
# mergeSort(A)
