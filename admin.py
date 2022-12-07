""" Customer Class and Functionalities """

admin_check_list = ['admin']
admins = {}

class Admin:
    def __init__(
            self, name: str, user_name: str, password):
        self.name = name
        self.user_name = user_name
        self.password = password

        admin_check_list.append(self.user_name)
        if self.user_name not in admins:
            admins[self.user_name] = []
            admins[self.user_name].append(self)
        else:
            admins[self.user_name].append(self)


