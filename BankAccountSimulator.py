# Gabriel A. Viera Perez and Jose Raul Rivera Rodriguez
# CIIC 3015 Lab Project 1


# We added some extra features like the account system, record system, and a sent and receive money system.
# Also we have colors, so please do not use in the Windows terminal, as it will not change the colors.


# Allows us to save the date and time of transactions for reports.
from datetime import datetime


# Different colored text to grab the user's attention.
class colors:
    green = '\033[92m'  # Ok
    yellow = '\033[93m'  # Warning
    red = '\033[91m'  # Penalty
    black = '\033[0m'  # Normal
    blue = '\033[94m'  # Withdraw Reports
    cyan = '\033[96m'  # Deposit Reports
    magenta = '\033[95m'  # Transactions


# All necessary variables that stores values
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
record_penalty = {}
general_record = {}
transfer_general = {}
transfer_receive = {}
transfer_send = {}
send_total = {}
receive_total = {}
riviera = '''██████╗░██╗██╗░░░██╗██╗███████╗██████╗░░█████╗░
██╔══██╗██║██║░░░██║██║██╔════╝██╔══██╗██╔══██╗
██████╔╝██║╚██╗░██╔╝██║█████╗░░██████╔╝███████║
██╔══██╗██║░╚████╔╝░██║██╔══╝░░██╔══██╗██╔══██║
██║░░██║██║░░╚██╔╝░░██║███████╗██║░░██║██║░░██║
╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝'''


# Sign up function used to ask for a log in or a create account.

def sign():
    global account_names, account_balances, current_account

    sign_log = input(
        f'{colors.green}\n{riviera}\n\nWelcome to Rivera and Viera\'s Bank Account Simulator!{colors.black}'
        f'\n\nWhat would you like to do? \n\n'
        f'1) Create an account\n'
        f'2) Log into an account\n\n'
        f'Please enter your selection: ').strip().lower()
    if sign_log in ('1', 'create', 'c', 'create an account'):
        while True:
            current_account = input(f'\nEnter an account name: ').strip()
            if current_account == '':
                print(f'{colors.yellow}\nPlease enter a valid input.{colors.black}')
            elif current_account in account_names:
                print(f'{colors.yellow}\nUnfortunately, that username is already taken.{colors.black}')
            else:
                account_names.update({current_account: current_account})
                ask_balance()
                break

    elif sign_log in ('2', 'log', 'l', 'log in', 'login', 'log into an account'):
        log = input(f'\nEnter your account name: ').strip()
        while log not in account_names:
            if log == '':
                print(f'{colors.yellow}\nPlease enter a valid input.{colors.black}')
            log_temp = input((f'{colors.red}\n-Account Does Not Exist.{colors.black}'
                                f'\nWould you likes to try another name? Yes/No: ')).strip().lower()
            if log_temp in ('1', 'yes', 'y'):
                log = input(f'\nEnter your account name: ').strip()
            elif log_temp in ('2', 'no', 'n'):
                sign()
                log = current_account

            else:
                print(f'{colors.yellow}\nPlease enter a valid input.{colors.black}')
        current_account = log

    else:
        print(f'{colors.yellow}\nPlease enter a valid input.{colors.black}')
        sign()


# Ask the user for their balance, if the input is not a valid will loop until you give him a correct input.
def ask_balance():
    while True:
        try:
            account_balances.update({current_account: float(input('\nEnter your starting balance: ').strip())})
            break
        except ValueError:
            print(f'\n{colors.yellow}Please enter a valid input.{colors.black}')


