""" Customer Class and Functionalities """

from util_sia import check_user_name, user_name_check_list

list_customer_object = {}

class Customer:
    def __init__(
            self, name: str, user_name: str, password, address: str, phone_number: int
    ):
        self.name = name
        self.user_name = user_name
        self.password = password
        self.address = address
        self.phone_num = phone_number

        user_name_check_list.append(user_name)
        list_customer_object[self.user_name] = self

    #def __str__(self):
    #    output = f"{self.name} has username {self.user_name} with password of{self.password}" \
    #             f" and address of {self.address} and phone number of {self.phone_num}. €"
    #    return output

    def customer_name(self):
        """Returns customer name"""
        return self.name


