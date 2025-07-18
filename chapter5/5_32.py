# Take required inputs
amount = float(input("Amount to be saved: "))
rate = float(input("Annual Interest Rate: "))
months = int(input("Number of months: "))

# Set variable for loop to check until last month
count = 0

# Set variable to calculate final value
final = 0

while count < months:
    # multiply amount by rate and set is as final   
    final = amount*(1 + (rate/100)/12)
    
    # change amount to final + amount for next iteration
    amount = final + 100
    
    # increment count
    count += 1

# print final value
print ("After ", months, "months: ", final)
