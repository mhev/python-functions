# 1 
def biggie_size(arr):
    for a in range (len(arr)):
        if arr[a] > 0:
            arr[a] = "big"
    return arr
        
print(biggie_size([-1,3,5,-5]))

# 2 
def countPositives(arr):
    count = 0
    for val in arr:
        if val > 0:
            count += 1
    arr[len(arr)-1] = count
    return arr
print(countPositives([-1,1,1,1]))

# 3 
def sum_total(arr):
    sum = 0
    for val in arr:
        sum = sum + val
    return sum
    
print(sum_total([1,2,3,4]))

# 4 

def average(arr):
    sum = 0
    for val in arr:
        sum = sum + val
    avg = sum/(len(arr))
    print(avg)
average([1,2,3,4])

# 5 

def listLen(arr):
   return len(arr)
print(listLen([1,2,3,4,5]))

# 6

def lowestNumber(arr):
    myMin = arr[0]
    for num in arr:
        if myMin > num:
            myMin = num
    return myMin


print(lowestNumber([37,2,1,-9]))

# 7

def highestNumber(l):
    myMax = l[0]
    for num in l:
        if myMax < num:
            myMax = num
    return myMax


print(highestNumber([37,2,1,-9]))

# 8

def ultimate(arr):
    min = arr[0]
    max = arr[0]
    sum = 0

    for val in arr:
        if val < min:
            min = val
        if val > max:
            max = val
        sum += val
    d = {"sumTotal": sum, "avg": sum/len(arr), "min": min, "max": max, "length": len(arr),}
    return d
print(ultimate([37,2,1,-9]))

# 9

def reverseList(arr):
    for i in range(len(arr)//2):
        temp = arr[i]
        arr[i] = arr[len(arr)-1-i]
        arr[len(arr)-1-i] = temp
    return arr
print(reverseList([1,2,3,4,5]))