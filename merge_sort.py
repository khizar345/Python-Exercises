def merge_sort(array):
    #to make sure that the length of the array is greater than 1 because more than 1 element is required for sorting
    if len(array) > 1:
        #slicing the array in almost half and storing the two sides in two different arrays
        left_array = array[:len(array)//2]
        right_array = array[len(array)//2:]
        
        #recursing both halves until all the elements are stored independently in their arrays
        merge_sort(left_array)
        merge_sort(right_array)
        
        #defining variables for indices of the arrays
        i = 0
        j = 0
        k = 0
        
        #comparing all the elements with each other and then storing them in the original array in a sorted manner.
        #The while loop runs through each element until it reaches its length.
        while i < len(left_array) and j < len(right_array):
            #Since the variables defined earlier for the indices start from 0, the left most element of the arrays will be checked.
            #If the element at a specified index (staring from 0) in left array is less than the one in right array, then the 
            #element in the original array will be overridden with the lesser value
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                #incrementing the variable of the index to jump to the next element in the array
                i += 1
                #also incrementing this index in order to override the next element of the original array with lesser value
                #k += 1
                #the same principle is applied when there is an element in the right array that is of lesser value than the one in left array
            else:
                array[k] = right_array[j]
                j += 1
                #since the variable k is incremented two times it can be added to the while loop for it run everytime instead of the if statement 
                #k += 1
            k += 1
            
        #any leftover elements of the left array after the comparison with right array are also added to the original array
        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1
        #and vice versa
        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1
            

some_array = [10,9,8,3,54,7,5,4,32,5,7,9]
print(some_array)
merge_sort(some_array) 
print(some_array)