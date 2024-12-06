import customtkinter as ctk
import os
import time
from matrix_frame import matrices
from calc_frame import calc
from graph_frame import graph
from integral_frame import integral
from color_frame import color

prdir = os.path.dirname(os.path.dirname(__file__))
ctk.FontManager.load_font(f"{prdir}/assets/fonts/GoogleSans-Regular.ttf")
ctk.FontManager.load_font(f"{prdir}/assets/fonts/CalcOs-Font2.ttf")
with open(os.path.join(prdir, 'assets', 'colors.txt')) as f:
    colors = [line.strip() for line in f]

root = ctk.CTk()
size = [root.winfo_screenwidth(), root.winfo_screenheight()]
root.geometry(f"{size[0]}x{size[1]}")
root.attributes("-fullscreen", True)
root.configure(fg_color=f"#{colors[0]}")

columns = 1
frames = []
main_menu = None

topbar = ctk.CTkFrame(root, size[0], int(size[1]/20),20, fg_color=f"#{colors[0]}")
topbar.grid(row=0, column=0, columnspan=1)
topbar.pack_propagate(False)

def get_time():
    time_label.configure(text=time.strftime("%H:%M"))
    time_label.after(60000, get_time)

def create_frame():

    if len(frames) != 8:
        frame = ctk.CTkFrame(root, size[0], size[1]-int(size[1]/20),20, fg_color=f"#{colors[3]}")
        frame.grid_forget()
        frame.grid_propagate(False)
        frame.grid_anchor("center")
        frames.append(frame)

        frame.grid_rowconfigure(1, weight=1)
        frame.grid_columnconfigure(1, weight=1)

        frame.grid_columnconfigure(20, weight=0)  # Mantener el botón en su posición

        exit_button = ctk.CTkButton(frame, text="F", font=("CalcOs-Font", size[0]/125),
                                    command=lambda: close_frame(frame), width=int(size[0]/50),
                                    height=int(size[0]/50), fg_color=f"#{colors[0]}",
                                    hover_color=f"#{colors[2]}", text_color=f"#{colors[1]}")
        exit_button.grid(row=0, column=10, pady=10, padx=10, sticky="ne")
        update_frame_grid()
        return frame
    else:
        return None

def main_menu_frame():
    main_menu = create_frame()
    if main_menu is not None:
        inner_frame = ctk.CTkFrame(main_menu, size[0], size[1]-int(size[1]/20),20, fg_color=f"#{colors[3]}")
        inner_frame.grid(row=1, column=1, columnspan=10)
        ctk.CTkLabel(inner_frame, text="Main Menu", font=("Google Sans", size[0]/50), fg_color=f"#{colors[3]}", text_color=f"#{colors[1]}").grid(row=0, column=0, columnspan=2, pady=10)
        ctk.CTkButton(inner_frame, width=50, height=50,  text="B", font=("CalcOs-Font", size[0]/75), fg_color=f"#{colors[2]}", hover_color=f"#{colors[4]}", text_color=f"#{colors[1]}", command=matrix_frame).grid(row=1, column=0, pady=10, padx=10)
        ctk.CTkButton(inner_frame, width=50, height=50, text="D", font=("CalcOs-Font", size[0]/75), fg_color=f"#{colors[2]}", hover_color=f"#{colors[4]}", text_color=f"#{colors[1]}", command=calculator_frame).grid(row=1, column=1, pady=10, padx=10)
        ctk.CTkButton(inner_frame, width=50, height=50, text="A", font=("CalcOs-Font", size[0]/75), fg_color=f"#{colors[2]}", hover_color=f"#{colors[4]}", text_color=f"#{colors[1]}", command=integral_frame).grid(row=2, column=0, pady=10, padx=10)
        ctk.CTkButton(inner_frame, width=50, height=50, text="C", font=("CalcOs-Font", size[0]/75), fg_color=f"#{colors[2]}", hover_color=f"#{colors[4]}", text_color=f"#{colors[1]}", command=graph_frame).grid(row=2, column=1, pady=10, padx=10)


