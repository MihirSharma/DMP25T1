x = input("Enter a 4 digit number : ")

if(int(x)):
    y = x[::-1]
    print(y)

num = int(x)

var2 = num//1000 + ((num%1000)//100)*10 + ((num%100)//10)*100 + (num%10)*1000

print(var2)