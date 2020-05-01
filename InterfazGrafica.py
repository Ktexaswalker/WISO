from tkinter import *
from tkinter import messagebox
import sqlite3

#Funciones
def conexion_DB():
	conexion_DB = sqlite3.connect("Examen")
	guia = conexion_DB.cursor()
	try:
		guia.execute('''
			CREATE TABLE EXAMEN (
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			PREGUNTA VARCHAR(500),
			R1 VARCHAR(200),
			R2 VARCHAR(200),
			R3 VARCHAR(200),
			R4 VARCHAR(200),
			R5 VARCHAR(200),
			RESPUESTA INTEGER (10))
			''')
		messagebox.showinfo("DB","Base de datos creada")
	except:
		messagebox.showwarning("!","La base de datos ya existe")
def salir():
	condicional = messagebox.askquestion("Cerrar", "¿Desea salir del test?")
	if condicional == "yes":
		root.destroy()
def traduccion():
	pass
def no_traducir():
	pass
def nuevo():
	pass
def crear():
	pass
def leer():
	pass
def actualizar():
	pass
def borrar():
	pass
def ayuda():
	pass
def licencia():
	pass
def acerca_de():
	pass


def r():
	pass

#+++Interfaz grafica
root = Tk()
root.title("WISO")
ancho = root.winfo_screenwidth()
alto = root.winfo_screenheight()
root.geometry("%sx%d+0+0" % (ancho, alto))
#-++Barra menú (FRAME)
Barra_menu = Menu(root)
root.config(menu=Barra_menu, width=ancho, height=alto)
#Base de datos-> Conectar/Salir
DB_menu = Menu(Barra_menu, tearoff=0)
DB_menu.add_command(label="Conectar", command=conexion_DB)
DB_menu.add_separator()
DB_menu.add_command(label="Salir", command=salir)
#Ver -> Ver Traduccion / Ocultar Traduccion
Ver = Menu(Barra_menu, tearoff=0)
Ver.add_command(label="Ver Traducción", command=traduccion)
Ver.add_separator()
Ver.add_command(label="Ocultar traducción", command=no_traducir)

#Archivo -> Nuevo
Archivo = Menu(Barra_menu, tearoff=0)
Archivo.add_command(label="Archivo", command=nuevo)
#Edicion -> Crear/Leer/Actualizar/Borrar
Edicion = Menu(Barra_menu, tearoff=0)
Edicion.add_command(label="Crear", command=crear)
Edicion.add_command(label="Leer", command=leer)
Edicion.add_command(label="Actualizar", command=actualizar)
Edicion.add_command(label="Borrar", command=borrar)
#Información -> Ayuda/Licencia/Acerca de...
Informacion = Menu(Barra_menu, tearoff=0)
Informacion.add_command(label="Ayuda", command=ayuda)
Informacion.add_command(label="Licencia", command=licencia)
Informacion.add_separator()
Informacion.add_command(label="Acerca de...", command=acerca_de)
#Base de Datos / Ver / Archivo / Edicion / Información
Barra_menu.add_cascade(label="Base de Datos", menu=DB_menu)
Barra_menu.add_cascade(label="Archivo", menu=Archivo)
Barra_menu.add_cascade(label="Edicion", menu=Edicion)
Barra_menu.add_cascade(label="Ver", menu=Ver)
Barra_menu.add_cascade(label="Información", menu=Informacion)

