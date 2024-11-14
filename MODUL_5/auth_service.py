# File: auth_service.py
class user_service:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.data = {
            "nama1kelompok03": {
                "username": "nama1kelompok03",
                "password": "12345",
                "role": "mahasiswa",
            },
            "nama2kelompok03": {
                "username": "nama2kelompok03",
                "password": "12345",
                "role": "dosen",
            },
        }

    def check_password(self):
        for user_info in self.data.values():
            if (
                self.username == user_info["username"]
                and self.password == user_info["password"]
            ):
                return user_info
        return False

    def login(self):
        data = self.check_password()
        if data:
            print("\nWelcome", data["username"])
            print("Logged in as:", data["role"])
        else:
            print("\nInvalid Login!\n")
