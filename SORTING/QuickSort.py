def QuickSort(arr,lb,ub):
    if lb < ub:
        loc = Partition(arr,lb,ub)

        QuickSort(arr,lb,loc-1)
        QuickSort(arr,loc+1,ub)

def Partition(arr,lb,ub):
    pivot = arr[lb]
    start = lb
    end = ub

    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1

        if start < end:
            arr[start],arr[end] = arr[end],arr[start]
    arr[end],arr[lb] = arr[lb],arr[end]

    return end

arr = [10, 7, 8, 9, 1, 5]
QuickSort(arr,lb=0,ub=len(arr)-1)
print(arr)