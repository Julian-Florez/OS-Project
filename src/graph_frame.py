import customtkinter as ctk
from sympy import symbols, sympify
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def graph(inner_frame, colors):
    def plot_graph(formula):
        try:
            x = symbols('x')
            expr = sympify(formula)

            # Create a range of x values
            x_vals = np.linspace(-10, 10, 400)
            y_vals = [float(expr.subs(x, val).evalf()) if expr.subs(x, val).is_real else float('nan') for val in x_vals]
            # Plot using Matplotlib
            fig, ax = plt.subplots(figsize=(3, 2))
            fig.patch.set_facecolor(f"#{colors[3]}")  # Change outer frame background
            ax.tick_params(axis='x', colors=f"#{colors[1]}")
            ax.tick_params(axis='y', colors=f"#{colors[1]}")
            ax.set_facecolor(f"#{colors[3]}")  # Change plot area background
            ax.plot(x_vals, y_vals, label=formula, color=f"#{colors[1]}")
            ax.axhline(0, color=f"#{colors[0]}", linewidth=0.8, linestyle="--")
            ax.axvline(0, color=f"#{colors[0]}", linewidth=0.8, linestyle="--")
            ax.grid(color=f"#{colors[3]}", linestyle="--", linewidth=0.5)
            for spine in ax.spines.values():
                spine.set_edgecolor(f"#{colors[0]}")  # Set border color
                spine.set_linewidth(2)  # Set border thickness

            # Display in Tkinter
            canvas = FigureCanvasTkAgg(fig, master=inner_frame)
            canvas.draw()
            canvas.get_tk_widget().grid(row=2, column=0, columnspan=4, pady=5, ipadx=50, ipady=50)
            error_label.configure(text="")

        except Exception as e:
            error_label.configure(text="Invalid formula")


    entry = ctk.CTkEntry(inner_frame, width=300,fg_color=f"#{colors[0]}", text_color=f"#{colors[1]}", border_width=0, font=("GoogleSans", 15))
    entry.grid(row=1, column=0, columnspan=3, pady=10, padx=10)
    ctk.CTkButton(inner_frame, width=50, height=50, text="C", font=("CalcOs-Font", 20), command=lambda: plot_graph(entry.get()), fg_color=f"#{colors[2]}", hover_color=f"#{colors[4]}").grid(row=1, column=3, padx=10)
    error_label = ctk.CTkLabel(inner_frame, text="", text_color=f"#{colors[1]}", font=("GoogleSans", 15))
    error_label.grid(row=3, column=0, columnspan=4)
    plot_graph("y")
