#IMPORTO LAS FUNCIONES NECESARIAS
from tkinter import *

#RAÍZ ----------------------------------------------------------
root = Tk()
root.iconbitmap("E:\CursoPythonPI\CALCULADORA\calcu.ico")
root.title("Calculadora")
root.resizable(0, 0)

#VARIABLES -----------------------------------------------------
cadena = StringVar()
resultado = StringVar()
operacion = ""

#FUNCIONES -----------------------------------------------------
def clear_screen():
    global operacion
    operacion = ""

def boton_pulsado(num):
    if operacion!="":
        resultado.set("")
        clear_screen()

    cadena.set("")
    cad = resultado.get()
    resultado.set(cad + num)

def boton_igual():
    global operacion
    operacion = "done"
    cad = resultado.get()
    try:
        #MÉTODO COMÚN PARA TODAS LAS OPERACIONES, SÓLO SE CAMBIA EL SIGNO
        if cad.find("+") != 0 and cad.find("-") <= 0 and cad.find("*") <= 0 and cad.find("/") <= 0:
            txt = ""
            txt2 = ""
            num = cad.find("+")

            for i in range(num):
                txt = f"{txt}{cad[i]}"

            for x in range(num+1, len(cad)):
                txt2 = f"{txt2}{cad[x]}"

            arr = [txt, txt2]
            arr = list(map(lambda x: int(x), arr))
            result = arr[0] + arr[1]
            resultado.set(result)

        elif cad.find("+") <= 0 and cad.find("-") != 0 and cad.find("*") <= 0 and cad.find("/") <= 0:
            txt = ""
            txt2 = ""
            num = cad.find("-")

            for i in range(num):
                txt = f"{txt}{cad[i]}"

            for x in range(num+1, len(cad)):
                txt2 = f"{txt2}{cad[x]}"

            arr = [txt, txt2]
            arr = list(map(lambda x: int(x), arr))
            result = arr[0] - arr[1]
            resultado.set(result)

        elif cad.find("+") <= 0 and cad.find("-") <= 0 and cad.find("*") != 0 and cad.find("/") <= 0:
            txt = ""
            txt2 = ""
            num = cad.find("*")

            for i in range(num):
                txt = f"{txt}{cad[i]}"

            for x in range(num+1, len(cad)):
                txt2 = f"{txt2}{cad[x]}"

            arr = [txt, txt2]
            arr = list(map(lambda x: int(x), arr))
            result = arr[0] * arr[1]
            resultado.set(result)

        elif cad.find("+") <= 0 and cad.find("-") <= 0 and cad.find("*") <= 0 and cad.find("/") != 0:
            txt = ""
            txt2 = ""
            num = cad.find("/")

            for i in range(num):
                txt = f"{txt}{cad[i]}"

            for x in range(num+1, len(cad)):
                txt2 = f"{txt2}{cad[x]}"

            arr = [txt, txt2]
            arr = list(map(lambda x: int(x), arr))
            result = round(arr[0] / arr[1], 2)
            resultado.set(result)

        else:
            resultado.set("¡ERROR!")
 
    except ZeroDivisionError:
        resultado.set("INDEFINIDO")

    except:
        resultado.set("¡ERROR!")

    finally:
        cadena.set(cad+"=")
        
#FRAME ---------------------------------------------------------
fram = Frame(root, width=385, height=330, bg="#CDEAF2", bd=5)
fram.pack()

#LABELS --------------------------------------------------------
Label(fram, text="Author: GitHub.com/EzeSosa", font="Calibri", bg="#CDEAF2").place(x=173, y=295)

#ENTRY ----------------------------------------------------------
resultados = Entry(fram, width=20, font=("Calibri",26), state="disabled", justify="right", textvariable=resultado) #NEEDS TEXTVARIABLE
resultados.place(x=5, y=28)

cuentas = Entry(fram, width=28, justify="right", state="disabled", font=("Arial", 12), bg="white", relief="groove", textvariable=cadena, fg="black")
cuentas.place(x=113, y=1) 

#BUTTONS --------------------------------------------------------
boton_1 = Button(fram, text=" 1 ", pady=10, padx=10, command=lambda:boton_pulsado("1"), bg="lightblue", cursor="hand2", font=("Calculator", 20), width=4)
boton_1.place(x=11, y=80)

boton_2 = Button(fram, text=" 2 ", pady=10, padx=10, command=lambda:boton_pulsado("2"), bg="lightblue", cursor="hand2", font=("Calculator", 20), width=4)
boton_2.place(x=81, y=80)

boton_3 = Button(fram, text=" 3 ", pady=10, padx=10, command=lambda:boton_pulsado("3"), bg="lightblue", cursor="hand2", font=("Calculator", 20), width=4)
boton_3.place(x=151, y=80)

boton_4 = Button(fram, text=" 4 ", pady=10, padx=10, command=lambda:boton_pulsado("4"), bg="lightblue", cursor="hand2", font=("Calculator", 20), width=4)
boton_4.place(x=221, y=80)

boton_5 = Button(fram, text=" 5 ", pady=10, padx=10, command=lambda:boton_pulsado("5"), bg="lightblue", cursor="hand2", font=("Calculator", 20), width=4)
boton_5.place(x=11, y=150)

boton_6 = Button(fram, text=" 6 ", pady=10, padx=10, command=lambda:boton_pulsado("6"), bg="lightblue", cursor="hand2", font=("Calculator", 20), width=4)
boton_6.place(x=81, y=150)

boton_7 = Button(fram, text=" 7 ", pady=10, padx=10, command=lambda:boton_pulsado("7"), bg="lightblue", cursor="hand2", font=("Calculator", 20), width=4)
boton_7.place(x=151, y=150)

boton_8 = Button(fram, text=" 8 ", pady=10, padx=10, command=lambda:boton_pulsado("8"), bg="lightblue", cursor="hand2", font=("Calculator", 20), width=4)
boton_8.place(x=221, y=150)

boton_9 = Button(fram, text=" 9 ", pady=10, padx=10, command=lambda:boton_pulsado("9"), bg="lightblue", cursor="hand2", font=("Calculator", 20), width=4)
boton_9.place(x=11, y=220)

boton_0 = Button(fram, text=" 0 ", pady=10, padx=10, command=lambda:boton_pulsado("0"), bg="lightblue", cursor="hand2", font=("Calculator", 20), width=4)
boton_0.place(x=81, y=220)

boton_suma = Button(fram, text=" + ", pady=10, padx=10, command=lambda:boton_pulsado("+"), bg="orange", cursor="hand2", font=("Calculator", 20), width=4)
boton_suma.place(x=291, y=80)

boton_resta = Button(fram, text=" -- ", pady=10, padx=10, command=lambda:boton_pulsado("-"), bg="orange", cursor="hand2", font=("Calculator", 20), width=4)
boton_resta.place(x=291, y=150)

boton_multi = Button(fram, text=" x ", pady=10, padx=10, command=lambda:boton_pulsado("*"), bg="orange", cursor="hand2", font=("Calculator", 20), width=4)
boton_multi.place(x=151, y=220)

boton_div = Button(fram, text=" / ", pady=10, padx=10, command=lambda:boton_pulsado("/"), bg="orange", cursor="hand2", font=("Calculator", 20), width=4)
boton_div.place(x=221, y=220)

boton_igual = Button(fram, text=" = ", pady=10, padx=10, command=boton_igual, bg="red", cursor="hand2", font=("Calculator", 20), width=4)
boton_igual.place(x=291, y=220)

root.mainloop()
