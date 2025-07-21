# series sum

# Setting the start and of series
start = 1
end = 99

# creating variables for loop
numerator = start
result = 0

# entry controlled loop checking until numerator < 99
# For those confused why this is 99 and not 98, 
# the numerator is added by 2 and not 1 thus our last numerator value will be 99
# And 99 < 99 is False by nature so the loop stops at 97/99 and not at 99/101
while numerator < end:
    
    # update denominator at every iteration before calculation
    denominator = numerator + 2
    
    # calculate and add to result
    result += numerator / denominator
    
    # update numerator for next iteration
    numerator += 2

print (result)