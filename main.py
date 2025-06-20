import customtkinter as tk
import os


# region App Setup
app = tk.CTk()
app.title("Calculator+")
app.geometry("400x600")
app._set_appearance_mode("light")  # Set default appearance mode
# endregion

# region Font Configuration
btn_font = ("Arial", 20, "bold")
display_font = ("Arial", 30, "bold")
optn_font = ("Arial", 12)
# endregion

# region Grid Configuration
app.grid_rowconfigure(0, weight=3) # Display row
app.grid_rowconfigure(1, weight=1)
app.grid_rowconfigure(2, weight=1)
app.grid_rowconfigure(3, weight=1)
app.grid_rowconfigure(4, weight=1)
app.grid_rowconfigure(5, weight=1)

app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=1)
app.grid_columnconfigure(3, weight=1)
# endregion

# region Functions

def one_button_pressed():
    display.configure(state="normal")  # Enable the display to modify it
    current_text = display.get()
    if current_text == "0":
        display.delete(0, tk.END)
    display.insert(tk.END, "1")
    display.configure(state="disabled")  # Disable the display again
def two_button_pressed():
    display.configure(state="normal")  # Enable the display to modify it
    current_text = display.get()
    if current_text == "0":
        display.delete(0, tk.END)
    display.insert(tk.END, "2")
    display.configure(state="disabled")  # Disable the display again

def three_button_pressed():
    display.configure(state="normal")  # Enable the display to modify it
    current_text = display.get()
    if current_text == "0":
        display.delete(0, tk.END)
    display.insert(tk.END, "3")
    display.configure(state="disabled")  # Disable the display again

def four_button_pressed():
    display.configure(state="normal")  # Enable the display to modify it
    current_text = display.get()
    if current_text == "0":
        display.delete(0, tk.END)
    display.insert(tk.END, "4")
    display.configure(state="disabled")  # Disable the display again

def five_button_pressed():
    display.configure(state="normal")  # Enable the display to modify it
    current_text = display.get()
    if current_text == "0":
        display.delete(0, tk.END)
    display.insert(tk.END, "5")
    display.configure(state="disabled")  # Disable the display again

def six_button_pressed():
    display.configure(state="normal")  # Enable the display to modify it
    current_text = display.get()
    if current_text == "0":
        display.delete(0, tk.END)
    display.insert(tk.END, "6")
    display.configure(state="disabled")  # Disable the display again

def seven_button_pressed():
    display.configure(state="normal")  # Enable the display to modify it
    current_text = display.get()
    if current_text == "0":
        display.delete(0, tk.END)
    display.insert(tk.END, "7")
    display.configure(state="disabled")  # Disable the display again

def eight_button_pressed():
    display.configure(state="normal")  # Enable the display to modify it
    current_text = display.get()
    if current_text == "0":
        display.delete(0, tk.END)
    display.insert(tk.END, "8")
    display.configure(state="disabled")  # Disable the display again

def nine_button_pressed():
    display.configure(state="normal")  # Enable the display to modify it
    current_text = display.get()
    if current_text == "0":
        display.delete(0, tk.END)
    display.insert(tk.END, "9")
    display.configure(state="disabled")  # Disable the display again

def zero_button_pressed():
    display.configure(state="normal")  # Enable the display to modify it
    current_text = display.get()
    if current_text == "0":
        display.delete(0, tk.END)
    display.insert(tk.END, "0")
    display.configure(state="disabled")  # Disable the display again

# region Display

white_canvas = tk.CTkCanvas(app, bg="white")
white_canvas.grid(row=0, rowspan=2, column=0, columnspan=4, padx=10, pady=(30,60), sticky="nsew")

display = tk.CTkEntry(app, font=display_font, justify="right",  fg_color="white", text_color="black", border_width=0, corner_radius=0)
display.insert(0, "0")  # Initial value
display.grid(row=0, column=0, columnspan=4, padx=10, pady=(30,60), sticky="nsew")

upper_display = tk.CTkEntry(app, font=optn_font, justify="right", fg_color="white", text_color="black", border_width=0, corner_radius=0)
upper_display.grid(row=0, column=0, columnspan=4, padx=15, pady=(32, 220), sticky="nsew")


