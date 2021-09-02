account_name = input('Please enter the name of your account: ').title()
balance = float(input('\nPlease enter the starting balance: '))



def withdraw(n):
    global balance
    balance -= n


def deposit(n):
    global balance
    balance += n

def penalty():
    global balance
    balance -= 5
    print(f'\n-- Insufficient funds. For your convenience, an overdraft fee of $5 is being deducted from your balance. Have a nice day. --\n')

def stop():
    print('Thanks for using Rivera and Viera\'s Bank Account Simulator. Come again!')


def info():
    print(f"\nAccount: {account_name}")
    print(f"Balance: ${balance:,.2f}")


def choice():
    user_choice = input(f'You may:\n'
                        f'1) Deposit some funds\n'
                        f'2) Withdraw some funds\n'
                        f'3) Quit\n'
                        f'Please enter your selection: ').lower().strip()
    if user_choice == '1':
        d_amount = float(input('How much would you like to deposit? '))
        deposit(d_amount)

    elif user_choice == '2':
        w_amount = float(input('How much would you like to withdraw? '))
        if(w_amount > balance):
            penalty()
        else:
            withdraw(w_amount)

    elif user_choice == '3':
        stop()
    else:
        print(f'---- {user_choice} is not a valid input. Please enter a valid input ----')
        choice()
    info()
    choice()

info()
choice()