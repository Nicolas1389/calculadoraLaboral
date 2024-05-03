import tkinter
from tkinter import*

raiz=Tk()
framePrueba=Frame(raiz)
framePrueba.pack()
#-------------------------recuadro inicial -------------------------------
raiz.title("calculadora laboral")
raiz.config(bg="grey")
raiz.config(cursor="hand2")



#-------------------Nombre label y cuadro para ingresar Nombre-------------------------
nombreLabel=Label(framePrueba, text="Nombre")
nombreLabel.grid(row=0, column=0)
nombreLabel.config(justify="right")

cuadroTextoNombre= Entry(framePrueba)
cuadroTextoNombre.grid(row=0,column=1)

#----------variables--------------------

numeroPantalla=StringVar()
numeroPantalla2=StringVar()
numeroPantalla3=StringVar()
numeroPantalla4=StringVar()
numeroPantallaMes=StringVar()
numeroPantallaDia=StringVar()
pantallaTotalPagar=StringVar()
salarioDIario=int
aportePensionEmpleado=int
totalDia=int
dia=int
mes=int
pantallaFondoSolidario=StringVar()
numeroPantaAñoRetiro=StringVar()
numeroPantallaTotalDia=StringVar()
diaIngreso=StringVar()
mesIngreso=StringVar()
añoIngreso=StringVar()
tipoDoc=StringVar()

#-------------------funciones--------------------------------------

def pulsarBoton(num):
    global salarioDIario
    global numeroPantalla2
    global numeroPantalla3
    global numeroPantalla4
    global aportePensionEmpleado
    global numeroPantalla
    global fondoSolidario
    global pantalla
    global pantallaTotalPagar
    global totalPagar

    #numeroPantalla.set(numeroPantalla.get())

    try:
        salarioDIario= int(num)//30
        aportePensionEmpleado=int(num)*0.04
        aporteSaludEmpleado=int(num)*0.04

        if int(num) >= 5400000:
            fondoSolidario = int(num) * 0.01
            pantallaFondoSolidario.set(f"{fondoSolidario:,}")
        else:
            fondoSolidario=int(0)
            pantallaFondoSolidario.set(f"")

        totalPagar=int(num)-int(aporteSaludEmpleado)-int(aportePensionEmpleado)-int(fondoSolidario)

        numeroPantalla2.set(f"{salarioDIario:,}")
        numeroPantalla3.set(f"{aportePensionEmpleado:,}")
        numeroPantalla4.set(f"{aporteSaludEmpleado:,}")
        pantallaTotalPagar.set(f"{totalPagar:,}")

    except ValueError:
        if num =="":
            numeroPantalla.set("no ha introducido ninguna cifra")
        else:
            numeroPantalla.set("error")
    finally:
        cuadroTexto.config(state="disable")
        cuadroTextoApellido.config(state="disable")
        cuadroTextoNombre.config(state="disable")
        cuadroTextoDocumento.config(state="disable")



def borrar():
    global numeroPantalla2
    global numeroPantalla3
    global numeroPantalla4
    global numeroPantalla

    numeroPantalla2.set(f"")
    numeroPantalla3.set(f"")
    numeroPantalla4.set(f"")
    numeroPantalla.set(f"")
    pantallaFondoSolidario.set(f"")
    pantallaTotalPagar.set(f"")
    numeroPantallaDia.set(f"")
    numeroPantallaMes.set(f"")
    numeroPantaAñoRetiro.set(f"")
    diaIngreso.set(f"")
    mesIngreso.set(f"")
    añoIngreso.set(f"")
    numeroPantallaTotalDia.set(f"")

    cuadroTexto.config(state="normal")
    cuadroTextoApellido.config(state="normal")
    cuadroTextoNombre.config(state="normal")
    cuadroTextoDocumento.config(state="normal")

def calcularTiempo(dia2,mes2,año2,dia1,mes1,año1):

    global totalDias
    global mesDia

    totalDias= (int(mes2)-int(mes1))*12 +(int(dia2)-int(dia1))+(int(año2)-int(año1))*360

    numeroPantallaTotalDia.set(f"{totalDias:,}")


#------------------apellido label y cuadro para ingresarolo---------------------------

apellidoLabel=Label(framePrueba, text="apellido")
apellidoLabel.grid(row=1, column=0)

cuadroTextoApellido= Entry(framePrueba)
cuadroTextoApellido.grid(row=1,column=1)

#-------------------seleccionar tipo de texto-------------------------------
tipoDocumentoLabel=Label(framePrueba, text="tipo de documento")
tipoDocumentoLabel.grid(row=2, column=0)

tipoDocumento=tkinter.OptionMenu(framePrueba, tipoDoc,"CC","CE","pasaporte", "diplomatica")
tipoDocumento.grid(row=2,column=1)

#----------------Numero de documento label y recuadro------------------------

ingreseDocumentoNoLabel=Label(framePrueba, text="ingrese número de documento")
ingreseDocumentoNoLabel.grid(row=3, column=0)