display.configure(state="disabled")  # Make the display read-only
# endregion

# region Options
"""
light_mode_button = tk.CTkButton(app, image=light_icon, text="", command=light_mode_button_pressed, height=1, width=2, fg_color="transparent", hover_color="lightblue", text_color="black", font=optn_font)
light_mode_button.grid(padx=3, pady=0, row=0, column=0, sticky="nsew")

dark_mode_button = tk.CTkButton(app, image=dark_icon, text="", command=dark_mode_button_pressed, height=1, width=2, fg_color="transparent", hover_color="lightblue", text_color="black", font=optn_font)
dark_mode_button.grid(padx=3, pady=0, row=0, column=1, sticky="nsew")
"""
# endregion

# region Function Buttons
add_button = tk.CTkButton(app, text="+", command=lambda: (print("Add"), add_button_pressed()), height=4, width=4, fg_color="blue", hover_color="lightblue", text_color="white")
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
one_bt = tk.CTkButton(app, text="1", command=lambda: (print("1"), one_button_pressed()), height=4, width=4, fg_color="white", hover_color="lightblue", text_color="black", font=btn_font, corner_radius=0)
one_bt.grid(padx = 3, pady = 3, row=4, column=0, sticky="nsew")

two_bt = tk.CTkButton(app, text="2", command=lambda: (print("2"), two_button_pressed()), height=4, width=4, fg_color="white", hover_color="lightblue", text_color="black", font=btn_font, corner_radius=0)
two_bt.grid(padx = 3, pady = 3, row=4, column=1, sticky="nsew")

three_bt = tk.CTkButton(app, text="3", command=lambda: (print("3"), three_button_pressed()), height=4, width=4, fg_color="white", hover_color="lightblue", text_color="black", font=btn_font, corner_radius=0)
three_bt.grid(padx = 3, pady = 3, row=4, column=2, sticky="nsew")

four_bt = tk.CTkButton(app, text="4", command=lambda: (print("4"), four_button_pressed()), height=4, width=4, fg_color="white", hover_color="lightblue", text_color="black", font=btn_font, corner_radius=0)
four_bt.grid(padx = 3, pady = 3, row=3, column=0, sticky="nsew")

five_bt = tk.CTkButton(app, text="5", command=lambda: (print("5"), five_button_pressed()), height=4, width=4, fg_color="white", hover_color="lightblue", text_color="black", font=btn_font, corner_radius=0)
five_bt.grid(padx = 3, pady = 3, row=3, column=1, sticky="nsew")

six_bt = tk.CTkButton(app, text="6", command=lambda: (print("6"), six_button_pressed()), height=4, width=4, fg_color="white", hover_color="lightblue", text_color="black", font=btn_font, corner_radius=0)
six_bt.grid(padx = 3, pady = 3, row=3, column=2, sticky="nsew")

seven_bt = tk.CTkButton(app, text="7", command=lambda: (print("7"), seven_button_pressed()), height=4, width=4, fg_color="white", hover_color="lightblue", text_color="black", font=btn_font, corner_radius=0)
seven_bt.grid(padx = 3, pady = 3, row=2, column=0, sticky="nsew")

eight_bt = tk.CTkButton(app, text="8", command=lambda: (print("8"), eight_button_pressed()), height=4, width=4, fg_color="white", hover_color="lightblue", text_color="black", font=btn_font, corner_radius=0)
eight_bt.grid(padx = 3, pady = 3, row=2, column=1, sticky="nsew")

nine_bt = tk.CTkButton(app, text="9", command=lambda: (print("9"), nine_button_pressed()), height=4, width=4, fg_color="white", hover_color="lightblue", text_color="black", font=btn_font, corner_radius=0)
nine_bt.grid(padx = 3, pady = 3, row=2, column = 2, sticky="nsew")

zero_bt = tk.CTkButton(app, text="0", command=lambda: (print("0"), zero_button_pressed()), height=4, width=8, fg_color="white", hover_color="lightblue", text_color="black", font=btn_font, corner_radius=0)
zero_bt.grid(padx = 3, pady = (3, 5), row=5, column=0, columnspan=2, sticky="nsew")
# endregion

app.mainloop()

