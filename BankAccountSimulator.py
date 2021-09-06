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

# All necessary variables that stores values which will be printed

account_names = {}
account_balances = {}
current_account = ''
total_withdraw = {}
failed_withdraw = {}
total_deposit = {}
total_penalty = {}
count_withdraw = {}
count_penalty = {}
count_deposit = {}
record_withdraw = {}
record_deposit = {}


def sign():
    global account_names, account_balances, current_account

    sign_log = input(f'{bcolors.green}\nWelcome to Rivera and Viera\'s Bank Account Simulator!{bcolors.black}'
                        f'\n\nWhat would you like to do? \n\n'
                        f'1) Create an account\n'
                        f'2) Log into an account\n\n'
                        f'Please enter your selection: ').strip().lower()
    if sign_log in ('1', 'create', 'c', 'create an account'):
        while True:
            current_account = input(f'\nEnter an account name: ')
            if current_account == '':
                print(f'{bcolors.yellow}\nPlease enter a valid input.{bcolors.black}')
            elif current_account in account_names:
                print(f'{bcolors.yellow}\nUnfortunately, that username is already taken.{bcolors.black}')
            else:
                account_names.update({current_account: current_account})
                ask_balance()
                break

    elif sign_log in ('2', 'log', 'l', 'log in', 'login', 'log into an account'):
        log = input(f'\nEnter your account name: ').strip()
        while log not in account_names:
            log_temp = input(f'{bcolors.red}\n-Account Does Not Exist.\n{bcolors.black}'
                                f'\nWould you like to try another name?' 
                                f'\n1) Yes'
                                f'\n2) No'
                                f'\nPlease enter your selection: ').strip().lower()
            if log_temp in ('1', 'yes', 'y'):
                log = input(f'\nEnter your account name: ').strip()
            elif log_temp in ('2', 'no', 'n'):
                sign()
                log = current_account
            else:
                print(f'{bcolors.yellow}\nPlease enter a valid input.{bcolors.black}')
        current_account = log

    else:
        print(f'{bcolors.yellow}\nPlease enter a valid input.{bcolors.black}')
        sign()


def ask_balance():
    while True:
        try:
            account_balances.update({current_account: float(input('\nEnter your starting balance: '))})
            break
        except ValueError:
            print(f'\n{bcolors.yellow}Please enter a valid input.{bcolors.black}')

def send_Money():
    global account_balances, account_names, current_account
    
    try:
        user_name = input(f'\nEnter 0 if you would like to cancel.\n'
                            f'Write the account name for send your money: ').strip()
        if(user_name in ['0','cancel']):
            return
        elif(not(user_name in account_names)):
            return print(f'\n{bcolors.yellow}Unfortunately, that account name is not registered in our database.{bcolors.black}')
        elif(user_name == current_account):
            return print(f"\n{bcolors.yellow}Unfortunately, you can't send money to yourself.{bcolors.black}")
        money_for_send = int(input(f'\nEnter 0 if you would like to cancel.\n'
                                    f'Enter the amount of money for send to {user_name}: '))
        if(money_for_send == 0):
            return
        elif(money_for_send < 0):
            return print(f"\n{bcolors.yellow}Hey, are you trying to subtract money of another account? That is not possible.{bcolors.black}")
        elif(money_for_send > account_balances.get(current_account)):
            return print(f"\n{bcolors.yellow}Sorry, you can't send money that you don't have.{bcolors.black}")
        account_balances.update({user_name:account_balances.get(user_name)+money_for_send})
        account_balances.update({current_account:account_balances.get(current_account) - money_for_send})
        print("The money was sent successfully")
    except ValueError:
        print(f'{bcolors.yellow}\nPlease enter a valid input.{bcolors.black}')

# Occurs when the user wants to exit. Will print final balance, general information of transactions, etc.
def stop():
    print(f'\nFinal balance: ${account_balances[current_account]:,.2f}')
    print(f'You made {count_deposit.get(current_account, 0)} deposits, '
            f'totaling: ${total_deposit.get(current_account, 0):,.2f}')
    print(f'You made {count_withdraw.get(current_account, 0)} withdraws, '
            f'totaling: ${total_withdraw.get(current_account, 0):,.2f}')
    print(f'You made {count_penalty.get(current_account, 0)} unsuccessful withdraws. '
            f'Unsuccessfully withdrawn :${failed_withdraw.get(current_account, 0):,.2f}')

    if count_penalty.get(current_account, 0) == 0:
        print(f'You encountered {count_penalty.get(current_account, 0)} penalties, '
                f'resulting in: ${total_penalty.get(current_account, 0):,.2f}')

    else:
        print(f'You encountered {count_penalty.get(current_account, 0)} penalties, '
                f'resulting in: -${total_penalty.get(current_account, 0):,.2f}')

    print(f'{bcolors.green}\nThanks for using Rivera and Viera\'s Bank Account Simulator. Come again!{bcolors.black}')

