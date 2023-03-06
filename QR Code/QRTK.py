import qrcode
import tkinter as tk
from PIL import ImageTk, Image

class GeradorQRCode(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Projeto - Cássio Estevão")
        self.master.geometry("450x450")
        self.master.configure(bg="purple")
        self.master.resizable(False,False)
        self.texto_qrcode = tk.StringVar()
        self.criar_widgets()

    def criar_widgets(self):
        self.label = tk.Label(self.master,bg="purple",fg="white",text="Digite o texto que deseja codificar:", font= "Times 13")
        self.label.pack(padx=10)

        self.campo_texto = tk.Entry(self.master,width=80,bg="purple",fg="white",font="Times 15",textvariable=self.texto_qrcode)
        self.campo_texto.pack(padx=10, pady=10)

        self.imagem_qrcode = tk.Label(self.master,bg="purple")
        self.imagem_qrcode.pack()

        self.botao = tk.Button(self.master,bg="purple",fg="white",font="Times 12",text="Gerar QR Code", command=self.gerar_qrcode)
        self.botao.pack(padx=10, pady=10)

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
