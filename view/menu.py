import customtkinter
import customtkinter as ctk
import os

colors =["000000", "ffffff", "252525", "505050"]
prdir = os.path.dirname(os.path.dirname(__file__))
customtkinter.FontManager.load_font(f"{prdir}/assets/fonts/NotoSansSymbols.ttf")
customtkinter.FontManager.load_font(f"{prdir}/assets/fonts/NotoSansSymbols2.ttf")
customtkinter.FontManager.load_font(f"{prdir}/assets/fonts/NotoEmoji.ttf")
customtkinter.FontManager.load_font(f"{prdir}/assets/fonts/NotoSans.ttf")

root = ctk.CTk()
size = [root.winfo_screenwidth(), root.winfo_screenheight()]
root.geometry(f"{size[0]}x{size[1]}")
root.wm_attributes("-type", "splash")

columns = 1
frames = []
main_menu = None

topbar = ctk.CTkFrame(root, size[0], int(size[1]/20),20, fg_color=f"#{colors[0]}")
topbar.grid(row=0, column=0, columnspan=1)
topbar.pack_propagate(False)


exit_button = ctk.CTkButton(topbar, text="\u23FB", font=("NotoSansSymbols", size[0]/125), command=root.quit, width=int(size[0]/50), height=int(size[0]/50), fg_color=f"#{colors[0]}", hover_color=f"#{colors[2]}", text_color=f"#{colors[1]}")
exit_button.pack(side="right", padx=10, pady=5)

config_button = ctk.CTkButton(topbar, text="\u2699", font=("NotoSansSymbols", size[0]/125), width=int(size[0]/50), height=int(size[0]/50), fg_color=f"#{colors[0]}", hover_color=f"#{colors[2]}", text_color=f"#{colors[1]}")
config_button.pack(side="right", padx=10, pady=5)

time_label = ctk.CTkLabel(topbar, text="00:00", font=("NotoSans", size[0]/125) , fg_color=f"#{colors[0]}", text_color=f"#{colors[1]}")
time_label.pack(side="left", padx=10, pady=5)

def get_time():
    import time
    time_label.configure(text=time.strftime("%H:%M"))
    time_label.after(60000, get_time)

def create_frame():
    if len(frames) != 12:
        frame = ctk.CTkFrame(root, size[0], size[1]-int(size[1]/20),20, fg_color=f"#{colors[3]}")
        frame.grid_forget()
        frame.grid_propagate(False)
        frame.grid_anchor("center")
        frames.append(frame)
        update_frame_grid()
        return frame
    else:
        return None

def main_menu_frame():
    main_menu = create_frame()
    ctk.CTkLabel(main_menu, text="Main Menu", font=("NotoSans", size[0]/50), fg_color=f"#{colors[3]}", text_color=f"#{colors[1]}").grid(row=0, column=0, columnspan=2, pady=10)
    ctk.CTkButton(main_menu, width=50, height=50,  text="[]", font=("NotoSans", size[0]/75), fg_color=f"#{colors[3]}", hover_color=f"#{colors[2]}", text_color=f"#{colors[1]}", command=matrix_frame).grid(row=1, column=0, pady=10, padx=10)
    ctk.CTkButton(main_menu, width=50, height=50, text="🧮", font=("NotoSans", size[0]/75), fg_color=f"#{colors[3]}", hover_color=f"#{colors[2]}", text_color=f"#{colors[1]}", command=calculator_frame).grid(row=1, column=1, pady=10, padx=10)
    ctk.CTkButton(main_menu, width=50, height=50, text="\u222B", font=("NotoSans", size[0]/75), fg_color=f"#{colors[3]}", hover_color=f"#{colors[2]}", text_color=f"#{colors[1]}", command=integral_frame).grid(row=2, column=0, pady=10, padx=10)
    ctk.CTkButton(main_menu, width=50, height=50, text="\U0001F4C8", font=("NotoSans", size[0]/75), fg_color=f"#{colors[3]}", hover_color=f"#{colors[2]}", text_color=f"#{colors[1]}", command=graph_frame).grid(row=2, column=1, pady=10, padx=10)


def matrix_frame():
    frame = create_frame()
    if frame is not None:
        label = ctk.CTkLabel(frame, text="Matrices", font=("NotoSans", size[0]/50), fg_color=f"#{colors[3]}", text_color=f"#{colors[1]}")
        label.grid(row=0, column=0, columnspan=4, pady=10)


def calculator_frame():
    frame = create_frame()
    if frame is not None:
        label = ctk.CTkLabel(frame, text="Calculadora", font=("NotoSans", size[0]/50), fg_color=f"#{colors[3]}", text_color=f"#{colors[1]}")
        label.grid(row=0, column=0, columnspan=4, pady=10)


def integral_frame():
    frame = create_frame()
    if frame is not None:
        label = ctk.CTkLabel(frame, text="Integrales", font=("NotoSans", size[0]/50), fg_color=f"#{colors[3]}", text_color=f"#{colors[1]}")
        label.grid(row=0, column=0, columnspan=4, pady=10)


def graph_frame():
    frame = create_frame()
    if frame is not None:
        label = ctk.CTkLabel(frame, text="Gráficas", font=("NotoSans", size[0]/50), fg_color=f"#{colors[3]}", text_color=f"#{colors[1]}")
        label.grid(row=0, column=0, columnspan=4, pady=10)


def update_frame_grid():
    print(frames)
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


get_time()

main_menu_frame()

root.mainloop()