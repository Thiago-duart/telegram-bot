from messages.send_message import bot
import base64
from tkinter import *

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry('350x350')
        self.title("Botfly Telegram")
        self.configure(background="#223240")

        self.handle = False

        button_font = ("Arial", 18)
        status_font = ("Arial", 16)

        frame = Frame(self, background="#223240")
        frame.pack(expand=True, fill=BOTH)

        button_start = Button(frame, text='Iniciar', command=self.start_bot, font=button_font, border=2,width=30)
        button_start.pack(pady=20)

        button_stop = Button(frame, text='Pausar', command=self.stop_bot, font=button_font, border=2,width=30)
        button_stop.pack(pady=20)

        self.status_label = Label(frame, text='Status: Pausado', font=status_font, fg='red', background="#223240")
        self.status_label.pack()

        self.iconbitmap('./icon.ico')

    def start_bot(self):
        self.handle = True
        self.bot_loop()  
        self.update_status_label()

    def bot_loop(self):
        if self.handle:
            with open('./tigrinho.jpg', 'rb') as f:
                encoded_img = base64.b64encode(f.read())
            bot(encoded_img)
            self.after(6000, self.bot_loop) 

    def stop_bot(self):
        self.handle = False
        self.update_status_label()

    def update_status_label(self):
        status_text = 'Status: Online' if self.handle else 'Status: Pausado'
        status_color = 'green' if self.handle else 'red'
        self.status_label.config(text=status_text, fg=status_color)

app = App()
app.mainloop()
