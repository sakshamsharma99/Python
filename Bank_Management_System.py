def next(email):
    p=False
    while p != True:
        
        x = int(input("\n[1] Deposit\n[2] Withdraw\n[3] Check Balance\n[4] Home Page\n\n"))

        if x == 1:
            deposit(email)
        elif x == 2:
            withdraw(email)
        elif x == 3:
            check(email)
        elif x == 4:
            first()
        else:
            print("Wrong Input")

def deposit(email):
    Amount = int(input("Amount: "))
    balance_list[email] = Amount
    print("\n Successfully Deposited\n")

def withdraw(email):
    Amount = int(input("Amount: "))
    if Amount > balance_list[email]:
        print("Aukat Se jada nahi nikalte")
    balance_list[email] = balance_list[email]-Amount
    print("\nWidthdraw Successfully\n")

def check(email):
    print(f"Balance: {balance_list[email]}\n")


print("\n\n-------Welcome to Bank of India-------\n\n")

lists = {}

balance_list = {}
x = False

def first():
    while x is not True:
        login = int(input("Home:\n[1] Login\n[2] SignUp\n\n"))
        flag = 0
        if login == 1:
            email = input("Email: ").lower()
            for key in lists:
                if email == key:
                    password = int(input("Password: "))
                    if password == lists[key]:
                        print("\nSuccessfully Login\n")
                        next(email)
                    else:
                        print("\nWrong Password. Try Again\n")
                else:
                    flag += 1
                    if flag >= len(lists):
                        print("\nYou don't have an account\n")
        elif login == 2:
            new_email = input("Email: ")
            new_password = int(input("Password(0-9): "))
            lists.update({new_email: new_password})
            print("\nSignUp Successfully\n\n")

first()