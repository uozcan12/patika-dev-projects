# Function to do insertion sort
def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key     
    return arr
 
 
# Driver code to test above
arr = [22,27,16,2,18,6]
sorted_arr = insertionSort(arr)
for i in range(len(sorted_arr)):
    print ("% d" % arr[i])
     #2
	 #6
	 #16
	 #18
	 #22
	 #27

print("The time complexity is O(n^2)")
	
arr = [7,3,5,8,2,9,4,15,6]
sorted_arr = insertionSort(arr)
for i in range(len(sorted_arr)):
    print ("% d" % arr[i])
    
    

