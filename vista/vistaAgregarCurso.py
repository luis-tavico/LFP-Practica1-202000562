from tkinter import Frame, Label, ttk, messagebox, StringVar, Button, Entry, W, CENTER

class AgregarCurso:

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
        self.agregarEtiquetas()
        self.agregarCamposYCajas()
        self.agregarBotones()

    def agregarPanel(self):
        self.panel = Frame(self.ventana)
        self.panel.config(bg="white")
        self.panel.pack(fill="both", expand="true")
    
    def agregarEtiquetas(self):
        etiquetaTitulo = Label(self.panel, text="AGREGAR CURSO", font=("Microsoft Yahei UI Light", 14, "bold"), bg="white", fg="#D35400", anchor=CENTER)
        etiquetaTitulo.place(x=0, y=35, width=500, height=20)
        etiquetaCodigo = Label(self.panel, text="Codigo:", font=("Segoe UI", 11, "normal"), bg="white", anchor=W)
        etiquetaCodigo.place(x=54, y=75, width=100, height=20)
        etiquetaNombre = Label(self.panel, text="Nombre:", font=("Segoe UI", 11, "normal"), bg="white", anchor=W)
        etiquetaNombre.place(x=54, y=110, width=100, height=20)
        etiquetaPreRequisito = Label(self.panel, text="Pre Requisito:", font=("Segoe UI", 11, "normal"), bg="white", anchor=W)
        etiquetaPreRequisito.place(x=54, y=145, width=100, height=20)
        etiquetaOpcionalidad = Label(self.panel, text="Opcionalidad:", font=("Segoe UI", 11, "normal"), bg="white", anchor=W)
        etiquetaOpcionalidad.place(x=54, y=180, width=100, height=20)
        etiquetaSemestre = Label(self.panel, text="Semestre:", font=("Segoe UI", 11, "normal"), bg="white", anchor=W)
        etiquetaSemestre.place(x=54, y=217, width=100, height=20)
        etiquetaCreditos = Label(self.panel, text="Créditos:", font=("Segoe UI", 11, "normal"), bg="white", anchor=W)
        etiquetaCreditos.place(x=54, y=254, width=100, height=20)
        etiquetaEstado = Label(self.panel, text="Estado:", font=("Segoe UI", 11, "normal"), bg="white", anchor=W)
        etiquetaEstado.place(x=54, y=291, width=100, height=20)

    def agregarCamposYCajas(self):
        self.txtcodigo = StringVar()
        self.campoCodigo = Entry(self.panel, font=("Segoe UI", 11, "normal"), textvariable=self.txtcodigo, bd=0, highlightthickness=1)
        self.campoCodigo.place(x=166, y=75, width=275, height=20)
        self.campoCodigo.config(highlightbackground = "#8e979a", highlightcolor= "#047CD4") 
        #self.campoCodigo.bind('<FocusIn>', self.focusIn)
        #self.campoCodigo.bind('<FocusOut>', self.focusOut)
        #tkinter.Label(self.panel, bg="#047CD4").place(x=166, y=95, width=275, height=1)
        self.campoCodigo.focus_set()
        self.txtnombre = StringVar()
        self.campoNombre = Entry(self.panel, font=("Segoe UI", 11, "normal"), textvariable=self.txtnombre, bd=0, highlightthickness=1)
        self.campoNombre.place(x=166, y=110, width=275, height=20)
        self.campoNombre.config(highlightbackground = "#8e979a", highlightcolor= "#047cd4")
        #tkinter.Label(self.panel, bg="#047CD4").place(x=166, y=130, width=275, height=1)
        self.txtprerrequisito = StringVar()
        campoPrerequisito = Entry(self.panel, font=("Segoe UI", 11, "normal"), textvariable=self.txtprerrequisito, bd=0, highlightthickness=1)
        campoPrerequisito.place(x=166, y=145, width=275, height=20)
        campoPrerequisito.config(highlightbackground = "#8e979a", highlightcolor= "#047cd4")
        #tkinter.Label(self.panel, bg="#047CD4").place(x=166, y=165, width=275, height=1)
        self.cajaOpcionalidad = ttk.Combobox(self.panel, font=("Segoe UI", 10, "normal"), state="readonly")
        self.cajaOpcionalidad["values"] = ("Seleccionar","Obligatorio", "Opcional")
        self.cajaOpcionalidad.current(0)
        self.cajaOpcionalidad.place(x=166, y=180, width=275, height=22)
        self.cajaSemestre = ttk.Combobox(self.panel, font=("Segoe UI", 10, "normal"), state="readonly")
        self.cajaSemestre["values"] = ("Seleccionar","1","2","3","4","5","6","7","8","9","10")
        self.cajaSemestre.current(0)
        self.cajaSemestre.place(x=166, y=217, width=275, height=22)
        self.txtcreditos = StringVar()
        campoCreditos = Entry(self.panel, font=("Segoe UI", 11, "normal"), textvariable=self.txtcreditos, bd=0, highlightthickness=1)
        campoCreditos.place(x=166, y=254, width=275, height=20)
        campoCreditos.config(highlightbackground = "#8e979a", highlightcolor= "#047cd4")
        #tkinter.Label(self.panel, bg="#047CD4").place(x=166, y=274, width=275, height=1)
        self.cajaEstado = ttk.Combobox(self.panel, font=("Segoe UI", 10, "normal"), state="readonly")
        self.cajaEstado["values"] = ("Seleccionar","Aprobado", "Cursando", "Pendiente")
        self.cajaEstado.current(0)
        self.cajaEstado.place(x=166, y=289, width=275, height=22)

    def agregarBotones(self):
        botonAgregar = Button(self.panel, text="Agregar", font=("Segoe UI", 11, "normal"), bg="#154360", fg="white", activebackground="#1F618D", activeforeground="white", cursor="hand2", bd=0, command=self.agregarCurso)
        botonAgregar.place(x=221, y=333, width=100, height=20)
        botonRegresar = Button(self.panel, text="Regresar", font=("Segoe UI", 11, "normal"), bg="#C0392B", fg="white", activebackground="#EC7063", activeforeground="white", cursor="hand2", bd=0, command=self.regresar)
        botonRegresar.place(x=341, y=333, width=100, height=20)

    def focusIn(self, e):
        if (self.txtcodigo.get() == "Ingrese un codigo"):
            self.txtcodigo.set("")
            self.campoCodigo.config(fg="black")
    
    def focusOut(self, e):
        if (self.txtnombre.get() == ""):
            self.txtcodigo.set("Ingrese un codigo")
            self.campoCodigo.config(fg="gray")

    def agregarCurso(self):
        if ((self.txtcodigo.get() and self.txtnombre.get() and self.txtcreditos.get()) != "") and (self.cajaOpcionalidad.get() != "Seleccionar" and self.cajaSemestre.get() != "Seleccionar" and self.cajaEstado.get() != "Seleccionar"):
            if (self.txtcodigo.get().isdigit() and self.txtcreditos.get().isdigit()):
                self.db.addCurso(self.txtcodigo.get(), self.txtnombre.get(), self.txtprerrequisito.get(), self.cajaOpcionalidad.get(), self.cajaSemestre.get(), self.txtcreditos.get(), self.cajaEstado.get())
                messagebox.showinfo("Informacion", "¡Curso agregado exitosamente!")
                self.limpiarCampos()
            else:
                messagebox.showwarning("Advertencia", "¡Ingrese solo numeros en los campos: Codigo y Creditos!")
        else:
            messagebox.showwarning("Advertencia", "¡Complete los campos obligatorios!")

    def regresar(self):
        self.ventana.destroy()   
        self.ventanaAnterior.deiconify() 

    def limpiarCampos(self):
        self.txtcodigo.set("")
        self.txtnombre.set("")
        self.txtprerrequisito.set("")
        self.cajaOpcionalidad.current(0)
        self.cajaSemestre.current(0)
        self.txtcreditos.set("")
        self.cajaEstado.current(0)

    def cerrarVentana(self):
        self.ventanaInicial.destroy()