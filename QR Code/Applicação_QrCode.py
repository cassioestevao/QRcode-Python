import qrcode
import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk, Image

class GeradorQRCode(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Dev Cásssio Estevão | Gerador de QRCode")
        self.master.geometry("400x580")
        self.master.configure(bg="purple")
        self.master.iconbitmap('icon.ico')
        self.master.resizable(False,False)
        self.texto_qrcode = tk.StringVar()
        self.criar_widgets()

    def criar_widgets(self):
        self.label = ctk.CTkLabel(self.master,text="Digite o texto que deseja codificar :",bg_color='transparent',corner_radius=20,text_color='white',font=('Century Gothic',17))
        self.label.pack(padx=10,pady=10)

        self.campo_texto = ctk.CTkEntry(self.master,width=300, fg_color='white',text_color='purple',corner_radius=20,textvariable=self.texto_qrcode)
        self.campo_texto.pack(padx=10, pady=10)
        

        self.imagem_qrcode = ctk.CTkLabel(self.master,bg_color="purple",text='')
        self.imagem_qrcode.pack(pady=15)

        self.botao = ctk.CTkButton(self.master,
                                   bg_color= 'purple',
                                   hover_color='black',
                                   fg_color='white',
                                   text_color='purple', 
                                   command=self.gerar_qrcode,
                                   corner_radius=20
                                   )
        self.botao.pack(padx=10, pady=20)

    def gerar_qrcode(self):
      
        texto = self.texto_qrcode.get()
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(texto)
        qr.make(fit=True)
        img = qr.make_image(fill_color="purple", back_color="white")

        img = ImageTk.PhotoImage(img)
        self.imagem_qrcode.configure(image=img)
        self.imagem_qrcode.image = img

        
root = tk.Tk()
app = GeradorQRCode(master=root)
app.mainloop()