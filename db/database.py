from modelo.modeloCurso import Curso

class Database():

    def __init__(self):
        self.Cursos = []
        self.codigoCursos = []
        self.creditosAprobados = 0
        self.creditosCursando = 0
        self.creditosPendientes = 0
        self.creditosHastaN = 0
        self.creditosSemestreAprobados = 0
        self.creditosSemestrePendientes = 0

    def addCurso(self, codigo, nombre, prerrequisito, opcionalidad, semestre, creditos, estado):
        nuevoCurso = Curso(codigo, nombre, prerrequisito, opcionalidad, semestre, creditos, estado)
        if (codigo in self.codigoCursos):
            self.Cursos[self.codigoCursos.index(codigo)] = nuevoCurso
        else:
            self.Cursos.append(nuevoCurso)
            self.codigoCursos.append(codigo)

    def updateCurso(self, codigo, nombre, prerrequisito, opcionalidad, semestre, creditos, estado):
        cursoEditado = Curso(codigo, nombre, prerrequisito, opcionalidad, semestre, creditos, estado)
        self.Cursos[self.codigoCursos.index(codigo)] = cursoEditado
        self.codigoCursos[self.codigoCursos.index(codigo)] = codigo

    def deleteCurso(self, codigo):
        self.Cursos.pop(self.codigoCursos.index(codigo))
        self.codigoCursos.remove(codigo)

    def searchCodigo(self, codigo):
        if (codigo in self.codigoCursos):
            return True
        else:
            return False

    def getCurso(self, codigo):
        curso = self.Cursos[self.codigoCursos.index(codigo)]
        return curso

    def getCursos(self):
        return self.Cursos

    def sumatoriaCreditos(self):
        self.creditosAprobados = 0
        self.creditosCursando = 0
        self.creditosPendientes = 0
        for curso in self.Cursos:
            if curso.getEstado() == "Aprobado":
                self.creditosAprobados += int(curso.getCreditos())
            elif curso.getEstado() == "Cursando":
                self.creditosCursando += int(curso.getCreditos())
            elif curso.getEstado() == "Pendiente":
                if curso.getOpcionalidad() == "Obligatorio":
                    self.creditosPendientes += int(curso.getCreditos())

    def sumatoriaCreditosHastaN(self, semestre):
        self.creditosHastaN = 0
        for curso in self.Cursos:
            if int(curso.getSemestre()) <= semestre and curso.getOpcionalidad() == "Obligatorio":
                self.creditosHastaN += int(curso.getCreditos())

    def sumatoriaCreditosSemestre(self, semestre):
        self.creditosSemestreAprobados = 0
        self.creditosSemestrePendientes = 0
        for curso in self.Cursos:
            if int(curso.getSemestre()) == semestre and (curso.getEstado() == "Aprobado"):
                self.creditosSemestreAprobados += int(curso.getCreditos())
            elif int(curso.getSemestre()) == semestre and (curso.getEstado() == "Pendiente"):
                self.creditosSemestrePendientes += int(curso.getCreditos())
