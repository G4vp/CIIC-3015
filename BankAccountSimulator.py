class bcolors:
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    black = '\033[0m'


account_name = input('Enter an account name: ').strip()
balance = 0

while not balance:
    try:
        balance = float(input('\nEnter your starting balance: '))
    except ValueError:
        print(f'{bcolors.yellow}\nInvalid starting balance. Try again.{bcolors.black}')

total_withdraw = 0
failed_withdraw = 0
total_deposit = 0
total_penalty = 0
count_withdraw = 0
count_penalty = 0
count_deposit = 0


def stop():
    print(f'\nFinal balance: ${balance:,.2f}')
    print(f'You made {count_deposit} deposits, totaling: ${total_deposit:,.2f}')
    print(f'You made {count_withdraw} withdraws, totaling: ${total_withdraw:,.2f}')
    print(f'You made {count_penalty} unsuccessful withdraws. Unsuccessfully withdrawn :${failed_withdraw:,.2f}')
    if count_penalty == 0:
        print(f'You encountered {count_penalty} penalties, resulting in: ${total_penalty:,.2f}')
    else:
        print(f'You encountered {count_penalty} penalties, resulting in: -${total_penalty:,.2f}')
    print(f'{bcolors.green}\nThanks for using Rivera and Viera\'s Bank Account Simulator. Come again!{bcolors.black}')


def info():
    print_name = f'Name: {account_name}\n'
    print_balance = f'Balance: ${balance:,.2f}\n'

    if len(print_balance) > len(print_name):
        x = len(print_balance)
    else:
        x = len(print_name)

    print(f'\n{"-" * x}\n'
            f'{print_name}'
            f'{print_balance}'
            f'{"-" * x}')


def choice_w():
    global total_withdraw, failed_withdraw, total_penalty, balance, count_withdraw, count_penalty
    try:
        w_amount = float(input('\nHow much would you like to withdraw? '))
        if w_amount >= 0:  # Makes sure we cannot input negatives. Just a quality of life thing.
            if balance >= w_amount:
                balance -= w_amount
                total_withdraw += w_amount
                count_withdraw += 1
            else:
                print(f'{bcolors.red}\nUnsuccessful withdrawal. Insufficient funds. $5 have been deducted from your '
                    f'account.{bcolors.black}')
                balance -= 5
                total_penalty += 5
                failed_withdraw += w_amount
                count_penalty += 1
        else:
            print(f'{bcolors.yellow}\nPlease enter a valid input.{bcolors.black}')
            choice_w()
    except ValueError:
        print(f'{bcolors.yellow}\nPlease enter a valid input.{bcolors.black}')
        choice_w()


def choice_d():
    global total_deposit, balance, count_deposit
    try:
        d_amount = float(input('\nHow much would you like to deposit? '))
        if d_amount >= 0:  # Similar to the withdraw(), no negatives.
            balance += d_amount
            total_deposit += d_amount
            count_deposit += 1
        else:
            print(f'{bcolors.yellow}\nPlease enter a valid input.{bcolors.black}')
            choice_d()
    except ValueError:
        print(f'{bcolors.yellow}\nPlease enter a valid input.{bcolors.black}')
        choice_d()


def choice():
    user_choice = input(f'\nWhat would you like to do?\n\n'
                        f'1) Withdraw\n'
                        f'2) Deposit\n'
                        f'3) Quit\n\n'
                        f'Please enter your selection: ').strip().lower()
    if user_choice in ('1', 'w', 'withdraw'):
        choice_w()
        info()
        choice()
    elif user_choice in ('2', 'd', 'deposit'):
        choice_d()
        info()
        choice()
    elif user_choice in ('3', 'q', 'quit'):
        stop()
    else:
        print(f'{bcolors.yellow}\nPlease enter a valid input.{bcolors.black}')
        choice()


info()
choice()