# Used to print the user's name and current balance after each transaction.
# It also prints dashes (-) on the top and bottom to separate it from other information.
# The if statement in this function allows us to print the right number of dashes.
def info():
    print_name = f'Name: {account_names[current_account]}\n'
    if account_balances[current_account] < 0:
        print_balance = f'Balance: -${abs(account_balances[current_account]):,.2f}\n'
    else:
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
        w_amount = float(int(float(input('\nEnter 0 if you would like to cancel this withdrawal. '
                                         '\nHow much would you like to withdraw? ').strip()) * 100) / 100)
        if w_amount > 0:
            if account_balances[current_account] >= w_amount:
                account_balances.update({current_account: account_balances.get(current_account, 0) - w_amount})
                total_withdraw.update({current_account: total_withdraw.get(current_account, 0) + w_amount})
                count_withdraw.update({current_account: count_withdraw.get(current_account, 0) + 1})
                temp = record_withdraw.setdefault(current_account, [])
                temp.append(([f'-${w_amount:,.2f}', datetime.now().isoformat(sep=" ", timespec="minutes")]))
                record_withdraw[current_account] = temp
                temp = general_record.setdefault(current_account, [])
                temp.append(([f'{colors.blue}-${w_amount:,.2f}',
                                f'{datetime.now().isoformat(sep=" ", timespec="minutes")}{colors.black}']))
                general_record[current_account] = temp
            else:
                print(f'{colors.red}\nUnsuccessful withdrawal. Insufficient funds. $5 have been deducted from your '
                        f'account.{colors.black}')
                account_balances.update({current_account: account_balances.get(current_account, 0) - 5})
                total_penalty.update({current_account: total_penalty.get(current_account, 0) + 5})
                failed_withdraw.update({current_account: failed_withdraw.get(current_account, 0) + w_amount})
                count_penalty.update({current_account: count_penalty.get(current_account, 0) + 1})
                temp = record_penalty.setdefault(current_account, [])
                temp.append(([f'-${5:,.2f}', datetime.now().isoformat(sep=" ", timespec="minutes")]))
                record_penalty[current_account] = temp
                temp = general_record.setdefault(current_account, [])
                temp.append(([f'{colors.red}-${5:,.2f}',
                                f'{datetime.now().isoformat(sep=" ", timespec="minutes")}{colors.black}']))
                general_record[current_account] = temp
        elif not w_amount:
            pass
        else:
            print(f'{colors.yellow}\nPlease enter a valid input.{colors.black}')
            choice_w()

    except ValueError:
        print(f'{colors.yellow}\nPlease enter a valid input.{colors.black}')
        choice_w()


# Very similar to the choice_w() function
# Runs when the user wants to deposit.
# It will not allow strings or negatives, and will run again if they are entered.
def choice_d():
    global total_deposit, count_deposit, record_deposit, account_balances
    try:
        d_amount = float(int(float(input('\nEnter 0 if you would like to cancel this deposit. '
                                         '\nHow much would you like to deposit? ').strip()) * 100) / 100)
        if d_amount > 0:
            account_balances.update({current_account: account_balances.get(current_account, 0) + d_amount})
            total_deposit.update({current_account: total_deposit.get(current_account, 0) + d_amount})
            count_deposit.update({current_account: count_deposit.get(current_account, 0) + 1})
            temp = record_deposit.setdefault(current_account, [])
            temp.append(([f'${d_amount:,.2f}', datetime.now().isoformat(sep=" ", timespec="minutes")]))
            record_deposit[current_account] = temp
            temp = general_record.setdefault(current_account, [])
            temp.append(([f'{colors.cyan}${d_amount:,.2f}',
                            f'{datetime.now().isoformat(sep=" ", timespec="minutes")}{colors.black}']))
            general_record[current_account] = temp
        elif not d_amount:
            pass
        else:
            print(f'{colors.yellow}\nPlease enter a valid input.{colors.black}')
            choice_d()

    except ValueError:
        print(f'{colors.yellow}\nPlease enter a valid input.{colors.black}')
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
                            f"1) General Record\n"
                            f"2) Withdrawal Record\n"
                            f"3) Deposit Record\n"
                            f"4) Penalty Record\n"
                            f"5) Transfer Record\n"
                            f"6) Go Back\n\n"
                            f'Please enter your selection: ').strip().lower()

    if record_choice in ('1', 'general record', 'general', 'g'):
        if len(general_record.setdefault(current_account, [])) == 0:
            print(f'{colors.red}\n-No records available-{colors.black}')
        else:
            for transaction in general_record[current_account]:
                print(f'\n{"  |  ".join(transaction)}')
            input("\nPress any key to continue. ")

    elif record_choice in ('2', 'withdrawal record', 'withdrawal', 'w'):
        if len(record_withdraw.setdefault(current_account, [])) == 0:
            print(f"{colors.red}\n-No withdrawal record available-{colors.black}")
        else:
            for x in record_withdraw[current_account]:
                print(f"\n{colors.blue}{x[0]}  |  {x[1]}{colors.black}")
            print(f"{colors.blue}\nTOTAL: -${total_withdraw[current_account]:,.2f}{colors.black}")
            input("\nPress any key to continue. ")

    elif record_choice in ('3', 'deposit record', 'deposit', 'd'):
        if len(record_deposit.setdefault(current_account, [])) == 0:
            print(f"{colors.red}\n-No deposit record available-{colors.black}")
        else:
            for x in record_deposit[current_account]:
                print(f"\n{colors.cyan}{x[0]}  |  {x[1]}{colors.black}")
            print(f"{colors.cyan}\nTOTAL: ${total_deposit[current_account]:,.2f}{colors.black}")
            input("\nPress any key to continue.")

    elif record_choice in ('4', 'penalties', 'penalty', 'p', 'penalty record'):
        if len(record_penalty.setdefault(current_account, [])) == 0:
            print(f'{colors.red}\n-No penalty record available-{colors.black}')
        else:
            for x in record_penalty[current_account]:
                print(f'\n{colors.red}{x[0]}  |  {x[1]}{colors.black}')
            print(f'{colors.red}\nTOTAL: -${total_penalty[current_account]:,.2f}{colors.black}')
            input("\nPress any key to continue.")

    elif record_choice in ('5', 'transfer', 'transfer record', 't'):
        choice_r_transfer()

    elif record_choice in ('6', 'go back', 'go', 'back'):
        return

    else:
        print(f'{colors.yellow}\nPlease enter a valid input.{colors.black}')

    choice_r()


