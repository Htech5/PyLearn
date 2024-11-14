import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Ensure Pillow is installed


class LoginApp:
    def __init__(self, apk):
        self.apk = apk
        self.apk.title("Login Page")

        self.font_style = ("Helvetica", 14)
        self.bg_color = "lightblue"

        # Initially setup login page
        self.setup_login_page()

    def setup_login_page(self):
        # Clear any existing widgets
        for widget in self.apk.winfo_children():
            widget.destroy()

        # Login Page Labels and Entries
        self.apk.configure(bg=self.bg_color)
        label_title = tk.Label(
            self.apk,
            text="User Login",
            font=("Helvetica", 16, "bold"),
            bg=self.bg_color,
        )
        label_title.place(x=125, y=10)

        label_username = tk.Label(
            self.apk, text="Username", font=self.font_style, bg=self.bg_color
        )
        label_username.place(x=20, y=60)

        self.entry_username = tk.Entry(self.apk)
        self.entry_username.place(x=20, y=90)

        label_password = tk.Label(
            self.apk, text="Password", font=self.font_style, bg=self.bg_color
        )
        label_password.place(x=20, y=150)

        self.entry_password = tk.Entry(self.apk, show="*")
        self.entry_password.place(x=20, y=180)

        # Checkbox for "Remember Me" option
        self.remember_me = tk.IntVar()
        checkbox_remember = tk.Checkbutton(
            self.apk,
            text=" VERIFY ",
            font=("Helvetica", 10),
            bg=self.bg_color,
            variable=self.remember_me,
        )
        checkbox_remember.place(x=20, y=210)

        login_button = tk.Button(
            self.apk, text="Login", font=self.font_style, command=self.login
        )
        login_button.place(x=100, y=250)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Check if "Remember Me" is checked
        if self.remember_me.get() == 0:
            messagebox.showerror("Login Failed", "You must check 'verif box' to log in")
            return

        # Replace with your validation logic
        if username == "admin" and password == "1234":
            self.show_dashboard()
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password")

    def show_dashboard(self):
        # Clear any existing widgets
        for widget in self.apk.winfo_children():
            widget.destroy()

        self.apk.configure(bg="lightgreen")  # Change background color for dashboard

        # Display the image on the dashboard
        image = Image.open("images.jpg")
        image = image.resize((250, 400))
        self.photo = ImageTk.PhotoImage(image)
        label_image = tk.Label(self.apk, image=self.photo)
        label_image.place(x=445, y=0)
        label_image.lower()

        label_welcome = tk.Label(
            self.apk,
            text="Kami Kelompok 03",
            font=("Helvetica", 16, "bold"),
            bg="lightgreen",
        )
        label_welcome.pack(pady=20)

        logout_button = tk.Button(
            self.apk, text="Logout", font=self.font_style, command=self.setup_login_page
        )
        logout_button.pack(pady=10)


if __name__ == "__main__":
    apk = tk.Tk()
    app = LoginApp(apk)
    apk.geometry("700x400")
    apk.resizable(False, False)
    apk.mainloop()
