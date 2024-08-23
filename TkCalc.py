import tkinter as tk

window = tk.Tk()
window.title("Simple Calculator")

entry = tk.Entry(window, width=16, font=("Arial", 24), bd=8, insertwidth=4, justify="right")
entry.grid(row=0, column=0, columnspan=4)

current_expression = ""

def button_click(number):
    """Handles button clicks for numbers and operators."""
    global current_expression
    current_expression += str(number)
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_expression)

def button_clear():
    """Clears the entry widget and the current expression."""
    global current_expression
    current_expression = ""
    entry.delete(0, tk.END)

def button_equal():
    """Evaluates the current expression and displays the result."""
    global current_expression
    try:
        result = str(eval(current_expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        current_expression = result   
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        current_expression = ""

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(window, text=text, padx=20, pady=20, font=("Arial", 18), command=button_equal)
    else:
        button = tk.Button(window, text=text, padx=20, pady=20, font=("Arial", 18), command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)

clear_button = tk.Button(window, text='C', padx=20, pady=20, font=("Arial", 18), command=button_clear)
clear_button.grid(row=5, column=0, columnspan=4)  

window.mainloop()
