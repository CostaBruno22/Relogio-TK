from tkinter import *
import tkinter
from datetime import datetime
import pyglet
pyglet.font.add_file('D:\\Projetos-py\\PROJETO_RELOGIO\\digital-7.regular.ttf')


# CORES QUE VOU USAR----------------------------------------------------

cor0 = '#000000' # PRETO
cor1 = '#FF1493' # DEEPPINK
cor2 = '#DCDCDC' # GAINSBORO
cor3 = '#00FFFF' # AQUA
cor4 = '#FFFF00' # AMARELO
cor5 = '#836FFF' # SLADEBLUE1
cor_fundo = '#B0C4DE' # LIGTHSTELLBLUE

# CONFIGURAÇÃO DE TELA---------------------------------------------------

janela = Tk()
janela.title('RELOGIO DIGITAL')
janela.geometry('500x160')
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=cor_fundo)


# FUNÇÃO RELOGIO--------------------------------------------------------

def relogio():
    tempo = datetime.now()
    hora = tempo.strftime('%H:%M:%S')
    dia_semana = tempo.strftime('%A')
    dia = tempo.day
    mes = tempo.strftime('%B')
    ano = tempo.strftime('%Y')
    label_01.config(text=hora)
    label_01.after(200, relogio)
    label_02.config(text=dia_semana + '  ' + str(dia) + '/' + str(mes) + '/' + str(ano))
   

# LABELS COM OS DADOS APRESENTADOS NO RELOGIO-----------------------------

label_01 = Label(janela, text='', font=('digital-7.regular 80'), bg=cor_fundo, fg=cor0)
label_01.grid(row = 0, column = 0, sticky=NW, padx= 5)

label_02 = Label(janela, text='', font=('digital-7.regular 20'), bg=cor_fundo, fg=cor0)
label_02.grid(row = 1, column = 0, sticky=NW, padx= 5)



relogio()
janela.mainloop()
