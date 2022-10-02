# 2019112018 원규진
print('2019112018 원규진')
print('문제1-1 순환적 버블정렬\n')

def bubbleSort(arr, cnt):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                cnt = cnt+1
                print(cnt, arr)
    
        
def recursiveBubbleSort(arr, cnt):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            cnt = cnt+1
            print(cnt, A)
            recursiveBubbleSort(arr, cnt)


A = [30, 20, 40, 10, 5, 10, 30, 15]

# bubbleSort(A, 0)
recursiveBubbleSort(A, 0)