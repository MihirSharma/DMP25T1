income = 1500000
tax = 0
surcharge = 0

if(income<300001):
    tax = 0
elif(income<700001):
    tax = (income - 300000)*0.05
elif(income<1000001):
    tax = 20000 + (income - 700000)*0.1
elif(income<1200001):
    tax = 50000 + (income - 1000000)*0.15
elif(income<1500001):
    tax = 80000 + (income - 1200000)*0.2
elif(income<5000001):
    tax = 140000 + (income - 1500000)*0.3
elif(income<10000001):
    tax = 140000 + (income - 1500000)*0.3
    surcharge = tax*0.1
elif(income<20000001):
    tax = 140000 + (income - 1500000)*0.3
    surcharge = tax*0.15
else:
    tax = 187500 + (income - 1500000)*0.3
    surcharge = tax*0.25

print(f"Tax : Rs.{tax} | Surcharge = Rs.{surcharge}")
