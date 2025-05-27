class Receta:
    def __init__(self, paciente, medico, medicamentos, hora_fecha):
        self.paciente = paciente
        self.medico = medico
        self.medicamentos = medicamentos
        self.hora_fecha = hora_fecha

    def set_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def get_estado(self):
        return self.estado

    def __str__(self):
        return f"Receta: {self.hora_fecha} - Paciente: {self.paciente.nombre}, Médico: {self.medico.nombre}, Medicamentos: {', '.join(self.medicamentos)}"