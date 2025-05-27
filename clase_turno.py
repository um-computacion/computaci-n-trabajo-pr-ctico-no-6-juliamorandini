class Turno:
    def __init__(self, paciente, medico, fecha_hora):
        self.paciente = paciente
        self.medico = medico
        self.fecha_hora = fecha_hora

    def set_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def get_estado(self):
        return self.estado

    def obtener_fecha_hora(self):
        return self.fecha_hora

    def __str__(self):
        return f"Turno: {self.fecha_hora} - Paciente: {self.paciente.nombre}, Médico: {self.medico.nombre}"
