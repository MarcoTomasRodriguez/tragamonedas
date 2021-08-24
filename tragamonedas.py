from random import randint
import tkinter as tk

window = tk.Tk()
window.title("Tragamonedas")

# Initialize window title.
title = tk.Label(text="Maquina Tragamonedas", font=("Arial", 16))
title.pack(padx=10, pady=10)

# Initialize numbers.
number_labels = [tk.Label(text="0") for _ in range(3)]
for number_label in number_labels:
    number_label.pack(padx=5, pady=5)

# Generate 3 random numbers, check if all of them are equal and log them in a csv.


def shoot():
    generated_numbers = []

    for number_label in number_labels:
        # Generate number between 1 and 6.
        generated_number = randint(1, 6)

        # Append generated number to list.
        generated_numbers.append(generated_number)

        # Set label text to the generated number.
        number_label["text"] = generated_number

    # Check whether the user won or not, and update the message label.
    # All the generated numbers must be equal in order for the user to win.
    if all(x == generated_numbers[0] for x in generated_numbers):
        message.config(text="Usted gano!", bg="lightgreen")
    else:
        message.config(text="Siga participando!", bg="lightblue")

    # Append shoot to shoots.csv.
    with open('shoots.csv', mode='a') as shoots_file:
        shoots_file.write(",".join(map(str, generated_numbers)))
        shoots_file.write("\n")


# Initialize shoot button & bind "Click" event to shoot.
shoot_button = tk.Button(text="Tirar", command=shoot)
shoot_button.pack()

# Initialize message label.
message = tk.Label(text="¡Haga su primer tiro!", bg="lightblue")
message.pack(padx=5, pady=5)

# Show program authors.
authors = tk.Label(
    text="Trabajo realizado por Alejo Scarlato y Marco Rodriguez")
authors.pack(padx=5, pady=5)

# Enter window main loop and prevent it from closing.
window.mainloop()
