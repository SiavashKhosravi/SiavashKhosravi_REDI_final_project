""" Main Project file """

from customer_sia import Customer, list_customer_object
from account_sia import Account
from util_sia import check_user_name, user_name_check_list


accounts = {}

sia = Customer(name='sia', user_name='sia-1', password=134324234, address='sdfasf3532423', phone_number=12345354)
print(sia)
print(user_name_check_list)
sia2 = Customer(name='sia2', user_name='sia-2', password=1343245, address='sdfasf353248', phone_number=12345354)
print(user_name_check_list)
print(list_customer_object)
print(list_customer_object["sia-1"].password)

#
# cus1 = Customer(name="sia", address="asfsfas2323423", phone_number=23234234234)
# print(cus1)
# cus1_acc = Account(customer=cus1, use_name="sia-1", init_balance=100)
# cus2_acc = Account(customer=cus1, use_name="sia-2", init_balance=500)
# cus1_acc.create_account()
# print(cus1.customer_name())
#
#
# def add_account(customer, account):
#     if customer.customer_name() not in accounts.keys():
#         accounts[customer.customer_name()] = []
#         accounts[customer.customer_name()].append(account)
#     else:
#         accounts[customer.customer_name()].append(account)
#
#
# add_account(customer=cus1, account=cus1_acc)
# add_account(customer=cus1, account=cus2_acc)
# cus3_acc = Account(customer=cus1, use_name="sia-2", init_balance=1000)
# add_account(customer=cus1, account=cus3_acc)
#
# arash = Customer(name="arash", address="fdsfdfsdf23121", phone_number=53423423)
# arash_acc = Account(customer=arash, use_name="arash-1", init_balance=35324)
# arash2_acc = Account(customer=arash, use_name="arash-2", init_balance=6222)
# add_account(customer=arash, account=arash_acc)
# add_account(customer=arash, account=arash2_acc)
#
# print(accounts)
# print(accounts['sia'][0].__dict__['acc_num'])
