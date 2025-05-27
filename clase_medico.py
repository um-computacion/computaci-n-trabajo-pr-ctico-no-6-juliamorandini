class Medico: 
    def __init__(self, matricula, nombre, especialidad):
        self.matricula = matricula 
        self.nombre = nombre
        self.especialidad = especialidad
    
    def set_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def get_estado(self):
        return self.estado

    def obtener_matricula(self):
        return self.matricula

    def __str__(self):
        return f"Médico: {self.nombre} (Matrícula: {self.matricula}), Especialidad: {self.especialidad}"