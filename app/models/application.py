class Application:
    def __init__(self):
        """
        constructor method
        """
        self.users = {}

    def create_user(self, user):
        if user.email not in self.users.keys():
            self.users[user.email] = user
            return True
        return False

    def get_user(self, email):
        if email in self.users.keys():
            return self.users[email]
        return False

    def signup(self, user):
        if user.email in self.users.keys():
            return False
        else:
            self.users[user.email] = user
            return True

    def login(self, email, password):
        if email in self.users.keys():
            user = self.users[email]
            if user.password == password:
                return True
            return False
