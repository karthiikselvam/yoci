arr = [1,2,3,5,6,7,8,9,11]
target = 4

def binarysearch(arr, target):
    low = 0
    high = len(arr)-1
    
    while (low <= high):
        mid = low + (high-low) // 2  
        if arr[mid] < target:
            low = mid + 1 
        elif arr[mid] > target :
            high = mid - 1
        else:
            return arr[mid]


result = binarysearch(arr,8)
print(result)


