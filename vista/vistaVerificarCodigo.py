from tkinter import E, Frame, Button, Entry, Label, StringVar, Toplevel, messagebox
from vista.vistaEditarCurso import EditarCurso

class VerficiarCodigo:

    def __init__(self, ventana, database, ventanaAnterior, ventanaInicial):
        self.ventanaInicial = ventanaInicial
        self.ventanaAnterior = ventanaAnterior
        self.db = database
        self.ventana = ventana
        ventanaAncho, ventanaAlto = 400, 120
        pantallaAncho = ventana.winfo_screenwidth()
        pantallaAlto = ventana.winfo_screenheight()
        posicionX = int(pantallaAncho/2 - ventanaAncho/2)
        posicionY = int(pantallaAlto/2 - ventanaAlto/2)
        ventana.geometry(f'{ventanaAncho}x{ventanaAlto}+{posicionX}+{posicionY}')
        self.ventana.title("PensumApp")
        self.ventana.resizable(False, False)
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrarVentana)
        self.iniciarComponentes()
    
    def iniciarComponentes(self):
        self.agregarPanel()
        self.agregarEtiquetas()
        self.agregarCampos()
        self.agregarBotones()

    def agregarPanel(self):
        self.panel = Frame(self.ventana)
        self.panel.config(bg="white")
        self.panel.pack(fill="both", expand="true")

    def agregarEtiquetas(self):
        etiqueta = Label(self.panel, text="Codigo de Curso:", font=("Segoe UI", 11, "normal"), bg="white", anchor=E)
        etiqueta.place(x=15, y=30, width=125, height=20)

    def agregarCampos(self):
        self.txtcodigo = StringVar()
        campoCodigo = Entry(self.panel, text="asdf", textvariable=self.txtcodigo, font=("Segoe UI", 11, "normal"), bd=0, highlightthickness=1)
        campoCodigo.place(x=150, y=30, width=225, height=20)
        campoCodigo.config(highlightbackground = "#B2BABB", highlightcolor= "#5499C7")
        campoCodigo.focus()

    def agregarBotones(self):
        botonAceptar = Button(self.panel, text="Aceptar", font=("Segoe UI", 11, "normal"), bg="#154360", fg="white", activebackground="#1F618D", activeforeground="white", cursor="hand2", bd=0, command=self.buscar)
        botonAceptar.place(x=210, y=70, width=75, height=20)
        botonRegresar = Button(self.panel, text="Regresar", font=("Segoe UI", 11, "normal"), bg="#C0392B", fg="white", activebackground="#EC7063", activeforeground="white", cursor="hand2", bd=0, command=self.regresar)
        botonRegresar.place(x=300, y=70, width=75, height=20)

    def buscar(self):
        if (self.txtcodigo.get() == ""):
            messagebox.showwarning("Advertencia", "¡Complete el campo vacio!")
        else:
            if (self.txtcodigo.get().isdigit()):
                if (self.db.searchCodigo(self.txtcodigo.get())):
                    self.ventana.withdraw()  
                    nuevaVentana = EditarCurso(Toplevel(), self.db, self.ventana, self.txtcodigo.get(), self.ventanaInicial)
                    self.txtcodigo.set("")
                    nuevaVentana.ventana.focus_force()
                    nuevaVentana.ventana.mainloop()
                else:
                    messagebox.showerror("Error", "¡No existe ningun curso con el codigo ingresado!")
            else:
                messagebox.showwarning("Advertencia", "¡Ingrese solo numeros en el campo Codigo!")
                self.txtcodigo.set("")

    def regresar(self):
        self.ventana.destroy()   
        self.ventanaAnterior.deiconify()

    def cerrarVentana(self):
        self.ventanaInicial.destroy()