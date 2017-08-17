class User():
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def create_shoppinglist(self, title, description):
        if title is not self.shopping.keys():
            self.shopping[title] = description
            self.shopping.list.append(self.shoppinglist)
            return True
        else:
            return False

    def delete_shoppinglist(self, title):
        if title in self.Myshoppinglist.keys():
            del self.Myshoppinglist[title]
        return self.Myshoppinglist

    def update_shoppinglist(self, title, description):
        if title in self.Myshopping.keys():
            self.Myshopping[title] = description
            return self.Myshopping
