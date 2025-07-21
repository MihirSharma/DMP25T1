# print first 50 prime numbers
def isPrime(num):
    mid = int(num ** 0.5) + 1
    for i in range (2, mid):
        if num % i == 0:
            return False
    return True

count = 0
num = 2
while count < 50:
    if isPrime(num):
        print (count+1, num)
        count += 1
    num += 1
    
# 5.22
# print primes between 1000 & 2000 in list of 10 nums

def isPrime(num):
    mid = int(num ** 0.5) + 1
    for i in range (2, mid):
        if num % i == 0:
            return False
    return True

num = 1000
tenCount = 0
primes = 0
while num < 2000:  
    if isPrime(num):
        print (num, end = " ")
        tenCount += 1
        primes += 1
        if tenCount == 10:
            print ("")
            tenCount = 0
    num += 1
print ("\nPrimes between 1000 & 2000: ", primes)
    

    
    