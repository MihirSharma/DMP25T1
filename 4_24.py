user_ip = input("Enter a letter : ")

# if(user_ip == 'a' or user_ip == 'A' or user_ip == 'e' or user_ip == 'E' or user_ip == 'i' or user_ip == 'I' or user_ip == 'o' or user_ip == 'O' or user_ip == 'u' or user_ip == 'U'):
#     print(f"{user_ip} is a vowel.")
# else:
#     print(f"{user_ip} is a consonant.")

vowel = False

match user_ip:
    case 'a':
        vowel = True
    case 'A':
        vowel = True
    case 'e':
        vowel = True
    case 'E':
        vowel = True
    case 'i':
        vowel = True
    case 'I':
        vowel = True
    case 'o':
        vowel = True
    case 'O':
        vowel = True
    case 'u':
        vowel = True
    case 'U':
        vowel = True

if(vowel):
    print(f"{user_ip} is a vowel.")
else:
    print(f"{user_ip} is a consonant.")