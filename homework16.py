class bankaccount:
    bank_name = 'BOG'
    total_accounts = 0
    def __init__(self, owner, balance):
        self.owner_ = owner
        if bankaccount.validate_amount(balance):
            self.__balance = balance
        else:
            self.__balance = 0
        bankaccount.__total_accounts += 1
        self.__account_number = f"AN{bankaccount.__total_accounts:04d}"
    def deposit(self, amount):
        if bankaccount.validate_amount(amount):
            self.__balance += amount
            print('money added successfuly')
        else:
            print('invalid amount')
    def withdraw(self, amount):
        if not bankaccount.validate_amount(amount):
            print('invalid amount')
        elif amount > self.__balance:
            print('not enough balance')
        else:
            self.__balance -= amount
            print('money withdrawn successfuly')
    def checkbalance(self):
        return self.__balance
    def get_account_number(self):
        return self.__account_number
    def change_owner(self, new_owner):
        self._owner == new_owner
    @classmethod
    def get_total_accounts(cls):
        return cls.__total_accounts
    @staticmethod
    def validate_amount(amount):
        return amount > 0
    def __str__(self):
        return f"Account: {self.__account_number} | Owner: {self._owner}"
            