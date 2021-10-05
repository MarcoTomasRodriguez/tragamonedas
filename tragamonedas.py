import webbrowser
from random import randint

import tkinter as tk
import tkinter.messagebox


class Application(tk.Frame):
    # Tkinter Widgets
    master: tk.Tk
    balance_label: tk.Label
    balance_var: tk.DoubleVar
    bet_var: tk.DoubleVar
    numbers_label: tk.Label

    # Application state
    balance: float
    bet: float

    def __init__(self, master=None):
        super().__init__(master)
        self.balance = 0
        self.master = master
        self.configure()
        self.create_widgets()
        self.pack()

    # Configure tkinter master.
    def configure(self):
        self.master.title("Tragamonedas")

        menu_bar = tk.Menu(self.master)
        help_menu = tk.Menu(self.master, tearoff=0)
        help_menu.add_command(label="Manual de Usuario",
                              command=self.redirect_to_help)
        help_menu.add_command(label="Acerca de", command=self.show_about)
        menu_bar.add_cascade(label="Ayuda", menu=help_menu)
        self.master.config(menu=menu_bar)

    # Create tkinter widgets.
    def create_widgets(self):
        # Initialize title label.
        title_label = tk.Label(text="Maquina Tragamonedas", font=("Arial", 16))
        title_label.pack(padx=10, pady=10)

        # Initialize balance label.
        self.balance_label = tk.Label(text="Dinero: $0", font=("Arial", 12))
        self.balance_label.pack(padx=10, pady=10)

        # Initialize balance input.
        self.balance_var = tk.DoubleVar()
        self.balance_input = tk.Entry(textvariable=self.balance_var)
        self.balance_input.pack()

        # Initialize balance button.
        deposit_button = tk.Button(text="Depositar", command=self.deposit)
        deposit_button.pack()

        # Initialize bet label.
        bet_label = tk.Label(text="Ingrese su apuesta")
        bet_label.pack()

        # Initialize bet input.
        self.bet_var = tk.DoubleVar()
        bet_input = tk.Entry(textvariable=self.bet_var)
        bet_input.pack()

        # Initialize numbers.
        self.numbers_label = tk.Label(text="0   0   0", font=("Arial", 12))
        self.numbers_label.pack(padx=5, pady=5)

        # Initialize shoot button & bind "Click" event to shoot.
        shoot_button = tk.Button(text="Tirar", command=self.shoot)
        shoot_button.pack()

        # Initialize message label.
        self.message = tk.Label(text="¡Haga su primer tiro!", bg="lightblue")
        self.message.pack(padx=5, pady=5)

    # Update balance & balance label.
    def update_balance(self, new_balance: float) -> None:
        assert new_balance >= 0
        self.balance = new_balance
        self.balance_label.config(text=f"Dinero: ${self.balance}")

    # Show a message. This can either be with a message label (if success or info) or a message box (if error).
    def show_message(self, text: str, type: str) -> None:
        if type in ["success", "info"]:
            color_dict = {"success": "lightgreen", "info": "lightblue"}
            self.message.config(text=text, bg=color_dict[type])
        elif type == "error":
            tk.messagebox.showerror("Error", text)

    # Redirect to help website.
    # Caller: help_menu on "Manual de Usuario" click.
    def redirect_to_help(self) -> None:
        webbrowser.open("https://github.com/MarcoTomasRodriguez/tragamonedas")

    # Show about.
    # Caller: help_menu on "Acerca de" click.
    def show_about(self) -> None:
        tk.messagebox.showinfo(
            "Acerca de", "Trabajo realizado por Alejo Scarlato y Marco Rodriguez")

    # Deposit a balance.
    # Caller: deposit_button on click.
    def deposit(self) -> None:
        # Get deposited balance.
        deposited_balance = self.balance_var.get()

        # Check if deposited balance is lower than 0. If so, show an error message.
        if deposited_balance < 0:
            self.show_message(
                "No puede depositar un valor inferior a 0.", "error")
            return

        # Update balance & set deposited balance to 0.
        self.update_balance(self.balance + deposited_balance)
        self.balance_var.set(0)

    # Generate 3 random numbers, check if all of them are equal and log them in a csv.
    # Caller: shoot_button on click.
    def shoot(self):
        # Get current bet.
        bet = self.bet_var.get()

        # Check if bet is lower than 0.
        if bet < 0:
            self.show_message("La apuesta no puede ser menor a 0.", "error")
            return

        # Check if bet is greater than balance, if so, show an error message.
        if bet > self.balance:
            self.show_message("Balance insuficiente.", "error")
            return

        # Generate 3 numbers between 1 and 6.
        generated_numbers = [randint(1, 6) for _ in range(3)]

        # Set label text to the generated number.
        self.numbers_label.config(text="   ".join(map(str, generated_numbers)))

        # Append shoot to shoots.csv.
        with open('shoots.csv', mode='a') as shoots_file:
            shoots_file.write(",".join(map(str, generated_numbers)))
            shoots_file.write("\n")

        # Check whether the user won or not, and update the message label.
        # All the generated numbers must be equal in order for the user to win.
        if all(x == generated_numbers[0] for x in generated_numbers):
            self.update_balance(self.balance + bet * 10)
            self.show_message("¡Usted gano!", "success")
        else:
            self.update_balance(self.balance - bet)
            self.show_message("¡Siga participando!", "info")


root = tk.Tk()
app = Application(master=root)
app.mainloop()
