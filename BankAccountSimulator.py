# Gabriel Viera and Jose Raul Rivera Rodriguez
# CIIC 3015 Lab Project 1

# Allows us to save the date and time of transactions for reports.
from datetime import datetime


# Different colored text to grab the user's attention.
class bcolors:
    green = '\033[92m'  # Ok
    yellow = '\033[93m'  # Warning
    red = '\033[91m'  # Penalty
    black = '\033[0m'  # Normal
    cyan = '\033[96m'  # Reports


# Has the user enter their preferred account name.
account_name = input('Enter an account name: ').strip()

# All necessary variables that stores values which will be printed
# during reports and when the user exits.
balance = -1
total_withdraw = 0
failed_withdraw = 0
total_deposit = 0
total_penalty = 0
count_withdraw = 0
count_penalty = 0
count_deposit = 0

# Lists that will store information for each transaction.
record_withdraw = []
record_deposit = []

# This neat code block ensures that the user will not enter strings or negative numbers when asked their starting balance.
while balance < 0:
    try:
        balance = float(input('\nEnter your starting balance: '))
        if balance < 0: 
            print(f'{bcolors.yellow}\nInvalid starting balance. Try again.{bcolors.black}')
    except ValueError:
        print(f'{bcolors.yellow}\nInvalid starting balance. Try again.{bcolors.black}')



# Occurs when the user wants to exit. Will print final balance, general information of transactions, etc.
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


# Used to print the user's name and current balance after each transaction.
# It also prints dashes (-) on the top and bottom to separate it from other information.
# The if statement in this function allows us to print the right number of dashes.
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


# Runs when the user wants to withdraw.
# If the user attempts to enter a string or negative number it will ask for a second input.
# If the user tries to withdraw more than what is currently available, it will warn the user and take $5.
def choice_w():
    global total_withdraw, failed_withdraw, total_penalty, balance, count_withdraw, count_penalty
    try:
        w_amount = float(input('\nHow much would you like to withdraw? '))
        if w_amount >= 0:
            if balance >= w_amount:
                balance -= w_amount
                total_withdraw += w_amount
                count_withdraw += 1
                record_withdraw.append([f'-${w_amount:,.2f}', datetime.now().isoformat(sep=' ', timespec='minutes')])
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


# Very similar to the choice_w() function
# Runs when the user wants to deposit.
# It will not allow strings or negatives, and will run again if they are entered.
def choice_d():
    global total_deposit, balance, count_deposit
    try:
        d_amount = float(input('\nHow much would you like to deposit? '))
        if d_amount >= 0:
            balance += d_amount
            total_deposit += d_amount
            count_deposit += 1
            record_deposit.append([f'${d_amount:,.2f}', datetime.now().isoformat(sep=' ', timespec='minutes')])
        else:
            print(f'{bcolors.yellow}\nPlease enter a valid input.{bcolors.black}')
            choice_d()
    except ValueError:
        print(f'{bcolors.yellow}\nPlease enter a valid input.{bcolors.black}')
        choice_d()


# Runs when the user wants to see their records.
# It will print the amount and date/time of each individual transaction.
# Will loop until the user decides to exit the record menu.
def choice_r():
    global record_deposit, total_deposit, total_withdraw
    print(f'\n------------------\n'
            f'RECORD OF DEPOSITS\n'
            f'------------------\n')
    record_choice = input(f'Which record would you like to see?\n\n'
                            f"1) Withdrawal Record\n"
                            f"2) Deposit Record\n"
                            f"3) Go Back\n\n"
                            f'Please enter your selection: ').strip().lower()
    if record_choice in ('1', 'withdrawal record', 'withdrawal', 'w'):
        if len(record_withdraw) == 0:
            print(f"{bcolors.red}\n-No withdraws record available-{bcolors.black}")
        else:
            for x in record_withdraw:
                print(f"\n{bcolors.cyan}{x[0]}  |  {x[1]}{bcolors.black}")
            print(f"{bcolors.cyan}\nTOTAL: -${total_withdraw:,.2f}{bcolors.black}")
            input("\nPress any key to continue. ")
    elif record_choice in ('2', 'deposit record', 'deposit', 'd'):
        if len(record_deposit) == 0:
            print(f"{bcolors.red}\n-No deposit's record available-{bcolors.black}")
        else:
            for x in record_deposit:
                print(f"\n{bcolors.cyan}{x[0]}  |  {x[1]}{bcolors.black}")
            print(f"{bcolors.cyan}\nTOTAL: ${total_deposit:,.2f}{bcolors.black}")
            input("\nPress any key to continue.")
    elif record_choice in ('3', 'Go Back'):
        return
    else:
        print(f'{bcolors.yellow}\nPlease enter a valid input.{bcolors.black}')
    choice_r()


# Function that allows the user to pick between withdraws, deposits, records, or exiting.
def choice():
    user_choice = input(f'\nWhat would you like to do?\n\n'
                        f'1) Withdraw\n'
                        f'2) Deposit\n'
                        f'3) Record\n'
                        f'4) Quit\n\n'
                        f'Please enter your selection: ').strip().lower()
    if user_choice in ('1', 'w', 'withdraw'):
        choice_w()

    elif user_choice in ('2', 'd', 'deposit'):
        choice_d()

    elif user_choice in ('3', 'r', 'record'):
        choice_r()

    elif user_choice in ('4', 'q', 'quit'):
        return stop()
    else:
        print(f'{bcolors.yellow}\nPlease enter a valid input.{bcolors.black}')
    info()
    choice()


info()
choice()