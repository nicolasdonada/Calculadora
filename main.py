from tkinter import *
import math

class Calculadora:
    def __init__(self):
        
        # Cores
        self.operacoes = "#323232"
        self.numeros = "#3b3b3b"
        self.igual = "#841a9b"
        self.fundo = "#282a36"
        self.cdisplay = '#202020'
        self.letras = "#FFF"

        #Gerando a tela do programa
        self.janela = Tk()
        self.janela.title("Calculadora")
        self.janela.geometry("300x486")
        self.janela.config(bg="gray")
        self.janela.resizable(width=False, height=False)

        self.all_values = ''
        self.text_value = StringVar()

        self.display = Frame(self.janela, width=300, height=90, bg=self.cdisplay)
        self.display.place(x=0, y=0)

        self.body = Frame(self.janela, width=420, height=425, bg=self.fundo)
        self.body.place(x=0, y=90)

        self.interface()
        self.janela.mainloop()

    def clear_screen(self):
        str(self.all_values)

        self.all_values = self.all_values[:0]
        self.text_value.set(self.all_values)

    def del_value(self):
        str(self.all_values)

        self.all_values = self.all_values[:-1]
        self.text_value.set(self.all_values)

    def enter_value(self, entry):
            self.all_values = str(self.all_values) + str(entry)  # Adiciona o número à expressão
            self.text_value.set(self.all_values)

    def interface(self):

        displayLabel = Label(self.display, textvariable=self.text_value, width=16, height=2, relief=FLAT,
                     anchor='e', justify=CENTER, font=('Ivy 23'), bg=self.cdisplay, fg=self.letras)
        displayLabel.place(x=0, y=0)

        button_C = Button(self.body, width=7, height=1, text="C", font="Arial 20", bg=self.numeros, fg=self.letras, 
                          relief=RAISED, overrelief=SUNKEN, command=lambda: self.clear_screen())
        button_C.place(x=0, y=0)

        button_7 = Button(self.body, width=3, height=1, text="7", font="Arial 25", bg=self.numeros, fg=self.letras, 
                          relief=RAISED, overrelief=SUNKEN ,command=lambda: self.enter_value("7"))
        button_7.place(x=0, y=57)

        button_8 = Button(self.body, width=3, height=1, text="8", font="Arial 25", bg=self.numeros, fg=self.letras, 
                          relief=RAISED, overrelief=SUNKEN ,command=lambda: self.enter_value("8"))
        button_8.place(x=68, y=57)

        button_9 = Button(self.body, width=3, height=1, text="9", font="Arial 25", bg=self.numeros, fg=self.letras, 
                          relief=RAISED, overrelief=SUNKEN ,command=lambda: self.enter_value("9"))
        button_9.place(x=136, y=57)

        button_6 = Button(self.body, width=3, height=1, text="6", font="Arial 25", bg=self.numeros, fg=self.letras, 
                          relief=RAISED, overrelief=SUNKEN ,command=lambda: self.enter_value("6"))
        button_6.place(x=136, y=125)

        button_5 = Button(self.body, width=3, height=1, text="5", font="Arial 25", bg=self.numeros, fg=self.letras, 
                          relief=RAISED, overrelief=SUNKEN ,command=lambda: self.enter_value("5"))
        button_5.place(x=68, y=125)

        button_4 = Button(self.body, width=3, height=1, text="4", font="Arial 25", bg=self.numeros, fg=self.letras, 
                          relief=RAISED, overrelief=SUNKEN ,command=lambda: self.enter_value("4"))
        button_4.place(x=0, y=125)

        button_1 = Button(self.body, width=3, height=1, text="1", font="Arial 25", bg=self.numeros, fg=self.letras, 
                          relief=RAISED, overrelief=SUNKEN ,command=lambda: self.enter_value("1"))
        button_1.place(x=0, y=193)

        button_2 = Button(self.body, width=3, height=1, text="2", font="Arial 25", bg=self.numeros, fg=self.letras, 
                          relief=RAISED, overrelief=SUNKEN ,command=lambda: self.enter_value("2"))
        button_2.place(x=68, y=193)

        button_3 = Button(self.body, width=3, height=1, text="3", font="Arial 25", bg=self.numeros, fg=self.letras, 
                          relief=RAISED, overrelief=SUNKEN ,command=lambda: self.enter_value("3"))
        button_3.place(x=136, y=193)
    
        button_0 = Button(self.body, width=3, height=1, text="0", font="Arial 25", bg=self.numeros, fg=self.letras, 
                          relief=RAISED, overrelief=SUNKEN ,command=lambda: self.enter_value("0"))
        button_0 .place(x=68, y=261)

        button_paren = Button(self.body, width=3, height=1, text="(", font="Arial 25", bg=self.numeros, fg=self.letras, 
                          relief=RAISED, overrelief=SUNKEN ,command=lambda: self.enter_value("("))
        button_paren.place(x=0, y=261)

        button_paren1 = Button(self.body, width=3, height=1, text=")", font="Arial 25", bg=self.numeros, fg=self.letras, 
                          relief=RAISED, overrelief=SUNKEN ,command=lambda: self.enter_value(")"))
        button_paren1.place(x=136, y=261)

        button_del = Button(self.body, width=3, height=1, text="Del", font="Arial 25", bg=self.numeros, fg=self.letras, 
                          relief=RAISED, overrelief=SUNKEN, command=lambda: self.del_value())
        button_del.place(x=0, y=329)

        button_sqrt = Button(self.body, width=4, height=1, text="√", font="Arial 21", bg=self.numeros, fg=self.letras,
                          relief=RAISED, overrelief=SUNKEN, command=lambda: self.enter_value("√"))
        button_sqrt.place(x=123, y=0)

        button_expo = Button(self.body, width=6, height=1, text="^", font="Arial 20", bg=self.numeros, fg=self.letras,
                          relief=RAISED, overrelief=SUNKEN, command=lambda: self.enter_value("^"))
        button_expo.place(x=199, y=0)

        button_division = Button(self.body, width=5, height=1, text="÷", font="Arial 25", bg=self.numeros, fg=self.letras,
                          relief=RAISED, overrelief=SUNKEN, command=lambda: self.enter_value("÷"))
        button_division.place(x=205, y=57)

        button_multi = Button(self.body, width=5, height=1, text="×", font="Arial 25", bg=self.numeros, fg=self.letras,
                          relief=RAISED, overrelief=SUNKEN, command=lambda: self.enter_value("×"))
        button_multi.place(x=205, y=125)

        button_sum = Button(self.body, width=5, height=1, text="+", font="Arial 25", bg=self.numeros, fg=self.letras,
                          relief=RAISED, overrelief=SUNKEN, command=lambda: self.enter_value("+"))
        button_sum.place(x=205, y=193)

        button_sub = Button(self.body, width=5, height=1, text="-", font="Arial 25", bg=self.numeros, fg=self.letras,  
                          relief=RAISED, overrelief=SUNKEN, command=lambda: self.enter_value("-"))
        button_sub.place(x=205, y=261)

        button_equals = Button(self.body, width=5, height=1, text="=", font="Arial 25", bg=self.numeros, fg=self.letras,
                          relief=RAISED, overrelief=SUNKEN, command=lambda: self.calcular())
        button_equals.place(x=205, y=329)

        button_point = Button(self.body, width=3, height=1, text=".", font="Arial 25", bg=self.numeros, fg=self.letras,
                          relief=RAISED, overrelief=SUNKEN, command=lambda: self.enter_value("."))
        button_point.place(x=136, y=329)

        button_porc = Button(self.body, width=3, height=1, text="%", font="Arial 25", bg=self.numeros, fg=self.letras,
                           relief=RAISED, overrelief=SUNKEN, command=lambda: self.enter_value("%"))
        button_porc.place(x=68, y=329)

        



    def calcular(self):

        try:
            if "×" in self.all_values:
                self.all_values = self.all_values.replace("×", "*")

            if "÷" in self.all_values:
                self.all_values = self.all_values.replace("÷", "/")

            if "√" in self.all_values:
                self.all_values = self.all_values.replace("√", "")

                number = int(self.all_values)

                resultado = math.sqrt(number)
                self.text_value.set(resultado)
                self.all_values = str(resultado)

            if "^" in self.all_values:
                self.all_values = self.all_values.replace("^", "**")

            else:
                result = eval(self.all_values)
                self.text_value.set(result)
                self.all_values = str(result)

        except Exception as e:
            self.text_value.set("Error")
            self.all_values = ""

cal = Calculadora()