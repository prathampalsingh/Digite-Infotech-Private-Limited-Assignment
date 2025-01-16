N = int(input("Enter the number of elements you want to input: ")) 
#This line creates an empty array list 
arr = []
# This line begins a for loop that will iterate N times
for _ in range(N):
    element = input("Enter element: ")
    #This line adds the element entered by the user to the end of the arr list using the append() method
    arr.append(element)

#This line prints the entire array list
print("Your array:", arr)

# Sort the array in ascending order
for i in range(len(arr)):
    #It iterates from the index i + 1 to the end of the array
    for j in range(i + 1, len(arr)):
        #This line checks if the element at index i is greater than the element at index j
        if arr[i] > arr[j]:
            # Swap the elements
            arr[i], arr[j] = arr[j], arr[i]

# After the sorting process, this line accesses the third-smallest element in the array.
third_smallest = arr[2]

print("The 3rd smallest number is:", third_smallest)
