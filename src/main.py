import customtkinter as ctk
import os
import time
from matrix_frame import matrices
from calc_frame import calc
from graph_frame import graph
from src.Integrales import integral

colors =["2E3440", "D8DEE9", "4C566A", "3B4252", "2F353D"]
prdir = os.path.dirname(os.path.dirname(__file__))
ctk.FontManager.load_font(f"{prdir}/assets/fonts/NotoSansSymbols.ttf")
ctk.FontManager.load_font(f"{prdir}/assets/fonts/NotoSansSymbols2.ttf")
ctk.FontManager.load_font(f"{prdir}/assets/fonts/NotoEmoji.ttf")
ctk.FontManager.load_font(f"{prdir}/assets/fonts/NotoSans.ttf")

root = ctk.CTk()
size = [root.winfo_screenwidth(), root.winfo_screenheight()]
root.geometry(f"{size[0]}x{size[1]}")
root.wm_attributes("-type", "splash")
root.configure(fg_color=f"#{colors[0]}")

columns = 1
frames = []
main_menu = None

topbar = ctk.CTkFrame(root, size[0], int(size[1]/20),20, fg_color=f"#{colors[0]}")
topbar.grid(row=0, column=0, columnspan=1)
topbar.pack_propagate(False)


def create_loading_animation(frame):
    """Display a loading animation for 3 seconds."""
    loading_label = ctk.CTkLabel(
        frame, text="Loading...", font=("NotoSans", size[0] // 100),
        fg_color=f"#{colors[3]}", text_color=f"#{colors[1]}"
    )
    loading_label.place(relx=0.5, rely=0.5, anchor="center")

    for _ in range(3):
        for char in "|/-\\":
            loading_label.configure(text=f"Loading {char}")
            time.sleep(0.2)  # Update every 200ms
            loading_label.update_idletasks()
    loading_label.destroy()

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

        exit_button = ctk.CTkButton(frame, text="\u2613", font=("NotoSansSymbols", size[0]/125),
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
        ctk.CTkLabel(inner_frame, text="Main Menu", font=("NotoSans", size[0]/50), fg_color=f"#{colors[3]}", text_color=f"#{colors[1]}").grid(row=0, column=0, columnspan=2, pady=10)
        ctk.CTkButton(inner_frame, width=50, height=50,  text="[]", font=("NotoSans", size[0]/75), fg_color=f"#{colors[2]}", hover_color=f"#{colors[4]}", text_color=f"#{colors[1]}", command=matrix_frame).grid(row=1, column=0, pady=10, padx=10)
        ctk.CTkButton(inner_frame, width=50, height=50, text="🧮", font=("NotoSans", size[0]/75), fg_color=f"#{colors[2]}", hover_color=f"#{colors[4]}", text_color=f"#{colors[1]}", command=calculator_frame).grid(row=1, column=1, pady=10, padx=10)
        ctk.CTkButton(inner_frame, width=50, height=50, text="\u222B", font=("NotoSans", size[0]/75), fg_color=f"#{colors[2]}", hover_color=f"#{colors[4]}", text_color=f"#{colors[1]}", command=integral_frame).grid(row=2, column=0, pady=10, padx=10)
        ctk.CTkButton(inner_frame, width=50, height=50, text="\U0001F4C8", font=("NotoSans", size[0]/75), fg_color=f"#{colors[2]}", hover_color=f"#{colors[4]}", text_color=f"#{colors[1]}", command=graph_frame).grid(row=2, column=1, pady=10, padx=10)


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
        label = ctk.CTkLabel(frame, text="Integrales", font=("NotoSans", size[0]/50), fg_color=f"#{colors[3]}", text_color=f"#{colors[1]}")
        label.grid(row=0, column=0, columnspan=4, pady=10)


def graph_frame():
    frame = create_frame()
    if frame is not None:
        inner_frame = ctk.CTkFrame(frame, fg_color=f"#{colors[3]}")
        inner_frame.grid(row=1, column=0, columnspan=20)
        graph(inner_frame, colors)


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


exit_button = ctk.CTkButton(topbar, text="\u23FB", font=("NotoSansSymbols", size[0]/125), command=root.quit, width=int(size[0]/50), height=int(size[0]/50), fg_color=f"#{colors[0]}", hover_color=f"#{colors[2]}", text_color=f"#{colors[1]}")
exit_button.pack(side="right", padx=10, pady=5)

config_button = ctk.CTkButton(topbar, text="\u2699", font=("NotoSansSymbols", size[0]/125), width=int(size[0]/50), height=int(size[0]/50), fg_color=f"#{colors[0]}", hover_color=f"#{colors[2]}", text_color=f"#{colors[1]}", command=main_menu_frame)
config_button.pack(side="right", padx=10, pady=5)

time_label = ctk.CTkLabel(topbar, text="00:00", font=("NotoSans", size[0]/125) , fg_color=f"#{colors[0]}", text_color=f"#{colors[1]}")
time_label.pack(side="left", padx=10, pady=5)

get_time()

main_menu_frame()

root.mainloop()