# Choice between sent or receive transfers, or both to see the record of they.
def choice_r_transfer():
    choice_t = input(f'\nWhich transfer record would you like to see? \n\n'
                        f'1) All Transfers\n'
                        f'2) Received Transfers\n'
                        f'3) Sent Transfers\n'
                        f'4) Go Back\n\n'
                        f'Please enter your selection: ').strip().lower()

    if choice_t in ('1', 'all', 'all transfers', 'a'):
        if len(transfer_general.setdefault(current_account, [])) == 0:
            print(f'{colors.red}\n-No transfer records available-{colors.black}')
            choice_r_transfer()
        else:
            for x in transfer_general[current_account]:
                print(f'\n{x[0]}  |  {x[1]}  |  {x[2]}')
            input("\nPress any key to continue.")
            choice_r_transfer()

    elif choice_t in ('2', 'r', 'received', 'received transfers'):
        if len(transfer_receive.setdefault(current_account, [])) == 0:
            print(f'{colors.red}\n-No transfer records available-{colors.black}')
            choice_r_transfer()
        else:
            for x in transfer_receive[current_account]:
                print(f'{colors.green}\n{x[0]}  |  {x[1]}  |  {x[2]}{colors.black}')
            input("\nPress any key to continue.")
            choice_r_transfer()

    elif choice_t in ('3', 's', 'sent', 'sent transfers'):
        if len(transfer_send.setdefault(current_account, [])) == 0:
            print(f'{colors.red}\n-No transfer records available-{colors.black}')
            choice_r_transfer()
        else:
            for x in transfer_send[current_account]:
                print(f'{colors.magenta}\n{x[0]}  |  {x[1]}  |  {x[2]}{colors.black}')
            input("\nPress any key to continue.")
            choice_r_transfer()

    elif choice_t in ('4', 'go', 'back', 'go back'):
        return

    else:
        print(f'{colors.yellow}\nPlease enter a valid input.{colors.black}')
        choice_r_transfer()


# The money transfer system
def send_money():
    global account_balances, account_names, current_account, send_total, receive_total

    try:
        user_name = input(f'\nIf you would like to cancel this money transfer, do not enter a name.'
                            f'\nWhat account would you like to send money to? ').strip()
        if user_name == '':
            return
        elif user_name not in account_names:
            return print(
                f'\n{colors.red}Unfortunately, that account name is not registered in our database.{colors.black}')
        elif user_name == current_account:
            return print(f"\n{colors.yellow}You cannot send money to yourself.{colors.black}")
        money_for_send = float(int(float(input(f'\nEnter 0 if you would like to cancel this money transfer.'
                                                f'\nEnter the amount you wish to send to {user_name}: ').strip())
                                   * 100) / 100)
        if money_for_send == 0:
            return
        elif money_for_send < 0:
            return print(f"\n{colors.yellow}Hey! Are you trying to steal money from another account?!{colors.black}")
        elif money_for_send > account_balances[current_account]:
            return print(f"\n{colors.yellow}Sorry, you can't send money that you don't have.{colors.black}")
        account_balances.update({user_name: account_balances.get(user_name) + money_for_send})
        account_balances.update({current_account: account_balances.get(current_account) - money_for_send})
        if current_account not in send_total.keys():
            send_total.update({current_account: {'total': 0, 'count': 0}})
        send_total[current_account].update({'total': send_total[current_account].get('total', 0) + money_for_send,
                                            'count': send_total[current_account].get('count', 0) + 1})

        if user_name not in receive_total.keys():
            receive_total.update({user_name: {'total': 0, 'count': 0}})
        receive_total[user_name].update({'total': receive_total[user_name].get('total', 0) + money_for_send,
                                            'count': receive_total[user_name].get('count', 0) + 1})
        temp = general_record.setdefault(user_name, [])
        temp.append(([f'{colors.green}${money_for_send:,.2f}',
                        f'{datetime.now().isoformat(sep=" ", timespec="minutes")}',
                        f'From: {current_account}{colors.black}']))
        general_record[user_name] = temp
        temp = transfer_receive.setdefault(user_name, [])
        temp.append(([f'${money_for_send:,.2f}',
                        f'{datetime.now().isoformat(sep=" ", timespec="minutes")}',
                        f'From: {current_account}']))
        transfer_receive[user_name] = temp
        temp = transfer_general.setdefault(user_name, [])
        temp.append(([f'{colors.green}${money_for_send:,.2f}',
                        f'{datetime.now().isoformat(sep=" ", timespec="minutes")}',
                        f'From: {current_account}{colors.black}']))
        transfer_general[user_name] = temp
        temp = general_record.setdefault(current_account, [])
        temp.append(([f'{colors.magenta}-${money_for_send:,.2f}',
                        f'{datetime.now().isoformat(sep=" ", timespec="minutes")}',
                        f'To: {user_name}{colors.black}']))
        general_record[current_account] = temp
        temp = transfer_send.setdefault(current_account, [])
        temp.append(([f'${money_for_send:,.2f}',
                        f'{datetime.now().isoformat(sep=" ", timespec="minutes")}',
                        f'To: {user_name}']))
        transfer_send[current_account] = temp
        temp = transfer_general.setdefault(current_account, [])
        temp.append(([f'{colors.magenta}-${money_for_send:,.2f}',
                        f'{datetime.now().isoformat(sep=" ", timespec="minutes")}',
                        f'To: {user_name}{colors.black}']))
        transfer_general[current_account] = temp
        print(f"You have successfully sent {colors.green}${money_for_send:,.2f}{colors.black} to {user_name}.")

    except ValueError:
        print(f'{colors.yellow}\nPlease enter a valid input.{colors.black}')


