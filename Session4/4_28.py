user_ip = input("Enter a string : ")

length = len(user_ip)
last_char = user_ip[-1]
space_count = user_ip.count(" ")

print(f"The length of the string is {length}")
print(f"The last character of the string is {last_char}")
print(f"The number of spaces in the string is {space_count}")