#declaración de variables de almacenamiento
P_id = StringVar()
Pregunta = StringVar()
R1 = StringVar()
R2 = StringVar()
R3 = StringVar()
R4 = StringVar()
R5 = StringVar()
Respuesta = StringVar()
Pregunta_tradu = StringVar()
R1_tradu = StringVar()
R2_tradu = StringVar()
R3_tradu = StringVar()
R4_tradu = StringVar()
R5_tradu = StringVar()
Respuesta_tradu = StringVar()
Time_exam_min = StringVar()
limite_num_preguntas = StringVar()
select = IntVar()
puntuacion = IntVar()
aciertos = IntVar()
fallos = IntVar()
#-++Frame 1	Preguntas y respuestas / Temporizadores
Frame_1 = Frame(root)
Frame_1.pack(anchor=W)
Frame_1.config(width=ancho,height=alto/2)
linea1 = Canvas(Frame_1, width=ancho/2, height=60 ,bg="#F0F0F0")
linea1.grid(row=0, columnspan=10)
#--+Labels
E1_r1 = Text(Frame_1, width=50, height=4)
E1_r1.grid(row=1, column=3, padx=5)
E1_r2 = Text(Frame_1, width=50, height=4)
E1_r2.grid(row=2, column=3, padx=5)
E1_r3 = Text(Frame_1, width=50, height=4)
E1_r3.grid(row=3, column=3, padx=5)
E1_r4 = Text(Frame_1, width=50, height=4)
E1_r4.grid(row=4, column=3, padx=5)
E1_r5 = Text(Frame_1, width=50, height=4)
E1_r5.grid(row=5, column=3, padx=5)
#--+Campos
Txt_Pregunta = Text(Frame_1, width=90, height=20)
Txt_Pregunta.grid(row=1, rowspan=5, column=0, padx=20, pady=20)
scroll_Pregunta = Scrollbar(Frame_1, command=Txt_Pregunta.yview)
scroll_Pregunta.grid(row=1, rowspan=5, column=1, sticky="nsew")
Txt_Pregunta.config(yscrollcommand=scroll_Pregunta.set)
#--+Botones
btn_r1 = Button(Frame_1, text="1.", command=r)
btn_r1.grid(row=1, column=2, pady=10, sticky="nsew")
btn_r2 = Button(Frame_1, text="2.", command=r)
btn_r2.grid(row=2, column=2, pady=10, sticky="nsew")
btn_r3 = Button(Frame_1, text="3.", command=r)
btn_r3.grid(row=3, column=2, pady=10, sticky="nsew")
btn_r4 = Button(Frame_1, text="4.", command=r)
btn_r4.grid(row=4, column=2, pady=10, sticky="nsew")
btn_r5 = Button(Frame_1, text="5.", command=r)
btn_r5.grid(row=5, column=2, pady=10, sticky="nsew")
#separacion
linea1 = Canvas(Frame_1, width=(ancho/10), height=30 ,bg="#F0F0F0")
linea1.grid(row=0, column=4)
#Temportizadores
L_cuentatras = Label(Frame_1, text="Cuenta atras", font=("Arial" ,18), anchor="w")
L_cuentatras.grid(row=0, column=5, columnspan=3, sticky="nsew")
Cuenta_atras = Label(Frame_1, text="00:00:00", font=("Helvetica", 48), relief=RIDGE)
Cuenta_atras.grid(row=1, column=5, sticky="nsew")
L_PvsT = Label(Frame_1, text="Pregunta VS Tiempo",font=("Arial" ,18), anchor="w")
L_PvsT.grid(row=2, column=5, columnspan=3, sticky="nsew")
PvsT = Label(Frame_1, text="00:00:00", font=("Helvetica", 48), relief=RIDGE)
PvsT.grid(row=3, column=5, sticky="nsew")
L_media = Label(Frame_1, text="Media de tiempo por respuesta", font=("Arial" ,18), anchor="w")
L_media.grid(row=4, column=5, columnspan=3, sticky="nsew")
Media = Label(Frame_1, text="00:00:00", font=("Helvetica", 48), relief=RIDGE)
Media.grid(row=5, column=5, sticky="nsew")
#-++Frame 2 Preguntas y respuestas traducidas
Frame_2 = Frame(root)
Frame_2.pack(anchor=W)
Frame_2.config(width=(ancho-(ancho/4)),height=alto/2) 
#separacion
linea2 = Canvas(Frame_2, width=ancho/2, height=60 ,bg="#F0F0F0")
linea2.grid(row=0, columnspan=10)
#--+Entry
E2_r1 = Text(Frame_2, width=50, height=4)
E2_r1.grid(row=1, column=3, padx=5)
E2_r2 = Text(Frame_2, width=50, height=4)
E2_r2.grid(row=2, column=3, padx=5)
E2_r3 = Text(Frame_2, width=50, height=4)
E2_r3.grid(row=3, column=3, padx=5)
E2_r4 = Text(Frame_2, width=50, height=4)
E2_r4.grid(row=4, column=3, padx=5)
E2_r5 = Text(Frame_2, width=50, height=4)
E2_r5.grid(row=5, column=3, padx=5)
#--+Campos
Txt_Pregunta_tradu = Text(Frame_2, width=90, height=20)
Txt_Pregunta_tradu.grid(row=1, rowspan=5, column=0, padx=20, pady=20)
scroll_Pregunta_tradu = Scrollbar(Frame_2, command=Txt_Pregunta_tradu.yview)
scroll_Pregunta_tradu.grid(row=1, rowspan=5, column=1, sticky="nsew")
Txt_Pregunta_tradu.config(yscrollcommand=scroll_Pregunta_tradu.set)
#--+Botones
btn_r1 = Button(Frame_2, text="1.", command=r)
btn_r1.grid(row=1, column=2, pady=10, sticky="nsew")
btn_r2 = Button(Frame_2, text="2.", command=r)
btn_r2.grid(row=2, column=2, pady=10, sticky="nsew")
btn_r3 = Button(Frame_2, text="3.", command=r)
btn_r3.grid(row=3, column=2, pady=10, sticky="nsew")
btn_r4 = Button(Frame_2, text="4.", command=r)
btn_r4.grid(row=4, column=2, pady=10, sticky="nsew")
btn_r5 = Button(Frame_2, text="5.", command=r)
btn_r5.grid(row=5, column=2, pady=10, sticky="nsew")
"""
Radiobutton(Frame_2, text=R1, value=1, variable=select, command=r).grid( row=1, column=2)
Radiobutton(Frame_2, text=R2, value=2, variable=select, command=r).grid( row=2, column=2)
Radiobutton(Frame_2, text=R3, value=3, variable=select, command=r).grid( row=3, column=2)
Radiobutton(Frame_2, text=R4, value=4, variable=select, command=r).grid( row=4, column=2)
Radiobutton(Frame_2, text=R5, value=5, variable=select, command=r).grid( row=5, column=2)"""
#separacion
linea2 = Canvas(Frame_2, width=(ancho/20), height=30 ,bg="#F0F0F0")
linea2.grid(row=0, column=4)
#Entrada Tiempo Examen
L_tiempo_de_examen = Label(Frame_2, text="Tiempo de examen en minutos", font=("Arial" ,18), anchor="w")
L_tiempo_de_examen.grid(row=1, column=5)
Tiempo_examen = Entry(Frame_2, textvariable=Time_exam_min, font=("Helvetica", 24), relief=RIDGE, justify=RIGHT)
Tiempo_examen.grid(row=2, column=5)

