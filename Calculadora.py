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

#FUNCIONES -----------------------------------------------------
def boton_pulsado(num):
    cad = cadena.get()
    cadena.set(cad + num)

def boton_igual():
    cad = cuentas.get()
    try:

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
 
    except:
        resultado.set("¡ERROR!")

    finally:
        cadena.set("")

#FRAME ---------------------------------------------------------
fram = Frame(root, width=310, height=290, bg="#CDEAF2", bd=5)
fram.pack()

#LABELS --------------------------------------------------------
Label(fram, text="Author: GitHub.com/EzeSosa", font="Calibri", bg="#CDEAF2").place(x=105, y=260)

#ENTRY ----------------------------------------------------------
resultados = Entry(fram, width=18, font=("Calibri",24), state="disabled", justify="right", textvariable=resultado) #NEEDS TEXTVARIABLE
resultados.place(x=5, y=25)

cuentas = Entry(fram, width=30, justify="left", state="disabled", font=("Arial", 8), bg="white", relief="groove", textvariable=cadena)
cuentas.place(x=113, y=2) 

#BUTTONS --------------------------------------------------------
boton_1 = Button(fram, text=" 1 ", pady=10, padx=10, command=lambda:boton_pulsado("1"), bg="lightblue", cursor="hand2")
boton_1.place(x=8, y=80)

boton_2 = Button(fram, text=" 2 ", pady=10, padx=10, command=lambda:boton_pulsado("2"), bg="lightblue", cursor="hand2")
boton_2.place(x=68, y=80)

boton_3 = Button(fram, text=" 3 ", pady=10, padx=10, command=lambda:boton_pulsado("3"), bg="lightblue", cursor="hand2")
boton_3.place(x=128, y=80)

boton_4 = Button(fram, text=" 4 ", pady=10, padx=10, command=lambda:boton_pulsado("4"), bg="lightblue", cursor="hand2")
boton_4.place(x=188, y=80)

boton_5 = Button(fram, text=" 5 ", pady=10, padx=10, command=lambda:boton_pulsado("5"), bg="lightblue", cursor="hand2")
boton_5.place(x=8, y=140)

boton_6 = Button(fram, text=" 6 ", pady=10, padx=10, command=lambda:boton_pulsado("6"), bg="lightblue", cursor="hand2")
boton_6.place(x=68, y=140)

boton_7 = Button(fram, text=" 7 ", pady=10, padx=10, command=lambda:boton_pulsado("7"), bg="lightblue", cursor="hand2")
boton_7.place(x=128, y=140)

boton_8 = Button(fram, text=" 8 ", pady=10, padx=10, command=lambda:boton_pulsado("8"), bg="lightblue", cursor="hand2")
boton_8.place(x=188, y=140)

boton_9 = Button(fram, text=" 9 ", pady=10, padx=10, command=lambda:boton_pulsado("9"), bg="lightblue", cursor="hand2")
boton_9.place(x=8, y=200)

boton_0 = Button(fram, text=" 0 ", pady=10, padx=10, command=lambda:boton_pulsado("0"), bg="lightblue", cursor="hand2")
boton_0.place(x=68, y=200)

boton_suma = Button(fram, text=" + ", pady=10, padx=10, command=lambda:boton_pulsado("+"), bg="orange", cursor="hand2")
boton_suma.place(x=248, y=80)

boton_resta = Button(fram, text="  - ", pady=10, padx=10, command=lambda:boton_pulsado("-"), bg="orange", cursor="hand2")
boton_resta.place(x=248, y=140)

boton_multi = Button(fram, text=" x ", pady=10, padx=10, command=lambda:boton_pulsado("*"), bg="orange", cursor="hand2")
boton_multi.place(x=128, y=200)

boton_div = Button(fram, text=" / ", pady=10, padx=10, command=lambda:boton_pulsado("/"), bg="orange", cursor="hand2")
boton_div.place(x=188, y=200)

boton_igual = Button(fram, text=" = ", pady=10, padx=10, command=boton_igual, bg="red", cursor="hand2")
boton_igual.place(x=248, y=200)

root.mainloop()
