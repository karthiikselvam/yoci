arr = [5,2,1,4,15,19,0,22]
def swap(j,j_prev,given_array):
    given_array[j],given_array[j_prev] = given_array[j_prev],given_array[j]

def insertion_sort(given_array):
    for i in range(len(given_array)):
        for j in range(i,-1,-1):
            if (j-1 >=0) and (given_array[j] <= given_array[j-1]):
                swap(j,j-1,given_array)
    return given_array

result = insertion_sort(arr)
print(result)
            
