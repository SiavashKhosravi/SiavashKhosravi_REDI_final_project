"""Final REDI project for bank account"""
from admin import Admin, admin_check_list, admins
from customer_sia import list_customer_object, Customer
from account_sia import Account, accounts
from util_sia import login_user_name_check

arash = Customer("arash", "arash1", "1234", "canada", "1234")

# function to print the entrance console
def entrance_console():
    print("welcome to the Gringotts Wizarding Bank")
    print("__Press 1 if you are a Customer__")
    print("__Press 2 if you are a Admin__")
    print("__Press 3 to Exit__")


# function to print menu when the user chooses to go to the customer menu
def customer_1_console():
    print("___welcome to the customer area___")
    print("press 1 to login into account ")
    print("press 2 to create new a customer ")  # profile customer
    print("press 3 to return to the previous menu ")
    print("press 4 to exit ")


def customer_2_console():
    print("___welcome to your profile")
    print("press 1 to make a new a account")
    print("press 2 to show me list of accounts ")
    print("press 3 to show balance ")
    print("press 4 to deposit ")
    print("press 5 to withdraw ")
    print("press 6 to previous menu ")
    print("press 7 to Exit ")


# function to print the menu when the user chooses to go to the admin area
def admin_1_console():
    print("___welcome to the admin area___")
    print("press 1 to login into your account ")
    print("press 2 Create admin ")
    print("press 3 to return to the previous menu ")
    print("press 4 to exit ")


# function to print the menu when the admin choose between his options
def admin_2_console():
    print("___welcome to the admin area___")
    print("press 1 to see customer information  ")
    print("press 2 to delete a customer ")
    print("press 3 to exit ")



""""""""""""""""""""""""""""""""""""""""""""
# below lines are for making
entrance_console()
option_1_user = input("Please chose your option: ")
if option_1_user.isnumeric():
    option_1_user = int(option_1_user)
