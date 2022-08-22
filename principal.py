from tkinter import Tk
from vista.vistaInicio import Inicio
from db.database import Database

if __name__ == "__main__":
    db = Database()
    nuevaVentana = Inicio(Tk(), db)
    nuevaVentana.ventana.mainloop()
