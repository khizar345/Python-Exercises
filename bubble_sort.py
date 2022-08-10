def bubbleSort(arr):
    n = len(arr)  
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        #go all the way until second last element to compare two values at the indices
        for j in range(n-1-i):
            # traverse the array from 0 to n-1-i, since the last elements are already sorted the loop will not go through them in succeding iteration
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
somearray=[5,4,3,2,1,6,10,9,8,7]
bubbleSort(somearray)
print(somearray)