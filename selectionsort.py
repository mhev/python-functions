arr = [8,5,6,1,9,0,2,7,3,4]

def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubbleSort(arr))