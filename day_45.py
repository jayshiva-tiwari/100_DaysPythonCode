# Day 45 of Python with Programming Paglu 🎀

# What is Tkinter?
# A standard GUI library for Python.

# Comes pre-installed with Python.

# Helps you build windows, buttons, labels, forms, etc.


# first  import the tkinter
import tkinter as tk

# create a window
window = tk.Tk()

# set the title of the window
window.title("My notes app")

# set the size of the window
window.geometry("400x300") # width x height

# create a label
label = tk.Label(window, text="Hello, Shiva!", font=("Arial", 18))


# add the label to the window
label.pack(pady=20)


# start the main loop / Run the window
window.mainloop()

