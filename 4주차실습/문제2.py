# 2019112018 원규진
print('2019112018 원규진')
print('문제2-2 힙 정렬\n')

# 힙 생성
def heapify(arr, id, n):
    l = id * 2
    r = id * 2 + 1
    i = id
    if l <= n and arr[i] < arr[l]:
        i = l
    if r <= n and arr[i] < arr[r]:
        i = r
    if i != id:
        arr[id], arr[i] = arr[i], arr[id]
        print(arr)
        return heapify(arr, i, n)
            
# 힙 정렬
def heapSort(arr):
    # 정렬 완료된 노드가 들어갈 리스트
    answer = []
    
    # 최대 힙 생성
    print(arr)
    for i in range((len(arr)-1)//2, 0, -1):
        heapify(arr, i, len(arr)-1)
    print()

    # 힙 정렬 수행
    for i in range(len(arr)-1, 0 , -1):
        answer.append(arr[1])  # 최대 힙을 꺼내 오름차순된 배열을 얻음
        arr[i], arr[1] = arr[1], arr[i]
        heapify(arr, 1, i-1) # 힙 재정비
    print()
    return answer

A = [0, 4, 1, 3, 2, 16, 9, 10, 14, 8, 7]

print("answer:", heapSort(A))
