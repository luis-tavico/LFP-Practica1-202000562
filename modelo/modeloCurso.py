class Curso():

    def __init__(self, codigo, nombre, prerrequisito, opcionalidad, semestre, creditos, estado):
        self.codigo = codigo
        self.nombre = nombre
        self.prerrequisito = prerrequisito
        self.opcionalidad = opcionalidad
        self.semestre = semestre
        self.creditos = creditos
        self.estado = estado

##################METODO GET#########################
    def getCodigo(self):
        return self.codigo

    def getNombre(self):
        return self.nombre

    def getPrerrequisito(self):
        return self.prerrequisito

    def getOpcionalidad(self):
        return self.opcionalidad

    def getSemestre(self):
        return self.semestre

    def getCreditos(self):
        return self.creditos
    
    def getEstado(self):
        return self.estado

#################METODO SET##########################
    def setCodigo(self, codigo):
        self.codigo = codigo

    def setNombre(self, nombre):
        self.nombre = nombre

    def setPrerrequisito(self, prerrequisito):
        self.prerrequisito = prerrequisito
    
    def setOpcionalidad(self, opcionalidad):
        self.opcionalidad = opcionalidad

    def setSemestre(self, semestre):
        self.semestre = semestre

    def setCreditos(self, creditos):
        self.creditos = creditos
    
    def setEstado(self, estado):
        self.estado = estado