#Limite de preguntas a resolver
L_cantidad_de_preguntas = Label(Frame_2, text="Cantidad de preguntas", font=("Arial" ,18), anchor="w")
L_cantidad_de_preguntas.grid(row=3, column=5, sticky="nsew")
Tiempo_examen = Entry(Frame_2, textvariable=limite_num_preguntas, font=("Helvetica", 24), relief=RIDGE, justify=RIGHT)
Tiempo_examen.grid(row=4, column=5)
#Aciertos / Fallos
L_aciertos = Label(Frame_2, text="Aciertos", font=("Arial" ,18), anchor=CENTER)
L_aciertos.grid(row=5, column=5)
Aciertos = Label(Frame_2, text=aciertos, relief=RIDGE, justify=CENTER)
Aciertos.grid(row=6, column=5, sticky="nsew")
L_fallos = Label(Frame_2, text="Fallos", font=("Arial" ,18), anchor=CENTER)
L_fallos.grid(row=5, column=6)
Fallos = Label(Frame_2, text=fallos, relief=RIDGE, justify=CENTER)
Fallos.grid(row=6, column=6, sticky="nsew")
#-++Frame 3 Nota
Frame_3 = Frame(root)
Frame_3.pack(anchor=W)
Frame_3.config(width=(ancho-(ancho/4)),height=alto/2) 
#separacion
linea3 = Canvas(Frame_3, width=(ancho*2), height=40 ,bg="#F0F0F0")
linea3.grid(row=1, column=5, columnspan=6)

L_nota = Label(Frame_3, text="Nota", font=("Arial" ,18), anchor=CENTER)
L_nota.grid(row=0, column=7)
Nota = Label(Frame_3, text=puntuacion, relief=RIDGE, justify=CENTER)
Nota.grid(row=1, column=7, sticky="nsew")




root.mainloop()
