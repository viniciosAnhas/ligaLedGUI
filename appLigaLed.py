from tkinter import *
import RPi.GPIO as gpio

led = 21
statusLed = False

def conf():
    
    gpio.setmode(gpio.BCM)
    gpio.setup(led, gpio.OUT)
    gpio.output(led, False)
    
janela = Tk()

janela.title("Liga Led")
janela.geometry("250x150+550+250")

def btn_click():
    
    global statusLed
    
    if statusLed == False:
        
        gpio.output(led, True)
        btn['text'] = "Desligar Led"
        lbl['text'] = "Led Ligado"
        statusLed = True
        
    else:
        
        gpio.output(led, False)
        btn['text'] = "Ligar Led"
        lbl['text'] = "Led Desligado"
        statusLed = False

btn = Button(janela, text = "Ligar Led", command = btn_click)
lbl = Label(janela, text = "Led Desligado")

btn.pack()
lbl.pack()

conf()
janela.mainloop()