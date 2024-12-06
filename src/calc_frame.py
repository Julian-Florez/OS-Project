import sympy as sp
import customtkinter as ctk

def calc(frame, colors):
    def evaluate_expression():
        try:
            expr = input_entry.get()
            result = sp.sympify(expr).evalf()
            result = str(result).rstrip('0').rstrip('.') if '.' in str(result) else str(result)
            input_entry.delete(0, "end")  # Clear the entry field
            input_entry.insert(0, str(result))  # Insert the result into the entry
        except Exception as e:
            input_entry.delete(0, "end")  # Clear the entry field
            input_entry.insert(0, f"Error")  # Show the error in the entry

    def append_to_input(char):
        input_entry.insert("end", char)

    def clear_entry():
        input_entry.delete(0, "end")

    def delete_last_char():
        current_text = input_entry.get()
        input_entry.delete(0, "end")
        input_entry.insert(0, current_text[:-1])

    input_entry = ctk.CTkEntry(frame, width=300, fg_color=f"#{colors[0]}", text_color=f"#{colors[1]}")
    input_entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

    buttons = [
        ("C", 1, 0), ("√", 1, 1), ("^", 1, 2), (" + ", 1, 3),
        ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), (" / ", 2, 3),
        ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), (" * ", 3, 3),
        ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), (" - ", 4, 3),
        ("0", 5, 0), (".", 5, 1), (" (", 5, 2), (")", 5, 3),
        ("mod", 7, 0), ("! ", 7, 3),
        ("sin", 6, 0), ("cos", 6, 1), ("tan", 6, 2), ("del", 6, 3)
    ]

    for text, row, col in buttons:
        if text == "del":
            command = delete_last_char
        elif text == "C":
            command = clear_entry
        elif text == "√":
            command = lambda: append_to_input(" sqrt(")
        elif text == "^":
            command = lambda: append_to_input(" ** ")
        elif text == "mod":
            command = lambda: append_to_input(" % ")
        elif text == "!":
            command = lambda: append_to_input("! ")
        elif text in {"sin", "cos", "tan"}:
            command = lambda t=text: append_to_input(f" {t}(")
        else:
            command = lambda t=text: append_to_input(f"{t}")

        button = ctk.CTkButton(
            frame,
            text=text,
            command=command,
            width=50,
            fg_color=f"#{colors[2]}",
            hover_color=f"#{colors[3]}",
            text_color=f"#{colors[1]}"
        )
        button.grid(row=row, column=col, pady=5, padx=5)

    evaluate_button = ctk.CTkButton(
        frame,
        text="=",
        command=evaluate_expression,
        fg_color=f"#{colors[2]}",
        hover_color=f"#{colors[3]}",
        text_color=f"#{colors[1]}"
    )
    evaluate_button.grid(row=8, column=0, columnspan=4, pady=10, padx=10)
