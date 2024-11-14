from constructor import UserService


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
