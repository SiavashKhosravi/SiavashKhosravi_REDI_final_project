""" Utility functions"""

user_name_check_list = []
account_check_list = []


def check_user_name(username: str) -> bool:
    """Checks if username exist"""

    if username in user_name_check_list:
        return False

    return True


def check_account(account: int) -> bool:
    """Checks if username exist"""

    if account in account_check_list:
        return False

    return True

def login_user_name_check(username) -> bool:
    """check if the entered_username is in the list or not"""
    if username in user_name_check_list:
        return True

    return False


def login_password_check(password) -> bool:
    """check if the entered_username is in the list or not"""
    if password in user_name_check_list:
        return True

    return False

#def dummy_data():
#    password = 123456
#    name = "siavash"
#    user_name = "sia"
#    phone_number = randint(111111, 999999)
#    address = f"{randint(1, 99)}, Munich, Germany"
#    for x in range(0, 6):
#        dummy_customer = Customer(
#            name=f"{name}-{x}",
#            user_name=f"{user_name}-{x}",
#            password=f"{user_name}-{x}",
#            address=address,
#            phone_number=phone_number,
#        )
#        Account(customer=dummy_customer, init_balance=int(f"{randint(
