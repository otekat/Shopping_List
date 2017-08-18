import random

class ShoppingList:
    def __init__(self):
        self.users = {}
        self.users_ShoppingList = []

    def user_register(self, user):
        if user.email in self.users.keys():
            return False
        else:
            self.users.update({user.email: user})
            self.users_ShoppingList.append(self.users)
            return True

    def get_user(self, email):
        if email in self.users.keys():
            return self.users[email]
        return None

    def user_login(self, email, password):
        if email in self.users.keys():
            if self.users[email].password == password:
                return True
