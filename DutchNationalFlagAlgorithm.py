def detch_national_flag(arr:list[int]) ->list[int]:
    low = 0
    mid = 0
    high = len(arr)-1

    while mid <= high:
        if arr[mid] == 0:   # if 0 then move it to the left of the array
            arr[mid],arr[low] = arr[low],arr[mid]
            low +=1
            mid +=1
        elif arr[mid] == 1:  # if 1 then jsut increment the mid, keep the 1's at center
            mid += 1
        else:                 # if 2 then move it to the right of the array
            arr[mid],arr[high] = arr[high],arr[mid]
            high -=1

    return arr


arr = [0,1,1,0,2,0,1,2]
sorted_arr = detch_national_flag(arr)
print(f'Sorted array: {sorted_arr}')


# output:
# Sorted array: [0, 0, 0, 1, 1, 1, 2, 2]
