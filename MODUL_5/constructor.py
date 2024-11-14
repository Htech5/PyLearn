import re


class UserService:
    def __init__(self):
        self.users = {}

    def is_strong_password(self, password):
        if (
            len(password) >= 8
            and re.search("[a-z]", password)
            and re.search("[A-Z]", password)
            and re.search("[0-9]", password)
            and re.search("[@#$%*^&+=!]", password)
        ):
            return True
        return False

    def register(self, username, password):
        if username in self.users:
            print("Username already exists. Please try another one.")
        elif not self.is_strong_password(password):
            print(
                "Password is not strong enough. It must be at least 8 characters long, "
                "contain at least one uppercase letter, one lowercase letter, one number, "
                "and one special character (@#$%^&+=!)."
            )
        else:
            self.users[username] = password
            print("Registration successful.")

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            print(f"Welcome {username}, you are now logged in.")
        else:
            print("Invalid username or password.")