# Occurs when the user wants to exit. Will print final balance, general information of transactions, etc.
def stop():
    print(f'{colors.green}\n{riviera}\n\n'
            f'{current_account}   |   {datetime.now().isoformat(sep=" ", timespec="minutes")}{colors.black}')
    print(f'\nFinal balance: ${account_balances[current_account]:,.2f}')
    print(f'You made {count_deposit.get(current_account, 0)} deposits, '
            f'totaling: ${total_deposit.get(current_account, 0):,.2f}')
    print(f'You made {count_withdraw.get(current_account, 0)} withdraws, '
            f'totaling: ${total_withdraw.get(current_account, 0):,.2f}')
    print(f'You made {count_penalty.get(current_account, 0)} unsuccessful withdraws. '
            f'Unsuccessfully withdrawn: ${failed_withdraw.get(current_account, 0):,.2f}')

    print(
        f'You sent money {send_total[current_account].get("count", 0)} times, finishing with a total value of '
        f'${send_total[current_account].get("total", 0):,.2f}') if current_account in send_total.keys() else print(
        f'You sent money 0 times.')

    print(
        f'You received money {receive_total[current_account].get("count", 0)} times, finishing with a total of '
        f'${receive_total[current_account].get("total", 0):,.2f}') if current_account in receive_total.keys() else \
        print(f'You received money 0 times.')

    print(f'You encountered {count_penalty.get(current_account, 0)} penalties, '
            f'resulting in: ${total_penalty.get(current_account, 0):,.2f}') if count_penalty.get(current_account,
                                                                                                0) == 0 else print(
        f'You encountered {count_penalty.get(current_account, 0)} penalties, '
        f'resulting in: -${total_penalty.get(current_account, 0):,.2f}')

    input(f'{colors.green}\nThanks for using Rivera and Viera\'s Bank Account Simulator. Come again!{colors.black}\n')


# Function that allows the user to pick between withdraws, deposits, records, send money or exiting.
def choice():
    global current_account

    user_choice = input(f'\nWhat would you like to do?\n\n'
                        f'1) Withdraw\n'
                        f'2) Deposit\n'
                        f'3) Record\n'
                        f'4) Send Money\n'
                        f'5) Log Out\n'
                        f'6) Quit\n\n'
                        f'Please enter your selection: ').strip().lower()

    if user_choice in ('1', 'w', 'withdraw'):
        choice_w()

    elif user_choice in ('2', 'd', 'deposit'):
        choice_d()

    elif user_choice in ('3', 'r', 'record'):
        choice_r()

    elif user_choice in ('4', 's', 'send money', 'send'):
        send_money()

    elif user_choice in ('5', 'l', 'o', 'log', 'out', 'logout', 'log out'):
        print(f'{colors.cyan}\nYou have been logged out of your account.')
        current_account = ''
        sign()

    elif user_choice in ('6', 'q', 'quit'):
        return stop()

    else:
        print(f'{colors.yellow}\nPlease enter a valid input.{colors.black}')

    info()
    choice()


sign()
info()
choice()

# <3
