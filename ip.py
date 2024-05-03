import tkinter as tk
import customtkinter
import pyautogui
import time 

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# criando janela principal
janela = customtkinter.CTk()
janela.geometry("149x300")
janela.title("logando")
janela.resizable(False, False)

# Frame
frame = customtkinter.CTkFrame(master = janela, width=140, height=295)
frame.place(x= 5, y= 5)

#criando variável
ip_var = tk.StringVar()

# criando funções 
def pegarip():
    pyautogui.press("win")
    time.sleep(1/2)
    pyautogui.write("cmd")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.write("ipconfig")
    pyautogui.press("enter")

def continuar():
    entrada_ip = ip_var.get()
    if entrada_ip == "":
        entrada_ip = "192.168.10.1"
    else:
        pass
    pyautogui.press("win")
    pyautogui.write("Chrome")
    time.sleep(1/2)
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.hotkey("ctrl", "t")
    pyautogui.write(entrada_ip)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.write("adminisp")
    pyautogui.press("tab")
    pyautogui.write("adminisp")
    pyautogui.press("enter")

def denovo():
    pyautogui.hotkey("alt", "tab")
    pyautogui.write("cls")
    pyautogui.press("enter")
    time.sleep(1/2)
    pyautogui.write("ipconfig")
    pyautogui.press("enter")

#Botões
botao1 = customtkinter.CTkButton(master=frame, text="Pegar IP".upper(), width=125, command=pegarip, fg_color="#115", hover_color="#113")
botao1.place(x= 7, y= 20)

botao2 = customtkinter.CTkButton(master=frame, text="logar".upper(), width=125, command=continuar, fg_color="#151",hover_color="#131")
botao2.place(x= 7, y= 60)

botao3 = customtkinter.CTkButton(master=frame, text="Pegar denovo".upper(), width=125, command= denovo, fg_color="#115", hover_color="#113")
botao3.place(x= 7, y= 250)

#Texto
texto = customtkinter.CTkLabel(master=frame, text="IP alternativo", font=(15, 15))
texto.place(x=25, y=110)

#Entrada
entrada1 = customtkinter.CTkEntry(master=frame, placeholder_text="Nome completo do comprador", textvariable=ip_var, font=(12, 12), width=125)
entrada1.place(x=7, y=135)

janela.mainloop()