# def console_menu_1(option_menu_1):
    while option_1_user != 3:

        if option_1_user == 1:
            # go to customer_1_console

            customer_1_console()
            # now ask the user for the new choice

            customer_2_option = input("Please enter your choice: ")
            if customer_2_option.isnumeric():
                customer_2_option = int(customer_2_option)

                while customer_2_option != 4:

                    if customer_2_option == 1:
                        # customer wants to login

                        entered_user_name = input("please enter your username: ")

                        if login_user_name_check(entered_user_name):  # check if the username is in the list
                            entered_password = input("please enter your password: ")

                            if entered_password == list_customer_object[entered_user_name].password:

                                print(f"welcome")
                                customer_2_console()  # console shows the option to the customer
                                customer_3_option = input("please enter your choice")
                                if customer_3_option.isnumeric():
                                    customer_3_option = int(customer_3_option)

                                    while customer_3_option != 7:

                                        if customer_3_option == 1:

                                            # customer wants to make a new account (customer already has a profile)
                                            enter_ini_balance = input("please enter your initial balance")
                                            if enter_ini_balance.isnumeric():
                                                enter_ini_balance = int(enter_ini_balance)
                                                account = Account(list_customer_object[entered_user_name], enter_ini_balance)
                                                print('Your new account been added to your profile')
                                            else:
                                                print("invalid initial balance")

                                        elif customer_3_option == 2:
                                            # show the list of bank accounts belonging to the logged-in customer

                                            for index, account in enumerate(accounts[entered_user_name]):
                                                print(f'{index + 1}:Account number: {accounts[entered_user_name][index].acc_num} '
                                                      f'\n')


                                        elif customer_3_option == 3:
                                            # ask from customer which bank account he needs to see the balance
                                            # if he has only one bank account then directly show the bank account
                                            print('Please choose which account number you want to check the balance.')
                                            account_num = input("please enter account number:")
                                            if account_num.isnumeric():
                                                account_num = int(account_num)
                                                for account in accounts[entered_user_name]:
                                                    if account.acc_num == account_num:
                                                        print(f'Your balance for account: {account.acc_num} is: '
                                                              f'{account.init_balance}')
                                                    else:
                                                        print('Account number is incorrect please enter the new one ')
                                            else:
                                                print("invalid input")

                                        elif customer_3_option == 4:
                                            # ask from customer; he needs to deposit the money from which bank account?
                                            # if he has only one bank account then  deposit the money to the account
                                            if len(accounts[entered_user_name]) == 1:
                                                Account.deposit(accounts[entered_user_name][0].acc_num)

                                            else:
                                                print('Please choose which account you want to deposit money')
                                                account_num = input("please enter account number:")
                                                if account_num.isnumeric():
                                                    account_num = int(account_num)
                                                    Account.deposit(account_num)
                                                else:
                                                    print("invalid input")
                                        elif customer_3_option == 5:
                                            # ask from customer; he needs to withdraw the money from which bank account?
                                            # if he has only one bank account then  withdraw the money fom the account

                                            if len(accounts[entered_user_name]) == 1:
                                                Account.withdraw(accounts[entered_user_name][0].acc_num)
                                            account_num = input("please enter account number:")
                                            if account_num.isnumeric():
                                                account_num = int(accout_num)
                                                Account.deposit(account_num)
                                            else:
                                                print("invalid input")

                                        elif customer_3_option == 6:
                                            # return to the previous menu
                                            break
                                        elif customer_3_option == 7:
                                            # return to the previous menu
                                            break
                                        else:
                                            print('Please choose you only between 1 to 7 options')

                                            customer_2_console()  # console shows the option to the customer=

                                        print("Thank you for choosing our wizarding bank")  # end of console
                                        break
                                    customer_2_console()  # console shows the option to the customer
                                else:
                                    print("invalid input")
                            else:
                                print("your password is not correct ")
                        else:
                            print("your username is not correct")
                    elif customer_2_option == 2:
                        # customer wants to make customer account ( he has never been our customer before)
                        # he has tp gp back to other menu to add e bank account to his new customer account
                        cus_name = input("Please enter your name: ")
                        if cus_name.isalpha():

                            cus_username = input("Please enter your user_name: ")
                            cus_password = input("Please enter your password: ")
                            cus_address = input("Please enter your address: ")
                            cus_phone = input("Please enter your phone number: ")
                            if cus_phone.isnumeric():
                                cus_phone = int(cus_phone)
                                customer = Customer(name=cus_name, user_name=cus_username, password=cus_password,
                                                    address=cus_address, phone_number=cus_phone)
                                print("Your customer account been created, please login into your account")
                                break
                            else:
                                print("phone number should contain only digits")
                        else:
                            print(" please enter only letters")
                    elif customer_2_option == 3:
                        # return to the previous menu
                        print("Thank you for choosing our wizarding bank")# end of console
                        break
                    customer_1_console()
                    break
            else:
                print("invalid option")
        elif option_1_user == 2:
            # admin_1_console
            admin_1_console()
            admin_1_choice = input("please enter your choice")
            if admin_1_choice.isnumeric():
                admin_1_choice = int(admin_1_choice)
                while admin_1_choice != 4:  # choices among admin_1_console
                    if admin_1_choice == 1:
                        # admin should be able to log in
                        adm_name = input("Please enter your name: ")
                        if adm_name.isalpha():
                            adm_username = input("Please enter your user_name: ")
                            adm_password = input("Please enter your password: ")
                            customer = Admin(name=adm_name, user_name=adm_username, password=adm_password)
                            print('Admin account created')
                        else:
                            print("name consists of only letters")

                    elif admin_1_choice == 2:
                        # login
                        entered_user_name = input("please enter your username: ")
                        if entered_user_name in admin_check_list:  # check if the username is in the list
                            entered_password = input("please enter your password: ")

                            if entered_password == admins[entered_user_name].password:
                                admin_2_console()
                                admin_2_option = int(input("please enter your choice"))

                                if admin_2_option == 1:
                                    pass
                                elif admin_2_option == 2:
                                    pass
                                elif admin_2_option == 3:
                                    pass

                    elif admin_1_choice == 3:
                        # return
                        pass

                print("Thank you for choosing our wizarding bank")  # end of console
            else:
                print("invalid input")

        else:
            print("invalid Option ")
            option_1_user = int(input("Please chose your option: "))
            break
    print("Thank you for choosing our wizarding bank")
else:
    print("invalid option")
entrance_console()
option_1_user = input("Please chose your option: ")


# console_menu_1(option_menu_1)
