#_______________________________________________________________________________
#Name: Atharva Lokhande
#Purpose: Task
#Task: 2
#Author: atharva
#created: 20-07GG-23
#_______________________________________________________________________________

import tkinter as tk
from tkinter import messagebox

def on_button_click(button_text):
    global entry
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except ZeroDivisionError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error: Division by zero")
            messagebox.showerror("Error", "Cannot divide by zero.")
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
            messagebox.showerror("Error", f"An error occurred: {e}")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

def create_button(frame, text, bg="#ECECEC", fg="black"):
    return tk.Button(frame, text=text, padx=20, pady=10, font=("Arial", 16), bg=bg, fg=fg,
                     command=lambda: on_button_click(text))

def create_calculator():
    global entry
    root = tk.Tk()
    root.title("Simple Calculator")
    root.configure(bg="#F0F0F0")

    entry = tk.Entry(root, width=15, font=("Arial", 20))
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    button_texts = [
        ("7", "#D3D3D3", "black"), ("8", "#D3D3D3", "black"), ("9", "#D3D3D3", "black"), ("/", "#FFA500", "white"),
        ("4", "#D3D3D3", "black"), ("5", "#D3D3D3", "black"), ("6", "#D3D3D3", "black"), ("*", "#FFA500", "white"),
        ("1", "#D3D3D3", "black"), ("2", "#D3D3D3", "black"), ("3", "#D3D3D3", "black"), ("-", "#FFA500", "white"),
        ("0", "#D3D3D3", "black"), (".", "#D3D3D3", "black"), ("=", "#FFA500", "white"), ("+", "#FFA500", "white"),
        ("C", "#FF0000", "white")
    ]

    row = 1
    col = 0
    for text, bg, fg in button_texts:
        button = create_button(root, text, bg, fg)
        button.grid(row=row, column=col, padx=5, pady=5)
        col += 1
        if col > 3:
            col = 0
            row += 1

    root.mainloop()

if __name__ == "__main__":
    create_calculator()
