print(
    '''
 _____________________
|  _________________  |
| | CS           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

'''
)
continue_loop = True
while continue_loop != False:    
    n1 = float(input("What's the first number?: "))
    print('''
    +
    -
    *
    /
    ''')

    def inner(n1):
                   
        operator = input("Pick an operation: ")

        n2 = float(input("What's the next number?: "))
        solution = 0
        if operator == '-':
            solution = n1 - n2
        elif operator == '+':
            solution = n1 + n2
        elif operator == '*':
            solution = n1 * n2
        elif operator == '/':
            solution = n1 / n2
        else:
            print("Wrong input")

        print(f"{n1} {operator} {n2} = {solution}")

        game_over = input(f"Type 'y' to continue calculating with {solution}, or type 'n' to stat a new calculation: ")

        if game_over == 'n':
            solution = 0
        elif game_over == 'y':
            n1 = solution
            inner(n1)
    inner(n1)
