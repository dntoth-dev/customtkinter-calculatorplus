import customtkinter as tk
import os


# region App Setup
app = tk.CTk()
app.title("Calculator+")
app.geometry("400x600")
app.resizable(False, False)  # Disable resizing
app._set_appearance_mode("light")  # Set default appearance mode
app.configure(fg_color="light grey")
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

def button_pressed(btn):
    display.configure(state="normal")
    current_text = display.get("3.0", "3.end")
    
    # Clear leading 0 if a number is pressed
    if current_text.strip() == "0" and btn not in ["+", "-", "×", "÷", "."]:
        display.delete("3.0", "3.end")
    
    # Replace last operator if a new one is pressed
    if btn in ["+", "-", "×", "÷"] and current_text.endswith(("+", "-", "×", "÷")):
        display.delete("3.end-1c")
       
        
    # Insert the character
    display.insert(tk.END, btn)
    display.configure(state="disabled")

def equal_button_pressed():
    try:
        current_text = display.get("3.0", "3.end")
        # Replace the custom "×" and "÷" with standard Python operators
        expression = current_text.replace("×", "*").replace("÷", "/")
        
        # Use eval() to calculate the result
        result = eval(expression)
        
        # Display the result
        display.configure(state="normal")
        display.delete(3.0, "3.end")
        display.insert("3.0", str(result))
        display.configure(state="disabled")

    except ZeroDivisionError:
        display.configure(state="normal")
        display.delete(3.0, tk.END)
        display.insert(3.0, "Error: Div by zero")
        display.configure(state="disabled")
    except (SyntaxError, ValueError):
        display.configure(state="normal")
        display.delete(3.0, tk.END)
        display.insert(3.0, "Error: Invalid input")
        display.configure(state="disabled")
    except Exception as e:
        display.configure(state="normal")
        display.delete(3.0, tk.END)
        display.insert(3.0, "Error")
        display.configure(state="disabled")



# region Display

# white_canvas = tk.CTkCanvas(app, bg="white")
# white_canvas.grid(row=0, rowspan=2, column=0, columnspan=4, padx=10, pady=(30,60))

display = tk.CTkTextbox(app, font=display_font,  fg_color="white", text_color="black", border_width=0, height=200, width=370)
display.insert(1.0, "\n")
display.insert(2.0, "\n")
display.insert(3.0, "0")  # Initial value
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# upper_display = tk.CTkEntry(app, font=optn_font, justify="right", fg_color="white", text_color="black", border_width=0)
# upper_display.grid(row=0, column=0, columnspan=4, padx=15, pady=(32, 220))


display.configure(state="disabled")  # Make the display read-only
# upper_display.configure(state="disabled")  # Make the upper display read-only

# endregion

# region Options
"""
light_mode_button = tk.CTkButton(app, image=light_icon, text="", command=light_mode_button_pressed, height=1, width=2, fg_color="transparent", hover_color="lightblue", text_color="black", font=optn_font)
light_mode_button.grid(padx=3, pady=0, row=0, column=0)

dark_mode_button = tk.CTkButton(app, image=dark_icon, text="", command=dark_mode_button_pressed, height=1, width=2, fg_color="transparent", hover_color="lightblue", text_color="black", font=optn_font)
dark_mode_button.grid(padx=3, pady=0, row=0, column=1)
"""
# endregion

# region Function Buttons

clearEntry_button = tk.CTkButton(app, text="CE", command=lambda: (print("Clear Entry")), height=70, width=95, fg_color="orange", hover_color="dark grey", text_color="white", font=btn_font)
clearEntry_button.grid(row=1, column=2, pady=1)
clear_button = tk.CTkButton(app, text="C", command=lambda: (print("Clear")), height=70, width=95, fg_color="orange", hover_color="dark grey", text_color="white", font=btn_font)
clear_button.grid(row=1, column=3, pady=1)
DEL_button = tk.CTkButton(app, text="DEL", command=lambda: (print("Delete")), height=70, width=95, fg_color="orange", hover_color="dark grey", text_color="white", font=btn_font)
DEL_button.grid(row=1, column=1, pady=1)
M_button = tk.CTkButton(app, text="M", command=lambda: (print("Memory")), height=70, width=95, fg_color="orange", hover_color="dark grey", text_color="white", font=btn_font)
M_button.grid(row=1, column=0, pady=1)


