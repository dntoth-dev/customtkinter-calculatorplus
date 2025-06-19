import customtkinter as tk
from PIL import Image, ImageTk

# region App Setup
app = tk.CTk()
app.title("Calculator+")
app.geometry("400x600")
# endregion

# region Font Configuration
btn_font = ("Arial", 20, "bold")
display_font = ("Arial", 30, "bold")
optn_font = ("Arial", 12, "bold")
# endregion

# region Grid Configuration
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=3)
app.grid_rowconfigure(2, weight=1)
app.grid_rowconfigure(3, weight=1)
app.grid_rowconfigure(4, weight=1)
app.grid_rowconfigure(5, weight=1)

app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=1)
app.grid_columnconfigure(3, weight=1)
# endregion

# region Display
display = tk.CTkEntry(app, font=display_font, justify="right", fg_color="white", text_color="black")
display.insert(0, "0")  # Initial value
display.grid(row=1, column=0, columnspan=4, padx=10, pady=(0,30), sticky="nsew")
# endregion

# region Function Buttons
add_button = tk.CTkButton(app, text="+", command=lambda: print("Add"), height=4, width=4, fg_color="blue", hover_color="lightblue", text_color="white", font=btn_font)
add_button.grid(padx = 3, pady = 3, row=2, column=3, sticky="nsew")
subtract_button = tk.CTkButton(app, text="-", command=lambda: print("Subtract"), height=4, width=4, fg_color="blue", hover_color="lightblue", text_color="white", font=btn_font)
subtract_button.grid(padx = 3, pady = 3, row=3, column=3, sticky="nsew")
multiply_button = tk.CTkButton(app, text="×", command=lambda: print("Multiply"), height=4, width=4, fg_color="blue", hover_color="lightblue", text_color="white", font=btn_font)
multiply_button.grid(padx = 3, pady = 3, row=4, column=3, sticky="nsew")
divide_button = tk.CTkButton(app, text="÷", command=lambda: print("Divide"), height=4, width=4, fg_color="blue", hover_color="lightblue", text_color="white", font=btn_font)
divide_button.grid(padx = 3, pady = (3, 5), row=5, column=3, sticky="nsew")

equal_button = tk.CTkButton(app, text="=", command=lambda: print("Equal to"), height=4, width=4, fg_color="green", hover_color="lightblue", text_color="white", font=btn_font)
equal_button.grid(padx = 3, pady = (3, 5), row=5, column=2, sticky="nsew")
# endregion

# region Number Buttons
one_bt = tk.CTkButton(app, text="1", command=lambda: print("1"), height=4, width=4, fg_color="white", hover_color="lightblue", text_color="black", font=btn_font)
one_bt.grid(padx = 3, pady = 3, row=4, column=0, sticky="nsew")

two_bt = tk.CTkButton(app, text="2", command=lambda: print("2"), height=4, width=4, fg_color="white", hover_color="lightblue", text_color="black", font=btn_font)
two_bt.grid(padx = 3, pady = 3, row=4, column=1, sticky="nsew")

three_bt = tk.CTkButton(app, text="3", command=lambda: print("3"), height=4, width=4, fg_color="white", hover_color="lightblue", text_color="black", font=btn_font)
three_bt.grid(padx = 3, pady = 3, row=4, column=2, sticky="nsew")

four_bt = tk.CTkButton(app, text="4", command=lambda: print("4"), height=4, width=4, fg_color="white", hover_color="lightblue", text_color="black", font=btn_font)
four_bt.grid(padx = 3, pady = 3, row=3, column=0, sticky="nsew")

five_bt = tk.CTkButton(app, text="5", command=lambda: print("5"), height=4, width=4, fg_color="white", hover_color="lightblue", text_color="black", font=btn_font)
five_bt.grid(padx = 3, pady = 3, row=3, column=1, sticky="nsew")

six_bt = tk.CTkButton(app, text="6", command=lambda: print("6"), height=4, width=4, fg_color="white", hover_color="lightblue", text_color="black", font=btn_font)
six_bt.grid(padx = 3, pady = 3, row=3, column=2, sticky="nsew")

seven_bt = tk.CTkButton(app, text="7", command=lambda: print("7"), height=4, width=4, fg_color="white", hover_color="lightblue", text_color="black", font=btn_font)
seven_bt.grid(padx = 3, pady = 3, row=2, column=0, sticky="nsew")

eight_bt = tk.CTkButton(app, text="8", command=lambda: print("8"), height=4, width=4, fg_color="white", hover_color="lightblue", text_color="black", font=btn_font)
eight_bt.grid(padx = 3, pady = 3, row=2, column=1, sticky="nsew")

nine_bt = tk.CTkButton(app, text="9", command=lambda: print("9"), height=4, width=4, fg_color="white", hover_color="lightblue", text_color="black", font=btn_font)
nine_bt.grid(padx = 3, pady = 3, row=2, column = 2, sticky="nsew")

zero_bt = tk.CTkButton(app, text="0", command=lambda: print("0"), height=4, width=8, fg_color="white", hover_color="lightblue", text_color="black", font=btn_font)
zero_bt.grid(padx = 3, pady = (3, 5), row=5, column=0, columnspan=2, sticky="nsew")
# endregion

app.mainloop()

