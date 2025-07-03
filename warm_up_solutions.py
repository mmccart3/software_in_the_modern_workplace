dataset = [34,67,5,81,2,45,9,23,55,41,42,84,109, 109, 109]


#? ------------------------------------------------------
#?                      Task 1                          |
#?              A function for the Mean                 |
#? ------------------------------------------------------

def find_mean(data):
    #* sum() function adds up all the values and returns the result. We refer to this as "total"
    total = sum(data)
    #* find the length of the data set
    count = len(data)
    #* divide - no need for floor division, the number can be fractional
    mean = total / count
    return mean

print("The mean of the datset is:", find_mean(dataset))

#? ------------------------------------------------------
#?                      Task 2                          |
#?             A function for the Median                |
#? ------------------------------------------------------

def find_median(data):
    #* sorted() function sorts the data in ascending order
    sorted_data = sorted(data)
    #* find the length of the sorted data
    length = len(sorted_data)
    #* divide the length by 2, which we then use for index position 
    #* // rounds down to the nearest whole number. 

    middle = length // 2
    #* for a dataset of length 6, 6/2 = 3 - but we know that isn't the middle value, so we also need to go to index position 2 and find their mean
    #* 0  1  2  3  4  6
    #* 1  3  5  6  6  8
    if length % 2 == 0:
        median = (sorted_data[middle - 1] + sorted_data[middle]) / 2
    else:
    #* for a dataset of length 5, 5/2 = 2.5 but floored 5//2 = 2, giving us our middle value as the thing at index position 2
    #* 0  1  2  3  4
    #* 1  3  5  6  6  
        median = sorted_data[middle]
    
    return median

print(find_median(dataset))

#? ------------------------------------------------------
#?                      Task 2                          |
#?             A function for the Mode                |
#? ------------------------------------------------------

def find_mode(data):
    # Dictionary to store the frequency of each value (key = the number in the dataset, value = number of times it appears)
    frequency_counts = {}
    
    # Count the occurrences of each value in the dataset
    for item in data:
        if item in frequency_counts:
            frequency_counts[item] += 1
        else:
            frequency_counts[item] = 1
    # Find the maximum frequency
    max_count = max(frequency_counts.values())
    
    # Collect all values that have the maximum frequency
    modes = [key for key, count in frequency_counts.items() if count == max_count]
    
    # Check if every value has the same frequency (no mode)
    if len(modes) == len(frequency_counts):
        return None  # No mode in the dataset (you can change this to "No mode" or any other placeholder)
    elif len(modes) == 1:
        return modes[0]  # Only one mode found, return it
    else:
        return modes  # Multiple modes found, return them as a list
    
print(find_mode(dataset))