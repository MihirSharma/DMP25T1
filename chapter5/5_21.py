for i in range(8):  
    space_num = (8-1-i)    
    append_str_1 = ""  
    append_str_2 = ""  
    for j in range(i):  
        append_str_1 += "\t" + "{:>3}".format((2**(j))) 
    for j in range(i,0,-1):  
        append_str_2 += "{:>3}".format((2**(j))) + "\t"     
    
    main_str = space_num*"\t" + append_str_1 + "\t" + "{:>3}".format((2**i)) + "\t" + append_str_2 + space_num*"\t"  #concat left spaces, left string, number string, right string and right spaces
    print(main_str)
    
    # pretty much the same as 5.19 just with the additional formatting added to the strings