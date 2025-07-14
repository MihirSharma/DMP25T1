for i in range(6): # loop from 0 to 5 to print line by line
    line_str = "" # intialize an empty string variable. This will represent the line
    for j in range(i+1): #nested loop from 0 to i to generate line numbers
        line_str += (str(j+1) + "\t") # appending line numbers to the empty string variable one by one
    print(f"{line_str} \n") # print output

print("-"*50 + "\n")

#==================================================================================

for i in range(6,0,-1): # loop reversed to generate line from 6 to 1
    line_str = ""
    for j in range(i):
        line_str += (str(j+1) + "\t")
    print(f"{line_str} \n")

print("-"*50 + "\n")

#==================================================================================

for i in range(6):
    line_str = "\t"*(5-i) # allows us to add required spaces preceding numbers
    for j in range(i+1):
        line_str += (str(i-j+1) + "\t") # gives us reverse ordered numbers
    print(f"{line_str} \n")

print("-"*50 + "\n")

#==================================================================================

for i in range(6):
    line_str = "\t"*i
    for j in range(6-i):
        line_str += (str(j+i+1) + "\t")
    print(f"{line_str} \n")
