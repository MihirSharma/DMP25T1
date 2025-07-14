import random

u_num = int(input("Enter a Three digit number : "))

l_num = random.randint(100,999)

ustr = str(u_num)
print(format(u_num))

h_l = l_num//100
t_l = (l_num%100)//10
u_l = (l_num%10)

while(h_l == t_l or h_l == u_l or t_l == u_l): # regen random number in case of digit repetition
    l_num = random.randint(100,999)
    h_l = l_num//100
    t_l = (l_num%100)//10
    u_l = (l_num%10)



h_u = u_num//100
t_u = (u_num%100)//10
u_u = (u_num%10)

# print(h_l, t_l, u_l, h_u, t_u, u_u)

lottery_numbers_set =  set([h_l, t_l, u_l])
user_numbers = [h_u, u_u, t_u]

threeK_prize_check = True
for i in user_numbers:
    if i in lottery_numbers_set:
        lottery_numbers_set.remove(i)
    else:
        threeK_prize_check = False
        break

print("Lottery is ", l_num)

if (h_u == h_l and t_u == t_l  and u_u == u_l ):
    print("$10000")
elif (threeK_prize_check):
    print("$3000")
elif (h_u == (h_l or t_l or u_l) or t_u == (h_l or t_l or u_l) or u_u == (h_l or t_l or u_l)):
    print("$1000")
else:
    print("Sorry, No match")

