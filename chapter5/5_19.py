user_ip = int(input("Enter the number of lines : "))

for i in range(user_ip):  # loop from 0 to 6 to print each line
    # print(" "*user_ip + "i+1")
    space_num = (user_ip-i-1)   # Calculate the number of spaces to be added on either side
    num_str = "1"  # string for center 1
    append_str_1 = ""  #  placeholder string variable for left side numbers
    append_str_2 = ""  #  placeholder string variable for right side numbers
    for j in range(i,0,-1):  # generate left side numbers using a loop that runs from existing value of i to the 0
        append_str_1 += str(j+1) + "\t"     #add generated number (j+1 because j will be 1 short of required number)
    for j in range(i):  # generate right side numbers using a loop that runs from 0 to the existing value of i
        append_str_2 += "\t" + str(j+2)     #add generated number (j+2 because j will be 2 short of required number)
    main_str = space_num*"\t" + append_str_1 + num_str + append_str_2 + space_num*"\t"  #concat left spaces, left string, number string, right string and right spaces
    print(main_str)  #print output line by line

    #We use /t (tab sapce) because that auto alligns the output based on spaces taken by the numbers

    