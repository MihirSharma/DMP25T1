# Prompt user for input
deposit = float(input("Enter the initial deposit amount: "))
annual_rate = float(input("Enter annual percentage yield: "))
months = int(input("Enter maturity period (number of months): "))

# Convert annual rate to monthly rate
monthly_rate = (annual_rate / 100) / 12

# Print table header
print()
print("%-10s%10s" % ("Month", "CD Value"))
print()

# Initialize counter
count = 1

# Loop through each month and calculate new value
while count <= months:
    deposit = deposit + (deposit * monthly_rate)
    print("%-10d%10.2f" % (count, deposit))
    count += 1
