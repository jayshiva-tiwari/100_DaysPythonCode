# Day 46 of Python with programming paglu 🎀

# What You’ll Learn Today:
# Tkinter GUI layout with buttons

# Handling button clicks

# Evaluating expressions

# Displaying results


#  Final Output:
# A small window-based calculator with:

# Number buttons (0–9)
# Operators (+, -, *, /)
# A display area to show inputs and results

# Clear and = buttons


import tkinter as tk

# Step 1: Create main window
window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")

# Step 2: Display entry
entry = tk.Entry(window, width=16, font=('Arial', 24), bd=5, relief='ridge', justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Step 3: Button click handler
def on_click(symbol):
    entry.insert(tk.END, symbol)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Step 4: Button Layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(window, text=text, width=5, height=2, font=('Arial', 18),
                command=calculate).grid(row=row, column=col)
    elif text == 'C':
        tk.Button(window, text=text, width=23, height=2, font=('Arial', 18),
                command=clear).grid(row=row, column=col, columnspan=4)
    else:
        tk.Button(window, text=text, width=5, height=2, font=('Arial', 18),
                command=lambda t=text: on_click(t)).grid(row=row, column=col)

# Step 5: Run the GUI
window.mainloop()


# | Concept    | Explanation                                        |
# | ---------- | -------------------------------------------------- |
# | `Tk()`     | Starts the GUI window                              |
# | `Entry()`  | Input/display area                                 |
# | `Button()` | Creates interactive buttons                        |
# | `.grid()`  | Places widgets in a table layout                   |
# | `eval()`   | Evaluates the math expression (e.g., "2+3\*4")     |
# | `lambda`   | Allows dynamic passing of button value to function |
