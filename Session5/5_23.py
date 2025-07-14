loan_amount = float(input("Enter loan amount : "))
loan_term = int(input("Enter number of years as an integer : "))

int_rate = "{:<10}".format("Interest Rate")
m_payment = "{:<10}".format("Monthly Payment")
total_amt = "{:<10}".format("Total Payment")

print(f"{int_rate} {"\t"*2} {m_payment} {"\t"} {total_amt}")

for itr in range(25):
    i = (5+float(float(itr)/8))/100 # calculate rate based on itr (iterating variable)
    emi = loan_amount * ((i/12) * ((1+(i/12))**(loan_term*12))) / (((1+i/12)**(loan_term*12)) - 1) # this is just the formula
    rate_str = f"{round(i*100,3):<10.3f}" # f-string : left align, 10 spaces and 3 decimals
    emi_str = f"{round(emi, 2):^12.2f}" # f-string : center align, 12 spaces and 2 decimals
    total = f"{round(emi*loan_term*12,2):^12.2f}" # f-string : center align, 12 spaces and 2 decimals
    print(f"{rate_str} {"\t"*2} {emi_str} {"\t"*2} {total}")