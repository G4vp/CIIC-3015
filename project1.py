account_name = input('Enter an account name: ')
balance = int(input('Enter your starting balance: '))


def withdraw(n):
    global balance
    balance -= n


def deposit(n):
    global balance
    balance += n


def stop():
    print('Thanks for using Rivera and Viera\'s Bank Account Simulator. Come again!')


def info():
    print('Name: ' + str(account_name))
    print("Balance: ${:.2f}".format(balance))


def choice():
    user_choice = input('What would you like to do? (W)ithdraw, (D)eposit, (Q)uit ').lower().strip()
    if user_choice == 'w':
        w_amount = float(input('How much would you like to withdraw? '))
        withdraw(w_amount)
        info()
        choice()
    elif user_choice == 'd':
        d_amount = float(input('How much would you like to deposit? '))
        deposit(d_amount)
        info()
        choice()
    elif user_choice == 'q':
        stop()
    else:
        print('Please enter a valid input')
        choice()


info()
choice()