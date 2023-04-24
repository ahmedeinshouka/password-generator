
import random
letters=['a','b','c''d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z','A','B','C''D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
symbol=['!','@','#','$','%','&','*','(',')']

print("Welcome to the PyPassword Generator!")
nr_letters=int(input("How many letters would you like in your password?\n"))
nr_symbols=int(input(f"How many symbols would you like?\n"))
nr_numbers=int(input(f"How many numbers would you like?\n"))
password_list=[]
for num_let in range(0,nr_letters) :
   password_list+=random.choice(letters)
for num_sym in range(0,nr_symbols):
    password_list+=random.choice(symbol)
for num_num in range(1,nr_numbers+1):
    password_list+=str(random.randint(0,10))
random.shuffle(password_list)
password=""
for char in password_list:
    password+=char
print(f"Your password is: {password}")