# Used to print the user's name and current balance after each transaction.
# It also prints dashes (-) on the top and bottom to separate it from other information.
# The if statement in this function allows us to print the right number of dashes.
def info():
    print_name = f'Name: {account_names[current_account]}\n'
    print_balance = f'Balance: ${account_balances[current_account]:,.2f}\n'

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
    global total_withdraw, failed_withdraw, total_penalty, count_withdraw, count_penalty
    global account_balances, record_withdraw

    try:
        w_amount = float(input('\nEnter 0 if you would like to cancel this withdrawal. '
                                '\nHow much would you like to withdraw? '))
        if w_amount > 0:
            if account_balances[current_account] >= w_amount:
                account_balances.update({current_account: account_balances.get(current_account, 0) - w_amount})
                total_withdraw.update({current_account: total_withdraw.get(current_account, 0) + w_amount})
                count_withdraw.update({current_account: count_withdraw.get(current_account, 0) + 1})
                temp = record_withdraw.setdefault(current_account, [])
                temp.append(([f'-${w_amount:,.2f}', datetime.now().isoformat(sep=' ', timespec='minutes')]))
                record_withdraw[current_account] = temp
            else:
                print(f'{bcolors.red}\nUnsuccessful withdrawal. Insufficient funds. $5 have been deducted from your '
                        f'account.{bcolors.black}')
                account_balances.update({current_account: account_balances.get(current_account, 0) - 5})
                total_penalty.update({current_account: total_penalty.get(current_account, 0) + 5})
                failed_withdraw.update({current_account: failed_withdraw.get(current_account, 0) + w_amount})
                count_penalty.update({current_account: count_penalty.get(current_account, 0) + 1})
        elif not w_amount:
            pass
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
    global total_deposit, count_deposit, record_deposit, account_balances
    try:
        d_amount = float(input('\nEnter 0 if you would like to cancel this deposit. '
                                '\nHow much would you like to deposit? '))
        if d_amount > 0:
            account_balances.update({current_account: account_balances.get(current_account, 0) + d_amount})
            total_deposit.update({current_account: total_deposit.get(current_account, 0) + d_amount})
            count_deposit.update({current_account: count_deposit.get(current_account, 0) + 1})
            temp = record_deposit.setdefault(current_account, [])
            temp.append(([f'${d_amount:,.2f}', datetime.now().isoformat(sep=' ', timespec='minutes')]))
            record_deposit[current_account] = temp
        elif not d_amount:
            pass
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
    global record_deposit, total_deposit, total_withdraw, record_withdraw
    print(f'\n------------------\n'
            f'RECORD OF DEPOSITS\n'
            f'------------------\n')

    record_choice = input(f'Which record would you like to see?\n\n'
                            f"1) Withdrawal Record\n"
                            f"2) Deposit Record\n"
                            f"3) Go Back\n\n"
                            f'Please enter your selection: ').strip().lower()
    if record_choice in ('1', 'withdrawal record', 'withdrawal', 'w'):

        if len(record_withdraw.setdefault(current_account, [])) == 0:
            print(f"{bcolors.red}\n-No withdrawal record available-{bcolors.black}")
        else:
            for x in record_withdraw[current_account]:
                print(f"\n{bcolors.cyan}{x[0]}  |  {x[1]}{bcolors.black}")
            print(f"{bcolors.cyan}\nTOTAL: -${total_withdraw[current_account]:,.2f}{bcolors.black}")
            input("\nPress any key to continue. ")

    elif record_choice in ('2', 'deposit record', 'deposit', 'd'):
        if len(record_deposit.setdefault(current_account, [])) == 0:
            print(f"{bcolors.red}\n-No deposit record available-{bcolors.black}")
        else:
            for x in record_deposit[current_account]:
                print(f"\n{bcolors.cyan}{x[0]}  |  {x[1]}{bcolors.black}")
            print(f"{bcolors.cyan}\nTOTAL: ${total_deposit[current_account]:,.2f}{bcolors.black}")
            input("\nPress any key to continue.")

    elif record_choice in ('3', 'go back', 'go', 'back'):
        return

    else:
        print(f'{bcolors.yellow}\nPlease enter a valid input.{bcolors.black}')

    choice_r()

# Function that allows the user to pick between withdraws, deposits, records, send money or exiting.
def choice():
    global current_account

    user_choice = input(f'\nWhat would you like to do?\n\n'
                        f'1) Withdraw\n'
                        f'2) Deposit\n'
                        f'3) Record\n'
                        f'4) Send money\n'
                        f'5) Log Out\n'
                        f'6) Quit\n\n'
                        f'Please enter your selection: ').strip().lower()

    if user_choice in ('1', 'w', 'withdraw'):
        choice_w()

    elif user_choice in ('2', 'd', 'deposit'):
        choice_d()

    elif user_choice in ('3', 'r', 'record'):
        choice_r()

    elif user_choice in ('4','s','Send money'):
        send_Money()

    elif user_choice in ('5', 'l', 'o', 'log', 'out', 'logout', 'log out'):
        print(f'{bcolors.cyan}\nYou have been logged out of your account.')
        current_account = ''
        sign()
    elif user_choice in ('6', 'q', 'quit'):
        return stop()

    else:
        print(f'{bcolors.yellow}\nPlease enter a valid input.{bcolors.black}')

    info()
    choice()


sign()
info()
choice()
