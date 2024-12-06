import customtkinter as ctk




def integral(p, colors):
    wid = p.winfo_screenwidth() / 200 + 30
    hig = p.winfo_screenheight() / 200 + 30
    entry = ctk.CTkEntry(p, width=wid, height=hig)
    entry.grid(row=0, column=0, padx=5, pady=0)
    entry2 = ctk.CTkEntry(p, width=wid, height=hig)
    entry2.grid(row=3, column=0, padx=5, pady=0)
    image = ctk.CTkLabel(p,50,50,20,text="\u222B",font=("NotoSans", 100), fg_color=f"#{colors[3]}", text_color=f"#{colors[1]}")
    image.grid(row=2,column=0,padx=5,pady=10)
    inputt = ctk.CTkEntry(p,width=wid+100, height=hig)
    inputt.grid(row=2,column=1,padx=5,pady=10)
    image2 = ctk.CTkLabel(p, 50, 50, 20, text="=", font=("NotoSans", 50), fg_color=f"#{colors[3]}",
                         text_color=f"#{colors[1]}")
    image2.grid(row=2, column=2, padx=5, pady=10)
    output = ctk.CTkEntry(p, width=wid+50, height=hig)
    output.grid(row=2,column=3,padx=5,pady=10)
