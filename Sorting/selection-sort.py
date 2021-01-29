arr = [5,2,1,4,15,19,0,22]
def swap(i,min_index,given_array):
    temp = given_array[i]
    given_array[i] = given_array[min_index]
    given_array[min_index] = temp

def selection_sort(given_array):
    for i in range(len(given_array)):
        min_index = i 
        for j in range(i+1,len(given_array)):
            if given_array[j] <= given_array[min_index]:
                min_index = j
        swap(i,min_index,given_array)
    return given_array

result = selection_sort(arr)
print(result)