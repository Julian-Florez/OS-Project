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
topbar.grid(row=0, column=0, columnspan=4)
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
    frame = ctk.CTkFrame(root, size[0], size[1]-int(size[1]/20),20, fg_color=f"#{colors[3]}")
    frame.grid_forget()
    frame.grid_propagate(False)
    frame.grid_anchor("center")
    frames.append(frame)
    update_frame_grid()
    return frame

def main_menu_frame():
    main_menu = create_frame()
    ctk.CTkLabel(main_menu, text="Main Menu", font=("NotoSans", size[0]/50), fg_color=f"#{colors[3]}", text_color=f"#{colors[1]}").grid(row=0, column=0, columnspan=2, pady=10)
    ctk.CTkButton(main_menu, width=50, height=50,  text="[]", font=("NotoSans", size[0]/75), fg_color=f"#{colors[3]}", hover_color=f"#{colors[2]}", text_color=f"#{colors[1]}", command=matrix_frame).grid(row=1, column=0, pady=10, padx=10)
    ctk.CTkButton(main_menu, width=50, height=50, text="🧮", font=("NotoSans", size[0]/75), fg_color=f"#{colors[3]}", hover_color=f"#{colors[2]}", text_color=f"#{colors[1]}", command=calculator_frame).grid(row=1, column=1, pady=10, padx=10)
    ctk.CTkButton(main_menu, width=50, height=50, text="\u222B", font=("NotoSans", size[0]/75), fg_color=f"#{colors[3]}", hover_color=f"#{colors[2]}", text_color=f"#{colors[1]}", command=integral_frame).grid(row=2, column=0, pady=10, padx=10)
    ctk.CTkButton(main_menu, width=50, height=50, text="\U0001F4C8", font=("NotoSans", size[0]/75), fg_color=f"#{colors[3]}", hover_color=f"#{colors[2]}", text_color=f"#{colors[1]}", command=graph_frame).grid(row=2, column=1, pady=10, padx=10)

def matrix_frame():
    frame = create_frame()

def calculator_frame():
    frame = create_frame()

def integral_frame():
    frame = create_frame()

def graph_frame():
    frame = create_frame()

def update_frame_grid():
    total_frames = len(frames)
    if total_frames == 0:
        return  # No hay frames para actualizar

    # Configurar las columnas del grid para distribuir los frames uniformemente
    for index, frame in enumerate(frames):
        frame.grid_forget()  # Asegúrate de limpiar cualquier configuración previa
        frame.grid(row=1, column=index, sticky="nsew", padx=5, pady=5)  # Añade espacio entre frames si es necesario

    # Configurar pesos para las columnas, para que cada frame se ajuste automáticamente
    for col in range(total_frames):
        root.grid_columnconfigure(col, weight=1)

    # Configurar peso para la fila donde están los frames
    root.grid_rowconfigure(1, weight=1)
    update_topbar(total_frames)

def update_topbar(columns):
    """Actualiza el columnspan de la barra superior según el número de columnas."""
    topbar.grid_forget()  # Limpia la configuración previa del grid
    topbar.grid(row=0, column=0, columnspan=columns, sticky="ew")  # Reasigna con el nuevo columnspan
    for col in range(columns):
        root.grid_columnconfigure(col, weight=1)


get_time()

main_menu_frame()

root.mainloop()