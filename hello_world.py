arr = [8,5,6,1,9,0,2,7,3,4]
newarr = []

def insertSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j+1] < arr[j]:
                newarr.append(i)
                    
    return newarr
print(insertSort(arr))     