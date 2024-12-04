import customtkinter as ctk
from django.template.defaultfilters import title


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Fullscreen Application")
        self.geometry("600x500")

        self.left_frame = ctk.CTkFrame(self, width=200, height=400, fg_color="green")
        self.left_frame.pack(side="left", fill="both", expand=True)

        self.right_frame = ctk.CTkFrame(self, width=200, height=400, fg_color="red")
        self.right_frame.pack(side="right", fill="both", expand=True)


        self.matriz(self.right_frame)
        self.matriz(self.left_frame)

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






    def matriz(self, parent):

        self.entry = ctk.CTkLabel(parent,text= "matriz",width=200, justify='center', font=("Arial", 18))
        self.entry.grid(row=0, column=0, columnspan=4, pady=10, padx=50)
        row_val = 1
        col_val = 0
        for button in range(9):
            # action = lambda x=button: self.on_button_click(x)
            ctk.CTkEntry(parent, width=50,height=50).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 2:
                col_val = 0
                row_val += 1

        


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()