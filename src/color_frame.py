import customtkinter as ctk
import os

prdir = os.path.dirname(os.path.dirname(__file__))

def color(inner_frame, colors):
    def save_colors():
        new_colors = [entry.get() for entry in entries]
        with open(f'{prdir}/assets/colors.txt', 'w') as f:
            f.write('\n'.join(new_colors))
        for i in range(len(colors)):
            colors[i] = new_colors[i]

    entries = []
    for i in range(5):
        label = ctk.CTkLabel(inner_frame, text=f"Color {i+1}", font=("Google Sans", 20), text_color=f"#{colors[1]}")
        label.grid(row=i, column=0, pady=5, padx=5)
        entry = ctk.CTkEntry(inner_frame, width=200, border_width=0, fg_color=f"#{colors[0]}", text_color=f"#{colors[1]}", font=("Google Sans", 20))
        entry.grid(row=i, column=1, pady=5, padx=5)
        entries.append(entry)

    save_button = ctk.CTkButton(inner_frame, text="Save Colors", command=save_colors, fg_color=f"#{colors[2]}", hover_color=f"#{colors[3]}", text_color=f"#{colors[1]}", font=("Google Sans", 20))
    save_button.grid(row=5, column=0, pady=10, padx=10, columnspan=2)