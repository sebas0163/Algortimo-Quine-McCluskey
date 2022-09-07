from msilib.schema import Font
import tkinter
from tkinter import font
import time

class Algoritmo():

    def __init__(self):
        #Ventana Principal
        self.ventana = tkinter.Tk()
        self.ventana.geometry("700x500")
        self.ventana.title("Algoritmo Quine-McCluskey")
        self.ventana.resizable(False, False)
        self.ventana.configure()
        #Frame
        self.frame1 = tkinter.Frame(self.ventana,width=350,height=500, bg="dark sea green")
        self.frame2 = tkinter.Frame(self.ventana, width=350,height=500,bg="purple")
        self.frame1.place(relx=0,rely=0)
        self.frame2.place(relx=0.5,rely=0)

        #Etiquetas de la interfaz
        self.etiquetaAlgA = tkinter.Label(self.frame1, text="Algoritmo de Quine-McCluskey",font="Helvetica 16 bold", bg="dark sea green")
        self.etiquetaAlgA.place(relx=0.08, rely=0.01)
        self.etiquetaAlgB = tkinter.Label(self.frame2, text="Algoritmo de Expresso", font="Helvetica 16 bold", bg="purple")
        self.etiquetaAlgB.place(relx=0.0, rely=0.01)
        self.etiquetaVar = tkinter.Label(self.frame1, text="Seleccione la cantidad de variables", font= "Helvetica 12", bg="dark sea green" )
        self.etiquetaVar.place(relx=0.08, rely=0.1)
        self.etiquetaNum = tkinter.Label(self.frame1, text="Ingrese la secuencia deseada", font= "Helvetica 12", bg="dark sea green" )
        self.etiquetaNum.place(relx=0.08, rely=0.25)
        self.resultadoAlgo1=tkinter.Label(self.frame1, text="Resultado", font= "Helvetica 12", bg="dark sea green" )
        self.resultadoAlgo1.place(relx=0.08, rely=0.5)
        self.time=tkinter.Label(self.frame1,text="Tiempo de ejecución: ",font= "Helvetica 12", bg="dark sea green")
        self.time.place(relx=0.08,rely=0.7)
        self.tiempo =tkinter.Label(self.frame1,text="",font= "Helvetica 12", bg="dark sea green")
        self.tiempo.place(relx=0.08,rely=0.75)

        #Dropdowns
        self.options =[
            4,
            5,
            6,
        ]
        self.clicked=tkinter.StringVar()
        self.clicked.set("4")
        self.drop = tkinter.OptionMenu(self.frame1,self.clicked,*self.options)
        self.drop.place(relx=0.08, rely=0.16)
        self.drop.configure(width=10, height=1)

        #Timer

        #Entrada
        self.mcCluskInput = tkinter.Text(self.frame1, font="Helvetica 14")
        self.mcCluskInput.configure(width=15, height=1)
        self.mcCluskInput.place(relx=0.08,rely=0.3)

        #Botones
        self.botonAlgMcClu=tkinter.Button(self.frame1,text="Calcular",command=self.calcularResultado)
        self.botonAlgMcClu.configure(height=2, width=15)
        self.botonAlgMcClu.place(relx=0.08,rely=0.4)


    def calcularResultado(self):
        print(time.perf_counter())
        num = self.mcCluskInput.get("1.0",'end-1c').split(",")
        result="Resultado: "
        print(self.converTabla(int(self.clicked.get()), num))
        for nums in num:
            result += nums
        self.resultadoAlgo1.config(text=result)
        #print(time.perf_counter())
    
    def converTabla(self,numVar, minterminos):
        if numVar ==4:
            tabla = [[0,0,0,0,0],[0,0,0,1,0],[0,0,1,0,0],[0,0,1,1,0],
            [0,1,0,0,0],[0,1,0,1,0],[0,1,1,0,0],[0,1,1,1,0],
            [1,0,0,0,0],[1,0,0,1,0],[1,0,1,0,0],[1,0,1,1,0],
            [1,1,0,0,0],[1,1,0,1,0],[1,1,1,0,0],[1,1,1,1,0]]
            index =0
            for i in tabla:
                if str(index) in minterminos:
                    tabla[index][4] =1
                index += 1
            return tabla
        elif numVar ==5:
            tabla = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],
            [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],
            [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],
            [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
            cont =1
            index =0
            for i in tabla:
                if str(index) in minterminos:
                    tabla[index][5] =1
                index += 1
            return tabla
        else:
            tabla = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
            cont =1
            index =0
            for i in tabla:
                if str(index) in minterminos:
                    tabla[index][6] =1
                index += 1
            return tabla
            




algoritmo=Algoritmo()
algoritmo.ventana.mainloop()

