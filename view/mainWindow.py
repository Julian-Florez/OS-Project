import customtkinter as ctk

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Fullscreen Application")
        self.attributes("-fullscreen", True)

        self.left_frame = ctk.CTkFrame(self, width=200, height=400, fg_color="blue")
        self.left_frame.pack(side="left", fill="both", expand=True)

        self.right_frame = ctk.CTkFrame(self, width=200, height=400, fg_color="red")
        self.right_frame.pack(side="right", fill="both", expand=True)
        self.create_calculator(self.left_frame)

    def on_button_click(self, char):
        if char == '=':
            try:
                result = str(eval(self.display.get()))
                self.display.delete(0, 'end')
                self.display.insert('end', result)
            except Exception as e:
                self.display.delete(0, 'end')
                self.display.insert('end', 'Error')
        elif char == 'C':
            self.display.delete(0, 'end')
        else:
            self.display.insert('end', char)


    def create_calculator(self, parent):
        self.display = ctk.CTkEntry(parent, width=200, justify='right', font=("Arial", 18))
        self.display.grid(row=0, column=0, columnspan=4, pady=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            ctk.CTkButton(parent, text=button, command=action, width=50, height=50).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()