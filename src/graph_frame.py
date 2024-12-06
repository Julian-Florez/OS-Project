import customtkinter as ctk
from sympy import symbols, sympify
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def graph(inner_frame, colors):
    def plot_graph():
        try:
            formula = entry.get()
            x = symbols('x')
            expr = sympify(formula)

            # Create a range of x values
            x_vals = np.linspace(-10, 10, 400)
            y_vals = [float(expr.subs(x, val).evalf()) if expr.subs(x, val).is_real else float('nan') for val in x_vals]
            # Plot using Matplotlib
            fig, ax = plt.subplots(figsize=(3, 2))
            fig.patch.set_facecolor(f"#{colors[3]}")  # Change outer frame background
            ax.set_facecolor(f"#{colors[3]}")  # Change plot area background
            ax.plot(x_vals, y_vals, label=formula, color=f"#{colors[0]}")
            ax.axhline(0, color="black", linewidth=0.8, linestyle="--")
            ax.axvline(0, color="black", linewidth=0.8, linestyle="--")
            ax.grid(color="gray", linestyle="--", linewidth=0.5)
            ax.legend()
            ax.set_xlabel("x")
            ax.set_ylabel("y")

            # Display in Tkinter
            canvas = FigureCanvasTkAgg(fig, master=inner_frame)
            canvas.draw()
            canvas.get_tk_widget().grid(row=2, column=0, columnspan=4, pady=5, ipadx=50, ipady=50)
            error_label.configure(text="")

        except Exception as e:
            error_label.configure(text="Invalid formula")


    entry = ctk.CTkEntry(inner_frame, width=200)
    entry.grid(row=1, column=0, columnspan=3, pady=10, padx=10)
    ctk.CTkButton(inner_frame, text="Graph", command=plot_graph, fg_color=f"#{colors[2]}", hover_color=f"#{colors[3]}").grid(row=1, column=3, padx=10)
    error_label = ctk.CTkLabel(inner_frame, text="", text_color="red")
    error_label.grid(row=3, column=0, columnspan=4)
