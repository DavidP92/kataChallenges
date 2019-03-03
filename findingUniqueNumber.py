##First we sort the array with .sort() command
##Now we will check the first place holder in the array with the last and second to last place holder within the first if statement
##Else, out of elimations, we know that the it must be in the last place holder due to only the array containing 1 unique number
## Finally, we print the uniq number of the array

def find_uniq(array):
    array.sort()            
    if array[0] != array[len(array)-1] and array[0] != array[len(array)-2]:
        uniq = array[0]    
    else: 
        uniq = array[len(array)-1] ## So store the value in uniq
    return uniq


##Second Solution
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b
