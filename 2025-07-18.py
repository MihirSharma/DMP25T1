# multiplication using while
i = 1
while (i < 11):
    j = 1
    while (j < 11):
        print (i * j, end = " ")
        j += 1
    print ()
    i += 1

# multiplication using for
for i in range (1,11):
    for j in range (1,11):
        print (i * j, end = " ")
    print ()
    
# gcd using while
def calgcd(n1, n2):
    k = 2
    gcd = 1
    while (n1 >= k and n2 >= k):
        if n1 % k == 0 and n2 % k == 0:
            gcd = k
        k += 1
    return gcd

gcd = calgcd (5,3)
print (gcd)
gcd = calgcd (20,5)
print (gcd)

# gcd using for
def calgcdf(n1,n2):
    gcd = 1
    k1 = min(n1,n2)
    for k in range (2,k1+1):
        if n1 % k == 0 and n2 % k == 0:
            gcd = k
    return gcd

gcd = calgcdf (2,4)
print (gcd)
gcd = calgcdf (20,5)
print (gcd)

# years to double tuition using while

def yearsToDouble (tuition):
    counter = 0
    while (counter < 20):
        if tuition > 20000:
            print (counter)
            break
        tuition *= 1.07
        counter += 1
    return counter, tuition
n1 = yearsToDouble(100000)
print (n1)

# years to double tuition using for

def yearsToDoubleF (tuition):
    for counter in range (21):
        if tuition > 20000:
            print (counter)
            break
        tuition *= 1.07
    return counter, tuition
n1 = yearsToDoubleF(100000)
print (n1)

# add all number till n but for 10, 11

def addall (n):
    counter = 0
    total = 0
    while counter < n:
        counter += 1
        if counter == 10 or counter == 11:
            continue
        total += counter
    print (total, counter)

addall(11)
addall(12)

# add all number till n but for 10, 11 using for

def addallf (n):
    total = 0
    for counter in range (1, n+1):
        if counter == 10 or counter == 11:
            continue
        total += counter
    print (total, counter)

addallf(11)
addallf(12)

# palindrome using while 

string = input("String")
reversed = ""
counter = 0
end = len(string)
while counter < end:
    character = string[counter]
    reversed = character + reversed
    counter += 1
if reversed == string:
    print (True)
else:
    print (False)