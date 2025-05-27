from clase_historia_clinica import Historia_Clinica
from clase_medico import Medico
from clase_paciente import Paciente
from clase_turno import Turno
from clase_receta import Receta
from datetime import datetime
from excepciones import PacienteNoExisteError, MedicoNoExisteError, TurnoDuplicadoError

class Clinica:
    def __init__(self):
        self.pacientes = {}  
        self.medicos = {}    
        self.turnos = []    
        self.historias_clinicas = {}  

    def agregar_paciente(self, paciente):
        self.pacientes[paciente.dni] = paciente
        if paciente.dni not in self.historias_clinicas:
            self.historias_clinicas[paciente.dni] = Historia_Clinica(paciente)

    def agregar_medico(self, medico):
        self.medicos[medico.matricula] = medico

    def agendar_turno(self, dni, matricula, fecha_hora):
        paciente = self.pacientes.get(dni)
        if not paciente:
            raise PacienteNoExisteError("El paciente no existe.")
        medico = self.medicos.get(matricula)
        if not medico:
            raise MedicoNoExisteError("El médico no existe.")
        # Verificar turno duplicado
        for t in self.turnos:
            if t.paciente.dni == dni and t.medico.matricula == matricula and t.fecha_hora == fecha_hora:
                raise TurnoDuplicadoError("l turno ya existe.")
        turno = Turno(paciente, medico, fecha_hora)
        self.turnos.append(turno)
        self.historias_clinicas[dni].agregar_turno(turno)
        return turno

    def emitir_receta(self, dni, matricula, medicamentos, hora_fecha=None):
        paciente = self.pacientes.get(dni)
        if not paciente:
            raise PacienteNoExisteError("el pacientee no existe.")
        medico = self.medicos.get(matricula)
        if not medico:
            raise MedicoNoExisteError(" médico no existe.")
        if hora_fecha is None:
            hora_fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
        receta = Receta(paciente, medico, medicamentos, hora_fecha)
        self.historias_clinicas[dni].agregar_receta(receta)
        return receta

    def obtener_historia_clinica(self, dni):
        return self.historias_clinicas.get(dni)

    def obtener_turnos(self):
        return self.turnos

    def main():
        clinica = Clinica()
        paciente1 = Paciente ("Juan", "Perez", "12345678", "M")
        medico1 = Medico("Dr. Smith", "87654321")
        clinica.agregar_paciente(paciente1)
        clinica.agregar_medico(medico1)
        turno1 = clinica.agendar_turno("12345678", "87654321", "2023-10-10 10:00")
        receta1 = clinica.emitir_receta("12345678", "87654321", ["Medicamento A", "Medicamento B"])
        historia = clinica.obtener_historia_clinica("12345678")
        print(historia)
        turnos = clinica.obtener_turnos()
        print(turnos)

