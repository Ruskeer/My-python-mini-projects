import random
import math


alpha = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
special = "@#$%&*"

pass_len = int(input("Enter length of password you desire: "))

alpha_len = pass_len // 2

num_len = math.ceil(pass_len * 30/100)

special_len = pass_len - (alpha_len + num_len)

password = []


def generate(length, array, is_alpha = False):

    for i in range(length):
         index = random.randint(0, len(array) - 1)

         this_pass = array[index]

         if is_alpha:
             flipped = random.randint(0,1)
             if flipped == 1:
                 this_pass = this_pass.upper()
        
         password.append(this_pass)


generate(alpha_len, alpha, True)

generate(num_len, num)
generate(special_len, special)


random.shuffle(password)

generated_pass = ""

for p in password:
    generated_pass = generated_pass + str(p)

print(f"Your generated password is: {generated_pass}")
    
    
         
        











































