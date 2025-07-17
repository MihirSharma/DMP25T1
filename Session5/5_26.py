# series sum

# Setting the start and of series
start = 1
end = 99

# creating variables for loop
numerator = start
result = 0

# entry controlled loop checking until numerator < 99
while numerator < end:
    
    # update denominator at every iteration before calculation
    denominator = numerator + 2
    
    # calculate and add to result
    result += numerator / denominator
    
    # update numerator for next iteration
    numerator += 2

print (result)