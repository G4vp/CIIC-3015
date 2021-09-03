account_name = input('Enter an account name: ').title().strip()
balance = 0

total_withdraw = 0
failed_withdraw = 0
total_deposit = 0
total_penalty = 0
count_withdraw = 0
count_penalty = 0
count_deposit = 0

# Loop until you give it a valid starting balance.
while not balance:
    try:
        balance = float(input('\nEnter your starting balance: '))
    except ValueError:
        print('Invalid starting balance. Try again.')


# Print the info if you Quit.
def stop():
    print(f'\nFinal balance: ${balance:,.2f}')
    print(f'You made {count_deposit} deposits, totaling: ${total_deposit:,.2f}')
    print(f'You made {count_withdraw} withdraws, totaling: ${total_withdraw:,.2f}')
    print(f'You made {count_penalty} unsuccessful withdraws. Unsuccessfully withdrawn3: ${failed_withdraw:,.2f}')
    print(f'You encountered {count_penalty} penalties, resulting in: ${0-total_penalty:,.2f}')
    print(f'\nThanks for using Rivera and Viera\'s Bank Account Simulator. Come again!')


# We print these quite a lot so I made a function for it.
def info():
    x = ''  
    if len(f'{balance:,.2f}')+10 > len(f'{account_name}')+6: 
        x = len(f'{balance:,.2f}')+10 
    else: 
        x = len(f'{account_name}')+6

    print(f'\n{"-"*x}\n'
            f'Name: {account_name}\n'
            f'Balance: ${balance:,.2f}\n'
            f'{"-"*x}')


def choice_w():
    global total_withdraw, failed_withdraw, total_penalty, balance, count_withdraw, count_penalty
    try:
        w_amount = float(input('How much would you like to withdraw? '))
        if w_amount >= 0:  # Makes sure we cannot input negatives. Just a quality of life thing.
            if balance >= w_amount:
                balance -= w_amount
                total_withdraw += w_amount
                count_withdraw += 1
            else:
                print('Unsuccessful withdrawal. Insufficient funds. $5 have been deducted from your account.')
                balance -= 5
                total_penalty += 5
                failed_withdraw += w_amount
                count_penalty += 1
        else:
            print('Please enter a valid input.')
            choice_w()
    except ValueError:
        print('Please enter a valid input.')
        choice_w()


def choice_d():
    global total_deposit, balance, count_deposit
    try:
        d_amount = float(input('How much would you like to deposit? '))
        if d_amount >= 0:  # Similar to the withdraw(), no negatives.
            balance += d_amount
            total_deposit += d_amount
            count_deposit += 1
        else:
            print('Please enter a valid input.')
            choice_d()
    except ValueError:
        print('Please enter a valid input.')
        choice_d()


def choice():
    user_choice = input(f'\nWhat would you like to do?\n\n'
                        f'1)Withdraw\n'
                        f'2)Deposit\n'
                        f'3)Quit\n\n'
                        f'Please enter your selection: ').strip()
    if user_choice == '1':
        choice_w()
    elif user_choice == '2':
        choice_d()
    elif user_choice == '3':
        return stop()
    else:
        print('Please enter a valid input')
    info()
    choice()

info()
choice()