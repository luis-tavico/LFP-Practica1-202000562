from tkinter import Frame, Button, Toplevel
from vista.vistaListarCursos import ListarCurso
from vista.vistaAgregarCurso import AgregarCurso
from vista.vistaVerificarCodigo import VerficiarCodigo
from vista.vistaEliminarCurso import EliminarCurso

class GestionarCurso:
    
    def __init__(self, ventana, database, ventanaAnterior):
        self.ventanaAnterior = ventanaAnterior
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
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrarVentana)
        self.iniciarComponentes()
        
    def iniciarComponentes(self):
        self.agregarPanel()
        self.agregarBotones()

    def agregarPanel(self):
        self.panel = Frame(self.ventana)
        self.panel.config(bg="white")
        self.panel.pack(fill="both", expand="true")

    def agregarBotones(self):
        botonListar = Button(self.panel, text="Listar Curso", font=("Segoe UI", 11, "normal"), bg="#34495E", fg="white", activebackground="#5D6D7E", activeforeground="white", cursor="hand2", bd=0, command=self.listarCursos)
        botonListar.place(x=175, y=115, width=150, height=20)
        botonAgregar = Button(self.panel, text="Agregar Curso", font=("Segoe UI", 11, "normal"), bg="#34495E", fg="white", activebackground="#5D6D7E", activeforeground="white", cursor="hand2", bd=0, command=self.agregarCurso)
        botonAgregar.place(x=175, y=150, width=150, height=20)
        botonEditar = Button(self.panel, text="Editar Curso", font=("Segoe UI", 11, "normal"), bg="#34495E", fg="white", activebackground="#5D6D7E", activeforeground="white", cursor="hand2", bd=0, command=self.editarCurso)
        botonEditar.place(x=175, y=185, width=150, height=20)
        botonEliminar = Button(self.panel, text="Eliminar Curso", font=("Segoe UI", 11, "normal"), bg="#34495E", fg="white", activebackground="#5D6D7E", activeforeground="white", cursor="hand2", bd=0, command=self.eliminarCurso)
        botonEliminar.place(x=175, y=220, width=150, height=20)
        botonRegresar = Button(self.panel, text="Regresar", font=("Segoe UI", 11, "normal"), bg="#C0392B", fg="white", activebackground="#EC7063", activeforeground="white", cursor="hand2", bd=0, command=self.regresar)
        botonRegresar.place(x=175, y=255, width=150, height=20)

    def listarCursos(self):
        self.ventana.withdraw()
        nuevaVentana = ListarCurso(Toplevel(), self.db, self.ventana, self.ventanaAnterior)
        nuevaVentana.ventana.focus_force()
        nuevaVentana.ventana.mainloop()

    def agregarCurso(self):
        self.ventana.withdraw()
        nuevaVentana = AgregarCurso(Toplevel(), self.db, self.ventana, self.ventanaAnterior)
        nuevaVentana.ventana.focus_force()
        nuevaVentana.ventana.mainloop()

    def editarCurso(self): 
        self.ventana.withdraw()
        nuevaVentana = VerficiarCodigo(Toplevel(), self.db, self.ventana, self.ventanaAnterior)
        nuevaVentana.ventana.focus_force() 
        nuevaVentana.ventana.mainloop()

    def eliminarCurso(self): 
        self.ventana.withdraw()
        nuevaVentana = EliminarCurso(Toplevel(), self.db, self.ventana, self.ventanaAnterior)
        nuevaVentana.ventana.focus_force()
        nuevaVentana.ventana.mainloop()

    def regresar(self):
        self.ventana.destroy()   
        self.ventanaAnterior.deiconify() 

    def cerrarVentana(self):
        self.ventanaAnterior.destroy()