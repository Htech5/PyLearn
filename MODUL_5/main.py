# mengimpor class user_service  dari file auth_service.py

from auth_service import user_service


print("login bang dari kelompok 03!")


# Mengambil masukan username & password melalui console

username = input("username: ")

password = input("password: ")


# Membuat objek logininfo dengan blueprint atribut dan method dari class user_service

auth = user_service(username, password)

auth.login()