def matrix_frame():
    frame = create_frame()

    if frame is not None:
        inner_frame = ctk.CTkFrame(frame,fg_color=f"#{colors[3]}")
        inner_frame.grid(row=1, column=0, columnspan=20)
        matrices(inner_frame, colors)

def calculator_frame():
    frame = create_frame()
    if frame is not None:
        inner_frame = ctk.CTkFrame(frame, fg_color=f"#{colors[3]}")
        inner_frame.grid(row=1, column=0, columnspan=20)
        calc(inner_frame, colors)

def integral_frame():
    frame = create_frame()
    if frame is not None:
        inner_frame = ctk.CTkFrame(frame,fg_color=f"#{colors[3]}")
        inner_frame.grid(row=1, column=0, columnspan=20)
        integral(inner_frame, colors)

def graph_frame():
    frame = create_frame()
    if frame is not None:
        inner_frame = ctk.CTkFrame(frame, fg_color=f"#{colors[3]}")
        inner_frame.grid(row=1, column=0, columnspan=20)
        graph(inner_frame, colors)

def edit_color_frame():
    frame = create_frame()
    if frame is not None:
        inner_frame = ctk.CTkFrame(frame,fg_color=f"#{colors[3]}")
        inner_frame.grid(row=1, column=0, columnspan=20)
        color(inner_frame, colors)



def close_frame(frame):
    if len(frames) == 1:
        main_menu_frame()
    frames.remove(frame)
    frame.destroy()
    update_frame_grid()

def update_frame_grid():
    total_frames = len(frames)
    if total_frames == 0:
        return  # No hay frames para actualizar

    max_columns = 4  # Máximo número de columnas por fila
    rows = (total_frames + max_columns - 1) // max_columns  # Calcular el número de filas necesarias

    # Configurar los frames en el grid
    for index, frame in enumerate(frames):
        row = index // max_columns  # Determinar la fila del frame
        column = index % max_columns  # Determinar la columna del frame
        frame.grid(row=row + 1, column=column, sticky="nsew", padx=5, pady=5)  # Ajustar el frame al grid

    # Configurar pesos para las columnas, para que cada frame se ajuste automáticamente
    for col in range(max_columns):
        root.grid_columnconfigure(col, weight=1)

    # Configurar pesos para las filas, para que cada fila se ajuste automáticamente
    for r in range(rows):
        root.grid_rowconfigure(r + 1, weight=1)

    # Configurar la barra superior para abarcar todas las columnas
    topbar.grid(row=0, column=0, columnspan=max_columns)

exit_button = ctk.CTkButton(topbar, text="K", font=("CalcOs-Font", size[0]/110), command=root.quit, width=int(size[0]/50), height=int(size[0]/50), fg_color=f"#{colors[0]}", hover_color=f"#{colors[2]}", text_color=f"#{colors[1]}")
exit_button.pack(side="right", padx=10, pady=5)

main_menu_button = ctk.CTkButton(topbar, text="J", font=("CalcOs-Font", size[0]/110), width=int(size[0]/50), height=int(size[0]/50), fg_color=f"#{colors[0]}", hover_color=f"#{colors[2]}", text_color=f"#{colors[1]}", command=main_menu_frame)
main_menu_button.pack(side="right", padx=10, pady=5)

edit_button = ctk.CTkButton(topbar, text="I", font=("CalcOs-Font", size[0]/110), width=int(size[0]/50), height=int(size[0]/50), fg_color=f"#{colors[0]}", hover_color=f"#{colors[2]}", text_color=f"#{colors[1]}", command=edit_color_frame)
edit_button.pack(side="right", padx=10, pady=5)

time_label = ctk.CTkLabel(topbar, text="00:00", font=("Google Sans", size[0]/110) , fg_color=f"#{colors[0]}", text_color=f"#{colors[1]}")
time_label.pack(side="left", padx=10, pady=5)

get_time()

main_menu_frame()

root.mainloop()