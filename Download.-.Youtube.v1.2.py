import pytube
from pytube import YouTube
import tkinter as tk
from tkinter import *
from tkinter import messagebox

#Função que executa alguma coisa
def funcao_botao():
    n1 = str(caixa_1.get())
    youtube = pytube.YouTube(n1)
    video = youtube.streams.first()
    video.download('C:\\Users\\pqcir\\Downloads\\video')
    messagebox.showinfo('Download realizado!', 'Seu video já está na pasta selecionada ')

#Iniciando uma janela
janela = Tk()

#Colocando um texto dentro da janela
label_1 = Label(janela, text='Cole a URL para realizar o download', font = 'Arial 9')
label_1.place(x=10,y=5)

#Criando um botão de função
botao_1 = Button(janela, width = 25, text ='Download!', command =funcao_botao, background = 'white')
botao_1.place(x=20,y=50)

#Criando uma caixa de entrada de dados
caixa_1 = Entry(janela, background='white', width = 30, font='Arial 8')
caixa_1.place(x=20, y=30)

#Criando uma janela 800x600
janela.geometry('250x100+0+0')

#Criando um loop para manter a janela aberta
janela.title("Pytube v1.2")
janela.mainloop()
