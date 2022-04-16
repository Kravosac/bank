from definitions import Client, Account
from time import sleep
from typing import List

accounts: List[Account] = []


def menu():
    print('------------------------------')
    print('[1] - Open new account')
    print('[2] - Withdraw')
    print('[3] - Deposit')
    print('[4] - Transfer')
    print('[5] - Display list of accounts')
    print('[6] - Exit')

    option: str = input('Choose an option: ')

    if option == '1':
        open_account()
        menu()
    elif option == '2':
        make_withdraw()
        menu()
    elif option == '3':
        make_deposit()
        menu()
    elif option == '4':
        make_transfer()
        menu()
    elif option == '5':
        display_accounts()
        menu()
    elif option == '6':
        print('Thanks for using the bank services')
        sleep(2)
        exit(0)
    else:
        print('Please enter a valid option')
        sleep(2)
        menu()


def open_account():
    name: str = input('Enter the client name: ')
    ssn: str = input('Enter the client SSN: ')
    email: str = input('Enter the client e-mail: ')
    client = Client(name, ssn, email)
    account = Account(client)
    accounts.append(account)
    print(f'New account open successfully - account number {account.number}')
    sleep(1)
    menu()


def find_account(number: int) -> Account:
    ac = None
    for account in accounts:
        if account.number == number:
            ac = account
    return ac


def make_withdraw():
    account_number: int = int(input('Please enter your account number: '))
    account = find_account(account_number)
    if account:
        amount: float = float(input('Enter the withdraw amount: '))
        if amount <= account.balance:
            account.withdraw(amount)
            print(f'Withdraw of {amount:.2f} is done\nYour current balance is {account.balance:.2f}')
            sleep(1)
        else:
            print('Not enough funds, please check your balance.')
            sleep(1)
    else:
        print('Account not found')
        sleep(1)


def make_deposit():
    account_number: int = int(input('Please enter your account number: '))
    account = find_account(account_number)
    if account:
        amount: float = float(input('Enter the deposit amount: '))
        account.deposit(amount)
        print(f'Deposit of {amount:.2f} is done\nYour current balance is {account.balance:.2f}')
        sleep(1)
    else:
        print('Account not found')
        sleep(1)


def make_transfer():
    from_account: int = int(input('Please enter the source account number: '))
    source_account: Account = find_account(from_account)
    if source_account:
        amount: float = float(input('Please enter the amount: '))
        if amount <= source_account.balance:
            to_account: int = int(input('Please enter the destination account number: '))
            dest_account: Account = find_account(to_account)
            if dest_account:
                source_account.balance -= amount
                dest_account.balance += amount
                print('Transfer performed successfully')
                sleep(1)
            else:
                print('Account not found')
                sleep(1)
        else:
            print('Not enough funds, please check your balance')
            sleep(1)
    else:
        print('Account not found')
        sleep(1)


def display_accounts():
    if len(accounts) == 0:
        print('No accounts to display')
    else:
        for account in accounts:
            print('-------------')
            print(account)
            sleep(1)


if __name__ == '__main__':
    menu()