add_button = tk.CTkButton(app, text="+", command=lambda: (print("Add"), button_pressed("+")), height=70, width=95, fg_color="blue", hover_color="lightblue", text_color="white", font=btn_font)
add_button.grid(row=2, column=3)
subtract_button = tk.CTkButton(app, text="-", command=lambda: (print("Subtract"), button_pressed("-")), height=70, width=95, fg_color="blue", hover_color="lightblue", text_color="white", font=btn_font)
subtract_button.grid(row=3, column=3)
multiply_button = tk.CTkButton(app, text="×", command=lambda: (print("Multiply"), button_pressed("×")), height=70, width=95, fg_color="blue", hover_color="lightblue", text_color="white", font=btn_font)
multiply_button.grid(row=4, column=3)
divide_button = tk.CTkButton(app, text="÷", command=lambda: (print("Divide"), button_pressed("÷")), height=70, width=95, fg_color="blue", hover_color="lightblue", text_color="white", font=btn_font)
divide_button.grid(row=5, column=3)

equal_button = tk.CTkButton(app, text="=", command=lambda: (print("Equal to"), equal_button_pressed()), height=70, width=95, fg_color="green", hover_color="lightblue", text_color="white", font=btn_font)
equal_button.grid(row=5, column=2)
# endregion

# region Number Buttons
one_bt = tk.CTkButton(app, text="1", command=lambda: (print("1"), button_pressed(1)), height=70, width=95, fg_color="white", hover_color="lightblue", text_color="black", font=btn_font)
one_bt.grid(row=4, column=0, pady=1)

two_bt = tk.CTkButton(app, text="2", command=lambda: (print("2"), button_pressed(2)), height=70, width=95, fg_color="white", hover_color="lightblue", text_color="black", font=btn_font)
two_bt.grid(row=4, column=1, pady=1)

three_bt = tk.CTkButton(app, text="3", command=lambda: (print("3"), button_pressed(3)), height=70, width=95, fg_color="white", hover_color="lightblue", text_color="black", font=btn_font)
three_bt.grid(row=4, column=2, pady=1)

four_bt = tk.CTkButton(app, text="4", command=lambda: (print("4"), button_pressed(4)), height=70, width=95, fg_color="white", hover_color="lightblue", text_color="black", font=btn_font)
four_bt.grid(row=3, column=0, pady=1)

five_bt = tk.CTkButton(app, text="5", command=lambda: (print("5"), button_pressed(5)), height=70, width=95, fg_color="white", hover_color="lightblue", text_color="black", font=btn_font)
five_bt.grid(row=3, column=1, pady=1)

six_bt = tk.CTkButton(app, text="6", command=lambda: (print("6"), button_pressed(6)), height=70, width=95, fg_color="white", hover_color="lightblue", text_color="black", font=btn_font)
six_bt.grid(row=3, column=2, pady=1)

seven_bt = tk.CTkButton(app, text="7", command=lambda: (print("7"), button_pressed(7)), height=70, width=95, fg_color="white", hover_color="lightblue", text_color="black", font=btn_font)
seven_bt.grid(row=2, column=0, pady=1)

eight_bt = tk.CTkButton(app, text="8", command=lambda: (print("8"), button_pressed(8)), height=70, width=95, fg_color="white", hover_color="lightblue", text_color="black", font=btn_font)
eight_bt.grid(row=2, column=1, pady=1)

nine_bt = tk.CTkButton(app, text="9", command=lambda: (print("9"), button_pressed(9)), height=70, width=95, fg_color="white", hover_color="lightblue", text_color="black", font=btn_font)
nine_bt.grid(row=2, column=2, pady=1)

zero_bt = tk.CTkButton(app, text="0", command=lambda: (print("0"), button_pressed(0)), height=70, width=190, fg_color="white", hover_color="lightblue", text_color="black", font=btn_font)
zero_bt.grid(row=5, column=0, columnspan=2, pady=1)
# endregion

app.mainloop()

