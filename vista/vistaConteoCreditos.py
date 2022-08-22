from tkinter import CENTER, W, Button, Entry, Label, Spinbox, StringVar, Frame

class ConteoCreditos:

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
        self.agregarEtiquetas()
        self.agregarCampos()
        self.agregarBotones()
        self.agregarCajas()
        self.actualizarCreditos()

    def agregarPanel(self):
        self.panel = Frame(self.ventana)
        self.panel.config(bg="white")
        self.panel.pack(fill="both", expand="true")

    def agregarEtiquetas(self):
        etiquetaTitulo = Label(self.panel, text="CONTEO DE CREDITOS", font=("Microsoft Yahei UI Light", 14, "bold"), bg="white", fg="#D35400", anchor=CENTER)
        etiquetaTitulo.place(x=0, y=35, width=500, height=20)
        etiquetaCreditosA = Label(self.panel, text="Créditos Aprobados:", font=("Segoe UI", 11, "normal"), bg="white", anchor=W)
        etiquetaCreditosA.place(x=90, y=75, width=150, height=20)
        etiquetaCreditosC = Label(self.panel, text="Créditos Cursando:", font=("Segoe UI", 11, "normal"), bg="white", anchor=W)
        etiquetaCreditosC.place(x=90, y=110, width=150, height=20)
        etiquetaCreditosP = Label(self.panel, text="Créditos Pendientes:", font=("Segoe UI", 11, "normal"), bg="white", anchor=W)
        etiquetaCreditosP.place(x=90, y=145, width=150, height=20)
        etiquetaCreditosO = Label(self.panel, text="Créditos Obligatorios hasta semestre:", font=("Segoe UI", 11, "normal"), bg="white", anchor=W)
        etiquetaCreditosO.place(x=90, y=180, width=300, height=20)
        etiquetaCreditosS = Label(self.panel, text="Créditos del Semestre:", font=("Segoe UI", 11, "normal"), bg="white", anchor=W)
        etiquetaCreditosS.place(x=90, y=250, width=175, height=20)
        etiquetaAprobados = Label(self.panel, text="Aprobados:", font=("Segoe UI", 11, "normal"), bg="white", anchor=W)
        etiquetaAprobados.place(x=90, y=285, width=150, height=20)
        etiquetaPendientes = Label(self.panel, text="Pendientes:", font=("Segoe UI", 11, "normal"), bg="white", anchor=W)
        etiquetaPendientes.place(x=256, y=285, width=150, height=20)

    def agregarCampos(self):
        self.txtCreditosA = StringVar()
        campoCreditosA = Entry(self.panel, font=("Segoe UI", 11, "normal"), textvariable=self.txtCreditosA, state="readonly", bd=0, highlightthickness=1, justify=CENTER)
        campoCreditosA.place(x=235, y=75, width=50, height=20)
        campoCreditosA.config(highlightbackground = "#8e979a", highlightcolor= "#8e979a")
        self.txtCreditosC = StringVar()
        campoCreditosC = Entry(self.panel, font=("Segoe UI", 11, "normal"), textvariable=self.txtCreditosC, state="readonly", bd=0, highlightthickness=1, justify=CENTER)
        campoCreditosC.place(x=235, y=110, width=50, height=20)
        campoCreditosC.config(highlightbackground = "#8e979a", highlightcolor= "#8e979a")
        self.txtCreditosP = StringVar()
        campoCreditosP = Entry(self.panel, font=("Segoe UI", 11, "normal"), textvariable=self.txtCreditosP, state="readonly", bd=0, highlightthickness=1, justify=CENTER)
        campoCreditosP.place(x=235, y=145, width=50, height=20)
        campoCreditosP.config(highlightbackground = "#8e979a", highlightcolor= "#8e979a")
        self.txtCreditosO = StringVar()
        campoCreditosObligatorios = Entry(self.panel, font=("Segoe UI", 11, "normal"), textvariable=self.txtCreditosO, state="readonly", bd=0, highlightthickness=1, justify=CENTER)
        campoCreditosObligatorios.place(x=265, y=215, width=50, height=20)
        campoCreditosObligatorios.config(highlightbackground = "#8e979a", highlightcolor= "#8e979a")
        self.txtCreditosAp = StringVar()
        campoCreditosAp = Entry(self.panel, font=("Segoe UI", 11, "normal"), textvariable=self.txtCreditosAp, state="readonly", bd=0, highlightthickness=1, justify=CENTER)
        campoCreditosAp.place(x=176, y=285, width=50, height=20)
        campoCreditosAp.config(highlightbackground = "#8e979a", highlightcolor= "#8e979a")
        self.txtCreditosPe = StringVar()
        campoCreditosPe = Entry(self.panel, font=("Segoe UI", 11, "normal"), textvariable=self.txtCreditosPe, state="readonly", bd=0, highlightthickness=1, justify=CENTER)
        campoCreditosPe.place(x=341, y=285, width=50, height=20)
        campoCreditosPe.config(highlightbackground = "#8e979a", highlightcolor= "#8e979a")
    
    def agregarBotones(self):
        botonContar1 = Button(self.panel, text="Contar", font=("Segoe UI", 11, "normal"), bg="#154360", fg="white", activebackground="#1F618D", activeforeground="white", cursor="hand2", bd=0, command=self.contarCreditosHastaN)
        botonContar1.place(x=175, y=215, width=75, height=20)
        botonContar2 = Button(self.panel, text="Contar", font=("Segoe UI", 11, "normal"), bg="#154360", fg="white", activebackground="#1F618D", activeforeground="white", cursor="hand2", bd=0, command=self.contarCreditos)
        botonContar2.place(x=324, y=250, width=75, height=20)
        botonRegresar = Button(self.panel, text="Regresar", font=("Segoe UI", 11, "normal"), bg="#C0392B", fg="white", activebackground="#EC7063", activeforeground="white", cursor="hand2", bd=0, command=self.regresar)
        botonRegresar.place(x=341, y=325, width=100, height=20)

    def agregarCajas(self):
        self.txtSemestreO = StringVar()
        cajaSemestreO = Spinbox(self.panel, textvariable=self.txtSemestreO, state="readonly", font=("Segoe UI", 11, "normal"), justify=CENTER, bd=0, highlightthickness=1)
        cajaSemestreO["values"] = ("1","2","3","4","5","6","7","8","9","10")
        cajaSemestreO.config(highlightbackground = "#8e979a", highlightcolor= "#047cd4")
        cajaSemestreO.place(x=347, y=180, width=60, height=20)
        self.txtSemestre = StringVar()
        cajaSemestre = Spinbox(self.panel, textvariable=self.txtSemestre, state="readonly", font=("Segoe UI", 11, "normal"), justify=CENTER, bd=0, highlightthickness=1)
        cajaSemestre["values"] = ("1","2","3","4","5","6","7","8","9","10")
        cajaSemestre.config(highlightbackground = "#8e979a", highlightcolor= "#047cd4")
        cajaSemestre.place(x=249, y=250, width=60, height=20)

    def actualizarCreditos(self):
        self.db.sumatoriaCreditos()
        self.txtCreditosA.set(self.db.creditosAprobados)
        self.txtCreditosC.set(self.db.creditosCursando)
        self.txtCreditosP.set(self.db.creditosPendientes)

    def contarCreditosHastaN(self):
            self.db.sumatoriaCreditosHastaN(int(self.txtSemestreO.get()))
            self.txtCreditosO.set(str(self.db.creditosHastaN))

    def contarCreditos(self):
            self.db.sumatoriaCreditosSemestre(int(self.txtSemestre.get()))
            self.txtCreditosAp.set(str(self.db.creditosSemestreAprobados))
            self.txtCreditosPe.set(str(self.db.creditosSemestrePendientes))
            
    def regresar(self):
        self.ventana.destroy()   
        self.ventanaAnterior.deiconify()

    def cerrarVentana(self):
        self.ventanaAnterior.destroy()