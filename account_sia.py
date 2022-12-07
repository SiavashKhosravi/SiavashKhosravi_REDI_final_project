""" Account information """

from random import randint
from customer_sia import Customer
from util_sia import check_account, account_check_list

accounts = {}


class Account:
    """Accounts for all customers"""

    def __init__(self, customer: Customer, init_balance: int):
        self.customer = customer
        self.acc_num = randint(111111, 999999)
        self.init_balance = init_balance

        account_check_list.append(self.acc_num)
        if self.customer.user_name not in accounts.keys():
            accounts[self.customer.user_name] = []
            accounts[self.customer.user_name].append(self)
        else:
            accounts[self.customer.user_name].append(self)

    def __str__(self):
        output = f"{self.customer}'s account is {self.acc_num} with balance of{self.init_balance}. €"
        return output

    @staticmethod
    def withdraw(account_num):
        """Withdraw money from customer account"""
        try:
            withdraw = float(input("please enter how much Gallions you would like to withdraw?  "))
            if withdraw < 0:
                raise ValueError
            if type(withdraw) != int:
                raise ValueError
            if withdraw > account_num.init_balance:
                raise Exception
            account_num.init_balance -= withdraw
        except ValueError:
            print("Please enter a positive number")
        except Exception:
            print("You do not have enough Gallion")

    @staticmethod
    def deposit(account_num):
        """Deposits money to customer account"""
        try:
            deposit = float(input("please enter how much Gallions you would like to deposit?  "))
            if deposit < 0:
                raise ValueError
            if type(deposit) != int:
                raise ValueError
            account_num.init_balance += deposit
        except ValueError:
            print("Please enter a number")
