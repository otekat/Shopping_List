
class User():
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.ShoppingList = []

    def create_shoppinglist(self, title, description):
        if title is not self.ShoppingList.keys():
            self.ShoppingList[title] = description
            self.ShoppingList.list.append(self.ShoppingList)
            return True
        else:
            return False

    def delete_shoppinglist(self, title):
        if title in self.ShoppingList.keys():
            del self.ShoppingList[title]
        return self.ShoppingList

    def update_shoppinglist(self, title, description):
        if title in self.ShoppingList.keys():
            self.ShoppingList[title] = description
            return self.ShoppingList
