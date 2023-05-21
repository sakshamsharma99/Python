import random

print("\nWelcome to the Password Generator!\n")
letters = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z".split(",")
num = "0,1,2,3,4,5,6,7,8,9".split(",")
special_symbols = "!,@,#,$,%,&,*,(,)".split(",")
user_input = int(input("How many letters would you like in your password?\n"))
symbols = int(input("How many symbols would you like?\n"))
number = int(input("How many numbers would you like?\n"))
password = []
for n in range(0,user_input):
    password.append(random.choice(letters))

for n in range(0,symbols):
    password += random.choice(special_symbols)

for n in range(0,number):
    password += random.choice(num)

random.shuffle(password)

answer = ""
for n in password:
    answer += n

print(f"Password: {answer}")