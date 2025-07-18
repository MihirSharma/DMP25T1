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
    
