class Client:

    def __init__(self: object, name: str, ssn: str, email: str) -> None:
        self.__name: str = name
        self.__ssn: str = ssn
        self.__email: str = email

    @property
    def name(self):
        return self.__name


class Account:

    counter: int = 1001

    def __init__(self: object, client: Client) -> None:
        self.__number: int = Account.counter
        self.__client: Client = client
        self.__balance: float = 0
        self.__limit: float = 100
        Account.counter += 1

    @property
    def number(self):
        return self.__number

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        self.__balance = new_balance

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, new_limit):
        self.__limit = new_limit

    @property
    def client(self):
        return self.__client

    def __str__(self):
        return f'Account number: {self.number}\nName: {self.client.name}\n' \
               f'Balance: {self.balance:.2f}\nLimit: {self.limit:.2f}'

    def withdraw(self, amount: float) -> None:
        self.balance -= amount

    def deposit(self, amount: float) -> None:
        self.balance += amount
