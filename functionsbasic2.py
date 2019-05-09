# 1
def countdown(num):
    for x in range(num, 0, -1):
        print(x)
countdown(5)

# 2

def print_and_return(arr):
    print (arr[0])
    return arr[1]
print_and_return([5, 10])

# 3

def first_plus_length(arr):
    return arr[0] + len(arr)
print (first_plus_length([1,2,3,4,5]))

# 4 

def values_greater_than_second(arr):
    newarr = []
    second = arr[1]
    count = 0
    for val in arr:
        if val > second:
            count += 1
            newarr.append(val)
    print(count)
    return newarr
print(values_greater_than_second([5,2,3,2,1,4]))

# 5 

def length_and_value(b,c):
    newarr = []
    size = b
    value = c
    for i in range(1, b+1):
        newarr.append(c)
    return newarr
    
print(length_and_value(4,7))
print(length_and_value(6,2))