from tkinter import CENTER, END, Button, Frame
from tkinter import ttk

class ListarCurso:

    def __init__(self, ventana, database, ventanaAnterior, ventanaInicial):
        self.ventanaInicial = ventanaInicial
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
        self.agregarTabla()
    
    def agregarPanel(self):
        self.panel = Frame(self.ventana)
        self.panel.config(bg="white")
        self.panel.pack(fill="both", expand="true")

    def agregarBotones(self):
        botonRegresar = Button(self.panel, text="Regresar", font=("Segoe UI", 11, "normal"), bg="#C0392B", fg="white", activebackground="#EC7063", activeforeground="white", cursor="hand2", bd=0, command=self.regresar)
        botonRegresar.place(x=380, y=360, width=100, height=20)
    
    def agregarTabla(self):
        tabla = ttk.Treeview(self.panel, columns=("col1", "col2", "col3", "col4", "col5", "col6"))
        #Agregando titulos a encabezado
        tabla.heading("#0", text="Codigo", anchor=CENTER)
        tabla.heading("col1", text="Nombre", anchor=CENTER)
        tabla.heading("col2", text="Prerrequisito", anchor=CENTER)
        tabla.heading("col3", text="Opcionalidad", anchor=CENTER)
        tabla.heading("col4", text="Semestre", anchor=CENTER)
        tabla.heading("col5", text="Creditos", anchor=CENTER)
        tabla.heading("col6", text="Estado", anchor=CENTER)
        #Editando encabezado
        tabla.column("#0", width=49, anchor=CENTER)
        tabla.column("col1", width=90, anchor=CENTER)
        tabla.column("col2", width=75, anchor=CENTER)
        tabla.column("col3", width=80, anchor=CENTER)
        tabla.column("col4", width=60, anchor=CENTER)
        tabla.column("col5", width=55, anchor=CENTER)   
        tabla.column("col6", width=49, anchor=CENTER)
        #Llenando tabla
        for curso in self.db.getCursos():
            tabla.insert("",END, text=curso.getCodigo(), values=(curso.getNombre(), curso.getPrerrequisito(), curso.getOpcionalidad(), curso.getSemestre(), curso.getCreditos(), curso.getEstado()))
        tabla.place(x=20, y=20, width=460, height=320)

    def regresar(self):
        self.ventana.destroy()   
        self.ventanaAnterior.deiconify()

    def cerrarVentana(self):
        self.ventanaInicial.destroy()
