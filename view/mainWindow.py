import customtkinter as ctk

class CalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.geometry("400x600")
        self.expression = ""
        self.input_text = ctk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        input_frame = ctk.CTkFrame(self, width=400, height=50, border_width=1)
        input_frame.pack(side=ctk.TOP)
        input_field = ctk.CTkEntry(input_frame, textvariable=self.input_text, width=400, height=50, justify='right', font=('arial', 18, 'bold'))
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        btns_frame = ctk.CTkFrame(self, width=400, height=450)
        btns_frame.pack()

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in buttons:
            button = ctk.CTkButton(btns_frame, text=text, width=100, height=100, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception as e:
                self.expression = "Error"
        else:
            self.expression += str(char)
        self.input_text.set(self.expression)

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()