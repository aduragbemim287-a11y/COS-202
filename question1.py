from tkinter import *

# Create window
root = Tk()
root.title("Mathematical Calculator (MC)")
root.geometry("350x500")
root.resizable(False, False)

# Entry box
entry = Entry(root, font=("Arial", 20), bd=8, relief=RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to insert values
def press(value):
    entry.insert(END, value)

# Function to clear screen
def clear():
    entry.delete(0, END)

# Function to evaluate expression
def calculate():
    try:
        expression = entry.get()

        # Replace ^ with ** for exponent
        expression = expression.replace("^", "**")

        # Replace \ with // for integer division
        expression = expression.replace("\\", "//")

        result = eval(expression)

        entry.delete(0, END)
        entry.insert(END, str(result))
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

# Function to close calculator
def off():
    root.destroy()

# Button layout
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('%',4,2), ('+',4,3),
    ('^',5,0), ('\\',5,1), ('C',5,2), ('=',5,3),
]

for (text, row, col) in buttons:
    if text == "C":
        Button(root, text=text, width=8, height=3,
               command=clear).grid(row=row, column=col, padx=5, pady=5)
    elif text == "=":
        Button(root, text=text, width=8, height=3,
               command=calculate).grid(row=row, column=col, padx=5, pady=5)
    else:
        Button(root, text=text, width=8, height=3,
               command=lambda t=text: press(t)).grid(row=row, column=col, padx=5, pady=5)

# OFF button
Button(root, text="OFF", bg="red", fg="white",
       width=35, height=2, command=off).grid(row=6, column=0, columnspan=4, padx=5, pady=10)

root.mainloop()