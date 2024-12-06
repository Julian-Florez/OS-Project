import math

import customtkinter as ctk
import sympy as sp
from django.db.models.sql.datastructures import Empty
from sympy import integrate
from sympy.abc import x


entrada_activa = None
def activar_entrada(event):
    global entrada_activa
    entrada_activa = event.widget


def integral(frame, colors):
    wid = frame.winfo_screenwidth() / 200 + 30
    input_entry = ctk.CTkEntry(frame, width=200, fg_color=f"#{colors[0]}", text_color=f"#{colors[1]}",placeholder_text="")
    input_entry.grid(row=2, column=1, columnspan=3, pady=10, padx=10)
    input_entry.bind("<Button-1>", activar_entrada)

    superior = ctk.CTkEntry(frame, width=wid,fg_color=f"#{colors[2]}", text_color=f"#{colors[1]}",placeholder_text="")
    superior.grid(row=0, column=0, padx=5, pady=0)
    superior.bind("<Button-1>", activar_entrada)

    inferior = ctk.CTkEntry(frame, width=wid,fg_color=f"#{colors[2]}", text_color=f"#{colors[1]}",placeholder_text="")
    inferior.grid(row=3, column=0, padx=5, pady=0)
    inferior.bind("<Button-1>",activar_entrada)

    image = ctk.CTkLabel(frame,50,20,text="\u222B",font=("NotoSans", 100), fg_color=f"#{colors[3]}", text_color=f"#{colors[1]}")
    image.grid(row=2,column=0,padx=5,pady=10)

    igual = ctk.CTkLabel(frame, 50, text="dx =", font=("NotoSans", 20), fg_color=f"#{colors[3]}",
                         text_color=f"#{colors[1]}")
    igual.grid(row=2, column=4, padx=5, pady=10)
    output = ctk.CTkEntry(frame, width=wid+50,fg_color=f"#{colors[2]}", text_color=f"#{colors[1]}")
    output.grid(row=2,column=6,padx=5,pady=10)






    def evaluate_expression():
        try:
            output.delete(0, "end")
            lim_sup = superior.get()
            lim_inf = inferior.get()
            if lim_sup != "" and lim_inf != "":
                expr = input_entry.get()
                result = integrate(sp.sympify(expr),(x,lim_inf,lim_sup))
            else:
                expr = input_entry.get()
                result = sp.sympify(expr).integrate()
            result = str(result).rstrip('0').rstrip('.') if '.' in str(result) else str(result)
            output.delete(0, "end")  # Clear the entry field
            output.insert(0, str(result))  # Insert the result into the entry
        except Exception as e:
            output.delete(0, "end")  # Clear the entry field
            output.insert(0, f"Error")  # Show the error in the entry

    def append_to_input(char):
        #entrada = event.widget
        if entrada_activa:
            entrada_activa.insert("end", char)

    def clear_entry():
        input_entry.delete(0, "end")
        output.delete(0, "end")
        superior.delete(0, "end")
        inferior.delete(0, "end")

    def delete_last_char():
        if entrada_activa:
            current_text = entrada_activa.get()
            entrada_activa.delete(0, "end")
            entrada_activa.insert(0, current_text[:-1])


    buttons = [
        ("C", 1, 2), (" + ", 1, 3),("x",1,0),
        ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), (" / ", 2, 3),
        ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), (" * ", 3, 3),
        ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), (" - ", 4, 3),
        ("0", 5, 0), (".", 5, 1), (" (", 5, 2), (")", 5, 3),
        ("√", 6, 0), ("^", 6, 1),("sin", 7, 0), ("cos", 7, 1),
        ("tan", 7, 2), ("del", 1, 1),("π",7,3)
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
        elif text =="π":
            command = lambda : append_to_input(f"{math.pi}")
        else:
            command = lambda t=text: append_to_input(f"{t}")

        button = ctk.CTkButton(
            frame,
            text=text,
            command=command,
            width=50,height=10,corner_radius=20,
            fg_color=f"#{colors[2]}",
            hover_color=f"#{colors[3]}",
            text_color=f"#{colors[1]}"
        )
        button.grid(row=row+2, column=col+1, pady=5, padx=5)

    evaluate_button = ctk.CTkButton(
        frame,
        text="=",height=10,corner_radius=20,width=100,
        command=evaluate_expression,
        fg_color=f"#{colors[2]}",
        hover_color=f"#{colors[3]}",
        text_color=f"#{colors[1]}"
    )
    evaluate_button.grid(row=8, column=3, columnspan=2, pady=10, padx=10)

