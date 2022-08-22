from tkinter import W, Button, Frame, Label, Toplevel, messagebox
from vista.vistaSeleccionarArchivo import SeleccionarArchivo
from vista.vistaGestionarCursos import GestionarCurso
from vista.vistaConteoCreditos import ConteoCreditos

class Inicio:

    def __init__(self, ventana, database):
        self.db = database
        self.ventana = ventana
        ventanaAncho, ventanaAlto = 500,400
        pantallaAncho = self.ventana.winfo_screenwidth()
        pantallaAlto = self.ventana.winfo_screenheight()
        posicionX = int(pantallaAncho/2 - ventanaAncho/2)
        posicionY = int(pantallaAlto/2 - ventanaAlto/2)
        self.ventana.geometry(f'{ventanaAncho}x{ventanaAlto}+{posicionX}+{posicionY}')
        self.ventana.title("PensumApp")
        self.ventana.resizable(False, False)
        self.iniciarComponentes()

    def iniciarComponentes(self):
        self.agregarPanel()
        self.agregarEtiquetas()
        self.agregarBotones()

    def agregarPanel(self):
        self.panel = Frame(self.ventana)
        self.panel.config(bg="white")
        self.panel.pack(fill="both", expand="true")

    def agregarBotones(self):
        botonCargarArchivos = Button(self.panel, text="Cargar Archivos", font=("Segoe UI", 11, "normal"), bg="#D68910", fg="white", activebackground="#F39C12", activeforeground="white", cursor="hand2", bd=0, command=self.cargarArchivo)
        botonCargarArchivos.place(x=162, y=170, width=175, height=22)
        botonGestionarCursos = Button(self.panel, text="Gestionar Cursos", font=("Segoe UI", 11, "normal"), bg="#154360", fg="white", activebackground="#1F618D", activeforeground="white", cursor="hand2", bd=0, command=self.gestionarCurso)
        botonGestionarCursos.place(x=162, y=207, width=175, height=22)
        botonConteodeCreditos = Button(self.panel, text="Conteo De Creditos", font=("Segoe UI", 11, "normal"), bg="#515A5A", fg="white", activebackground="#7F8C8D", activeforeground="white", cursor="hand2", bd=0, command=self.contarCreditos)
        botonConteodeCreditos.place(x=162, y=244, width=175, height=22)
        botonSalir = Button(self.panel, text="Salir", font=("Segoe UI", 11, "normal"), bg="#C0392B", fg="white", activebackground="#EC7063", activeforeground="white", cursor="hand2", bd=0, command=self.salir)
        botonSalir.place(x=162, y=281, width=175, height=22)

    def agregarEtiquetas(self):
        etiquetaNombredelCurso = Label(self.panel, text="Nombre del curso: Lab. Lenguajes Formales y de Programacion B+", font=("Segoe UI", 11, "normal"), bg="white", anchor=W)
        etiquetaNombredelCurso.place(x=25, y=10, width=450, height=20)
        etiquetaNombredelEstudiante = Label(self.panel, text="Nombre del estudiante: Pedro Luis Pu Tavico", font=("Segoe UI", 11, "normal"), bg="white", anchor=W)
        etiquetaNombredelEstudiante.place(x=25, y=40, width=450, height=20)
        etiquetaCarne = Label(self.panel, text="Carné del estudiante: 202000562", font=("Segoe UI", 11, "normal"), bg="white", anchor=W)
        etiquetaCarne.place(x=25, y=70, width=450, height=20)

    def cargarArchivo(self):
        self.ventana.withdraw()
        nuevaVentana = SeleccionarArchivo(Toplevel(), self.db, self.ventana)
        nuevaVentana.ventana.focus_force()
        nuevaVentana.ventana.mainloop()
        
    def gestionarCurso(self): 
        self.ventana.withdraw()
        nuevaVentana = GestionarCurso(Toplevel(), self.db, self.ventana) 
        nuevaVentana.ventana.focus_force() 
        nuevaVentana.ventana.mainloop()

    def contarCreditos(self):
        self.ventana.withdraw()
        nuevaVentana = ConteoCreditos(Toplevel(), self.db, self.ventana)
        nuevaVentana.ventana.focus_force()
        nuevaVentana.ventana.mainloop()

    def salir(self):
        respuesta = messagebox.askyesno("Confirmacion", "¿Seguro que desea salir?", default="no")
        if respuesta: self.ventana.destroy()
    

