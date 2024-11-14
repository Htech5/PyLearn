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


def main():
    service = UserService()
    while True:
        print("\n=== Menu ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            service.register(username, password)

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            service.login(username, password)

        elif choice == "3":
            print("Thank you for using our system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
