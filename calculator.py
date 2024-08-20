import tkinter as tk

def add_to_expression(value):
    current_text = expression_entry.get()
    expression_entry.delete(0, tk.END)
    expression_entry.insert(0, current_text + str(value))

def evaluate_expression():
    try:
        result = eval(expression_entry.get())
        expression_entry.delete(0, tk.END)
        expression_entry.insert(0, str(result))
    except Exception as e:
        expression_entry.delete(0, tk.END)
        expression_entry.insert(0, "Error")

def clear_expression():
    expression_entry.delete(0, tk.END)

# Initialize the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create an entry widget to display the expression
expression_entry = tk.Entry(root, width=30, borderwidth=5, font=('Arial', 18))
expression_entry.grid(row=0, column=0, columnspan=4)

# Create buttons for digits, operators, and actions
button_texts = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0, 4)
]

# Define button actions
for text, row, col, *span in button_texts:
    span = span[0] if span else 1
    if text == '=':
        action = evaluate_expression
    elif text == 'C':
        action = clear_expression
    else:
        action = lambda value=text: add_to_expression(value)

    tk.Button(root, text=text, width=10, height=3, command=action).grid(row=row, column=col, columnspan=span)

# Run the main event loop
root.mainloop()
