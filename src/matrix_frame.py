import customtkinter as ctk
import numpy as np
import matrix_operation as mt

def calculate_matrices(m1, m2, r, operation):
    if operation == "sum":
        result = mt.sumaMatrices(m1, m2)
    elif operation == "point":
        result = mt.productoPunto(m1, m2)
    elif operation == "traspuesta":
        result = mt.traspuesta(m1)
    elif operation == "inversa":
        result = mt.inversa(m1)
    update_result(r, result)

def update_result(entries, result):
    for i in range(3):
        for j in range(3):
            entries[i * 3 + j].delete(0, "end")
            entries[i * 3 + j].insert(0, result[i][j])

def matrices(p, colors):
    wid=p.winfo_screenwidth()/200+30
    hig=p.winfo_screenheight()/200+30
    entriesM1 = []
    entriesM2 = []
    entriesR = []
    row_val = 1
    col_val = 0

    ctk.CTkButton(p, width=50, height=50, text="E", command=lambda: calculate_matrices(getnpmatrix(entriesM1), getnpmatrix(entriesM2), entriesR,"sum"), fg_color=f"#{colors[2]}", hover_color=f"#{colors[4]}", text_color=f"#{colors[1]}", font=("CalcOs-Font", 20)).grid(row=2, column=4, padx=5, pady=5)
    ctk.CTkButton(p, width=50, height=50, text="F", command=lambda: calculate_matrices(getnpmatrix(entriesM1), getnpmatrix(entriesM2), entriesR, "point"), fg_color=f"#{colors[2]}", hover_color=f"#{colors[4]}", text_color=f"#{colors[1]}", font=("CalcOs-Font", 20)).grid(row=3, column=4, padx=5, pady=5)
    ctk.CTkButton(p, width=50, height=50, text="G", command=lambda: calculate_matrices(getnpmatrix(entriesM1), getnpmatrix(entriesM2), entriesR, "traspuesta"), fg_color=f"#{colors[2]}", hover_color=f"#{colors[4]}", text_color=f"#{colors[1]}", font=("CalcOs-Font", 20)).grid(row=4, column=4, padx=5, pady=5)
    ctk.CTkButton(p, width=50, height=50, text="H", command=lambda: calculate_matrices(getnpmatrix(entriesM1), getnpmatrix(entriesM2), entriesR, "inversa"), fg_color=f"#{colors[2]}", hover_color=f"#{colors[4]}", text_color=f"#{colors[1]}", font=("CalcOs-Font", 20)).grid(row=5, column=4, padx=5, pady=5)

    for a in range(9):
        entry = ctk.CTkEntry(p, width=wid, height=hig, fg_color=f"#{colors[0]}", text_color=f"#{colors[1]}", border_width=0, font=("Google Sans", 15))
        entry.grid(row=row_val, column=col_val, padx=5, pady=5)
        entriesM1.append(entry)
        col_val += 1
        if col_val > 2:
            col_val = 0
            row_val += 1

    row_val = 1
    col_val = 0
    for a in range(9):
        # action = lambda x=button: on_button_click(x)
        entry = ctk.CTkEntry(p, width=wid+20, height=hig, fg_color=f"#{colors[0]}", text_color=f"#{colors[1]}", border_width=0, font=("Google Sans", 15))
        entry.grid(row=row_val + 2, column=col_val + 6, padx=5, pady=5)
        entriesR.append(entry)
        col_val += 1
        if col_val > 2:
            col_val = 0
            row_val += 1

    row_val = 1
    col_val = 0
    for a in range(9):
        # action = lambda x=button: on_button_click(x)
        entry = ctk.CTkEntry(p, width=wid, height=hig, fg_color=f"#{colors[0]}", text_color=f"#{colors[1]}", border_width=0, font=("Google Sans", 15))
        entry.grid(row=row_val + 4, column=col_val, padx=5, pady=5)
        entriesM2.append(entry)
        col_val += 1
        if col_val > 2:
            col_val = 0
            row_val += 1


def getnpmatrix(entries):
    print(entries)
    matrix = np.array([[float(entries[i * 3 + j].get() or 0) for j in range(3)] for i in range(3)])
    return matrix