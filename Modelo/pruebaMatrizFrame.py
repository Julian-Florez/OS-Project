import customtkinter as ctk
from django.template.defaultfilters import title


def matrix():
    app = frameMatriz()
    app.mainloop()
class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Fullscreen Application")
        self.geometry("600x500")

        self.left_frame = ctk.CTkFrame(self, width=200, height=400, fg_color="green")


        self.right_frame = ctk.CTkFrame(self, width=200, height=400, fg_color="red")


        self.button_1 = ctk.CTkButton(self, text="open toplevel", command=self.open_toplevel,width=20, height=40,state="normal")
        self.button_1.pack(side="right", fill="both", expand=True)
        self.right_frame.pack(side="right", fill="both", expand=True)

        self.left_frame.pack(side="left", fill="both", expand=True)
        self.toplevel_window = None


    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = frameMatriz(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it





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
    #def matriz(self,parent):
        #self.newframe = ctk.CTkFrame(self, width=200, height=400, fg_color="green")
        #self.newframe.pack(side="left", fill="both", expand=True)


class frameMatriz(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # add widgets onto the frame, for example:
        self.focus()
        self.geometry("600x500")


        self.right_frame = ctk.CTkFrame(self, width=400, height=400, fg_color="yellow")
        self.right_frame.pack(side="right", fill="both", expand=True)


        self.matrices(self.right_frame)

    def matrices(self,p):
        self.entry1 = ctk.CTkLabel(p, text="matriz", width=100, justify='center', font=("Arial", 18))
        self.entry1.grid(row=0, column=0, columnspan=20, pady=50, padx=150)
        row_val = 1
        col_val = 0
        for a in range(9):
            # action = lambda x=button: self.on_button_click(x)
            ctk.CTkEntry(p, width=50, height=50).grid(row=row_val, column=col_val, padx=18, pady=5)
            col_val += 1
            if col_val > 2:
                col_val = 0
                row_val += 1

        row_val = 1
        col_val = 0
        for a in range(9):
 #action = lambda x=button: self.on_button_click(x)
             ctk.CTkEntry(p, width=50, height=50).grid(row=row_val+2, column=col_val+6, padx=18, pady=5)
             col_val += 1
             if col_val > 2:
                 col_val = 0
                 row_val += 1
        ctk.CTkButton(p,text="CTkButton").grid(row=4, column=5, padx=5, pady=5)
        row_val = 1
        col_val = 0
        for a in range(9):
            # action = lambda x=button: self.on_button_click(x)
            ctk.CTkEntry(p, width=50, height=50).grid(row=row_val+4, column=col_val, padx=18, pady=5)
            col_val += 1
            if col_val > 2:
                col_val = 0
                row_val += 1







if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()