cuadroTextoDocumento= Entry(framePrueba)
cuadroTextoDocumento.grid(row=3,column=1)

#----------------salario label y recuadro------------------------

ingreseSalarioLabel=Label(framePrueba, text="ingrese salario")
ingreseSalarioLabel.grid(row=0, column=2)

cuadroTexto= Entry(framePrueba, textvariable=numeroPantalla, state="normal")
cuadroTexto.grid(row=0,column=3)
#-------------- recuadro para iniciar calculos----------------------------------

botonEmpezarCalculos=Button(framePrueba, text="boton salarios", command=lambda:pulsarBoton(numeroPantalla.get()))
botonEmpezarCalculos.grid(row=0,column=4)

BotonBorrar=Button(framePrueba, text="borrar", command=lambda:borrar())
BotonBorrar.grid(row=0, column=5)

BotonCalcularTiempo=Button(framePrueba,text="calcular días trabajados", command=lambda:calcularTiempo(dia.get(),mesRetiro.get(),añoRetiro.get(),diaIngre.get(),mesIngre.get(),añoIngre.get()))
BotonCalcularTiempo.grid(row=3, column=5)


#-------------------recuadros para imprimir resultados------------------------------

#---------------salario diario--------------------------------------
resultadoSalarioDiario=Label(framePrueba, text="salario diario")
resultadoSalarioDiario.grid(row=1,column=2)

resultadoSalarioDiario=Entry(framePrueba, textvariable=numeroPantalla2, state="disable")
resultadoSalarioDiario.grid(row=1,column=3)

#------------------aporte a salud y pensión------------------------

aportePensionEmpleado=Label(framePrueba, text="aporte del emplado a pensión")
aportePensionEmpleado.grid(row=2,column=2)

aportePensionEmpleado=Entry(framePrueba, textvariable=numeroPantalla3, state="disable")
aportePensionEmpleado.grid(row=2,column=3)

aporteSaludEmpleado=Label(framePrueba, text="aporte del emplado a salud")
aporteSaludEmpleado.grid(row=3,column=2)

aporteSaludEmpleado=Entry(framePrueba, textvariable=numeroPantalla4, state="disable")
aporteSaludEmpleado.grid(row=3,column=3)

#------------------------------calcular cesantías causadas en el año-----------------------
#------------------------dia retiro---------------------------------------------------
dia=Label(framePrueba, text="dia de retiro del empleado")
dia.grid(row=4,column=2)

dia=Entry(framePrueba, textvariable=numeroPantallaDia)
dia.grid(row=4,column=3)
#---------------------------mes retiro------------------------------------------------------
mesRetiro=Label(framePrueba, text="mes de retiro del empleado")
mesRetiro.grid(row=5,column=2)

mesRetiro=Entry(framePrueba, textvariable=numeroPantallaMes)
mesRetiro.grid(row=5,column=3)
#-----------------------------------año retiro-----------------------------------------------

añoRetiro=Label(framePrueba, text="año de retiro del empleado")
añoRetiro.grid(row=6,column=2)

añoRetiro=Entry(framePrueba, textvariable=numeroPantaAñoRetiro)
añoRetiro.grid(row=6,column=3)


#------------------------------Fechas de ingreso----------------------------------------------

#------------------------dia ingreso---------------------------------------------------
diaIngre=Label(framePrueba, text="dia de ingreso del empleado")
diaIngre.grid(row=4,column=4)

diaIngre=Entry(framePrueba, textvariable=diaIngreso)
diaIngre.grid(row=4,column=5)
#---------------------------mes ingreso------------------------------------------------------
mesIngre=Label(framePrueba, text="mes de ingreso del empleado")
mesIngre.grid(row=5,column=4)

mesIngre=Entry(framePrueba, textvariable=mesIngreso)
mesIngre.grid(row=5,column=5)
#-----------------------------------año ingreso-----------------------------------------------
añoIngre=Label(framePrueba, text="año de ingreso del empleado")
añoIngre.grid(row=6,column=4)

añoIngre=Entry(framePrueba, textvariable=añoIngreso)
añoIngre.grid(row=6,column=5)



#-----------------------------total días trabajados-----------------------------------------

totalDia=Label(framePrueba, text="dias totales")
totalDia.grid(row=7,column=2)

totalDia=Entry(framePrueba, textvariable=numeroPantallaTotalDia, state="disable")
totalDia.grid(row=7,column=3)

#--------------------------------fondo solidario--------------------------
fondoSolidario=Label(framePrueba, text="fondo solidario")
fondoSolidario.grid(row=6,column=7)

fondoSolidario=Entry(framePrueba, textvariable=pantallaFondoSolidario, state="disable")
fondoSolidario.grid(row=6,column=8)

#---------------------------total recibido-----------------------------------------

totalPagar=Label(framePrueba, text="total a pagar")
totalPagar.grid(row=7,  column=7)

totalPagar=Entry(framePrueba, textvariable=pantallaTotalPagar, state="disable")
totalPagar.grid(row=7,column=8)

#--------------------main loop, necesario para que corra graficamente-----------------
raiz.mainloop()