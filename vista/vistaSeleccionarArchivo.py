from tkinter import Frame, Label, filedialog, StringVar, Entry, Button, messagebox, E

class SeleccionarArchivo:

    def __init__(self, ventana, database, ventanaAnterior):
        self.ventanaAnterior = ventanaAnterior
        self.db = database
        self.ventana = ventana
        ventanaAncho, ventanaAlto = 400, 120
        pantallaAncho = ventana.winfo_screenwidth()
        pantallaAlto = ventana.winfo_screenheight()
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

    def agregarPanel(self):
        self.panel = Frame(self.ventana)
        self.panel.config(bg="white")
        self.panel.pack(fill="both", expand="true")

    def agregarEtiquetas(self):
        etiqueta = Label(self.panel, text="Ruta:", font=("Segoe UI", 11, "normal"), bg="white", anchor=E)
        etiqueta.place(x=15, y=30, width=50, height=20)

    def agregarCampos(self):
        self.txtRuta = StringVar()
        self.campoRuta = Entry(self.panel, font=("Segoe UI", 11, "normal"), textvariable=self.txtRuta, bd=0, highlightthickness=1)
        self.campoRuta.place(x=70, y=30, width=200, height=20)
        self.campoRuta.config(highlightbackground = "#B2BABB", highlightcolor= "#5499C7")
        self.campoRuta.focus()
        #tkinter.Label(self.panel, bg="#5DADE2").place(x=70, y=50, width=200, height=1)

    def agregarBotones(self):
        botonSeleccionar = Button(self.panel, text="Seleccionar", font=("Segoe UI", 11, "normal"), bg="#515A5A", fg="white", activebackground="#7F8C8D", activeforeground="white", cursor="hand2", bd=0, command=self.seleccionarArchivo)
        botonSeleccionar.place(x=285, y=30, width=90, height=20)
        botonAceptar = Button(self.panel, text="Aceptar", font=("Segoe UI", 11, "normal"), bg="#154360", fg="white", activebackground="#1F618D", activeforeground="white", cursor="hand2", bd=0, command=self.cargarArchivo)
        botonAceptar.place(x=210, y=70, width=75, height=20)
        botonRegresar = Button(self.panel, text="Regresar", font=("Segoe UI", 11, "normal"), bg="#C0392B", fg="white", activebackground="#EC7063", activeforeground="white", cursor="hand2", bd=0, command=self.regresar)
        botonRegresar.place(x=300, y=70, width=75, height=20)

    def seleccionarArchivo(self):
        ruta = filedialog.askopenfilename(title="Abrir")
        self.txtRuta.set(ruta)

    def cargarArchivo(self):
        if (self.txtRuta.get() == ""):
            messagebox.showwarning("Advertencia", "¡Complete el campo vacio!")
        else:
            try:
                archivo = open(self.txtRuta.get(), 'r+')
                info = archivo.readlines()
                info = list(map(lambda l: l.rstrip("\n"), info)) 
                for cadena in info:
                    curso = cadena.split(",")
                    if int(curso[3]) == 1:
                        curso[3] = "Obligatorio"
                    else:
                        curso[3] = "Opcional"
                    if int(curso[6]) == 0:
                        curso[6] = "Aprobado"
                    elif int(curso[6]) == 1:
                        curso[6] = "Cursando"
                    else:
                        curso[6] = "Pendiente"
                    self.db.addCurso(curso[0], curso[1], curso[2], curso[3], curso[4], curso[5], curso[6])
                archivo.close()
                messagebox.showinfo("Informacion", "¡Curso(s) agregado(s) exitosamente!")
                self.txtRuta.set("")
            except FileNotFoundError:
                messagebox.showerror("Error", "¡El archivo no existe!")
            except IndexError:
                messagebox.showerror("Error", "¡El archivo no se puede leer!\nRevise que el archivo este bien \nescrito o que sea de extension .lfp")
            
    def regresar(self):
        self.ventana.destroy()   
        self.ventanaAnterior.deiconify()

    def cerrarVentana(self):
        self.ventanaAnterior.destroy()

