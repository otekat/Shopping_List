import random

class Application:

    def __init__(self, users):
        self.users = users

    def create_user (self, user):
        if user.email not in self.users.keys():
            self.users[user.email]=user
            return True
        return False

    def login (self, email, password):
        if email in self.users[email].password == password:
            return True
         return False

    def user_account(self,email):
        if email in self.users:
            return self.users[email]
        return False



