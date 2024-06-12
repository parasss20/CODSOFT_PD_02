import tkinter as tk
from tkinter import ttk
import random
import string

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        # Creating GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Label and entry for password length
        self.length_label = ttk.Label(self.master, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.length_entry = ttk.Entry(self.master)
        self.length_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Button to generate password
        self.generate_button = ttk.Button(self.master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=1, columnspan=2, padx=5, pady=5)

        # Label to display generated password
        self.password_label = ttk.Label(self.master, text="")
        self.password_label.grid(row=2, columnspan=2, padx=5, pady=5)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError
            password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
            self.password_label.config(text=f"Generated Password: {password}")
        except ValueError:
            self.password_label.config(text="Invalid input for password length")
import tkinter as tk
from tkinter import ttk
import random
import string

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        # Creating GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Label and entry for password length
        self.length_label = ttk.Label(self.master, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.length_entry = ttk.Entry(self.master)
        self.length_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Checkbox for complexity options
        self.lowercase_var = tk.IntVar()
        self.lowercase_check = ttk.Checkbutton(self.master, text="Include Lowercase Letters", variable=self.lowercase_var)
        self.lowercase_check.grid(row=1, columnspan=2, padx=5, pady=5, sticky=tk.W)

        self.uppercase_var = tk.IntVar()
        self.uppercase_check = ttk.Checkbutton(self.master, text="Include Uppercase Letters", variable=self.uppercase_var)
        self.uppercase_check.grid(row=2, columnspan=2, padx=5, pady=5, sticky=tk.W)

        self.digits_var = tk.IntVar()
        self.digits_check = ttk.Checkbutton(self.master, text="Include Digits", variable=self.digits_var)
        self.digits_check.grid(row=3, columnspan=2, padx=5, pady=5, sticky=tk.W)

        self.special_var = tk.IntVar()
        self.special_check = ttk.Checkbutton(self.master, text="Include Special Characters", variable=self.special_var)
        self.special_check.grid(row=4, columnspan=2, padx=5, pady=5, sticky=tk.W)
        
        # Button to generate password
        self.generate_button = ttk.Button(self.master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=5, columnspan=2, padx=5, pady=5)

        # Label to display generated password
        self.password_label = ttk.Label(self.master, text="")
        self.password_label.grid(row=6, columnspan=2, padx=5, pady=5)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError
            
            # Define character sets based on complexity options
            charset = ""
            if self.lowercase_var.get():
                charset += string.ascii_lowercase
            if self.uppercase_var.get():
                charset += string.ascii_uppercase
            if self.digits_var.get():
                charset += string.digits
            if self.special_var.get():
                charset += string.punctuation
            
            # Check if at least one option is selected
            if not charset:
                raise ValueError("Select at least one option for password complexity")

            # Generate password
            password = ''.join(random.choices(charset, k=length))
            self.password_label.config(text=f"Generated Password: {password}")
        except ValueError as ve:
            self.password_label.config(text=str(ve))

def main():
    root = tk.Tk()
    password_generator = PasswordGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()


def main():
    root = tk.Tk()
    password_generator = PasswordGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
