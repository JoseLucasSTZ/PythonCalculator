# importações

from tkinter import *
from tkinter import ttk

# cores

cor1 = "#1e1f1e"  # preto
cor2 = "#feffff"  # branco
cor3 = "#38576b"  # azul
cor4 = "#ECEFF1"  # Cinza
cor5 = "#FFAB40"  # laranja

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")

# frames (os containers em formato retangular)
frame_tela = Frame(janela, width=235, height=50, bg=cor1)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268, bg=cor3)
frame_corpo.grid(row=1, column=0)

# botões

b_1 = Button(frame_corpo, text="C", width=11, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo, text="%", width=11, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=90, y=0)

b_3 = Button(frame_corpo, text="/", width=11, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

janela.mainloop()
