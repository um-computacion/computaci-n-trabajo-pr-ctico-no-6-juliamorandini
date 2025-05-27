class Historia_Clinica:
    def __init__(self, paciente, turnos=None, recetas=None):
        self.paciente = paciente
        self.turnos = turnos if turnos is not None else []
        self.recetas = recetas if recetas is not None else []

    def agregar_turno(self, turno):
        self.turnos.append(turno)

    def agregar_receta(self, receta):
        self.recetas.append(receta)

    def obtener_turnos(self):
        return self.turnos

    def obtener_recetas(self):
        return self.recetas

    def __str__(self):
        info = f"Historia clínica de {self.paciente.nombre} (DNI: {self.paciente.dni})\n"
        info += "Turnos:\n"
        for t in self.turnos:
            info += f"  - {t.fecha_hora} con Dr/a. {t.medico.nombre}\n"
        info += "Recetas:\n"
        for r in self.recetas:
            info += f"  - {r.hora_fecha} por Dr/a. {r.medico.nombre}: {', '.join(r.medicamentos)}\n"
        return info