class Paciente:
    def __init__(self, dni, nombre, fc_nacimiento):
        self.dni = dni
        self.nombre = nombre
        self.fc_nacimiento = fc_nacimiento

    def set_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def get_estado(self):
        return self.estado

    def obtener_dni(self):
        return self.dni

    def __str__(self):
        return "Paciente: {self.nombre} (DNI: {self.dni}), Fecha de nacimiento: {self.fc_nacimiento}"