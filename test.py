import unittest
from clase_clinica import Clinica
from clase_paciente import Paciente
from clase_medico import Medico
from clase_turno import Turno
from excepciones import PacienteNoExisteError, MedicoNoExisteError, TurnoDuplicadoError

class TestClinica(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()
        self.paciente = Paciente("123", "Juan", "2000-01-01")
        self.medico = Medico("A1", "Dra. Ana", "Pediatría")
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)

    def test_agregar_paciente(self):
        nuevo = Paciente("456", "Maria", "1999-05-05")
        self.clinica.agregar_paciente(nuevo)
        self.assertIn("456", self.clinica.pacientes)
        self.clinica.agregar_paciente(nuevo)
        self.assertEqual(self.clinica.pacientes["456"].nombre, "Maria")

    def test_agregar_medico(self):
        nuevo = Medico("B2", "Dr. Luis", "Cardiología")
        self.clinica.agregar_medico(nuevo)
        self.assertIn("B2", self.clinica.medicos)
        self.clinica.agregar_medico(nuevo)
        self.assertEqual(self.clinica.medicos["B2"].nombre, "Dr. Luis")

    def test_agendar_turno_valido(self):
        turno = self.clinica.agendar_turno("123", "A1", "2024-06-01 10:00")
        self.assertEqual(len(self.clinica.turnos), 1)
        self.assertEqual(turno.paciente.nombre, "Juan")
        self.assertEqual(turno.medico.nombre, "Dra. Ana")

    def test_turno_duplicado(self):
        self.clinica.agendar_turno("123", "A1", "2024-06-01 10:00")
        with self.assertRaises(TurnoDuplicadoError):
            self.clinica.agendar_turno("123", "A1", "2024-06-01 10:00")

    def test_agendar_turno_paciente_no_existe(self):
        with self.assertRaises(PacienteNoExisteError):
            self.clinica.agendar_turno("999", "A1", "2024-06-01 10:00")

    def test_agendar_turno_medico_no_existe(self):
        with self.assertRaises(MedicoNoExisteError):
            self.clinica.agendar_turno("123", "Z9", "2024-06-01 10:00")

    def test_emitir_receta_valida(self):
        receta = self.clinica.emitir_receta("123", "A1", ["Paracetamol"])
        historia = self.clinica.obtener_historia_clinica("123")
        self.assertIn(receta, historia.obtener_recetas())

    def test_emitir_receta_paciente_no_existe(self):
        with self.assertRaises(PacienteNoExisteError):
            self.clinica.emitir_receta("999", "A1", ["Ibuprofeno"])

    def test_emitir_receta_medico_no_existe(self):
        with self.assertRaises(MedicoNoExisteError):
            self.clinica.emitir_receta("123", "Z9", ["Ibuprofeno"])

    def test_historia_clinica_turnos_y_recetas(self):
        self.clinica.agendar_turno("123", "A1", "2024-06-01 10:00")
        self.clinica.emitir_receta("123", "A1", ["Ibuprofeno"])
        historia = self.clinica.obtener_historia_clinica("123")
        self.assertEqual(len(historia.obtener_turnos()), 1)
        self.assertEqual(len(historia.obtener_recetas()), 1)

    def test_listar_medicos(self):
        clinica = Clinica()
        medico1 = Medico("A1", "Dra. Ana", "Pediatría")
        medico2 = Medico("B2", "Dr. Luis", "Cardiología")
        clinica.agregar_medico(medico1)
        clinica.agregar_medico(medico2)
        for m in clinica.medicos.values():
            print(f"matricula: {m.matricula}, nombre: {m.nombre}, especialidad: {m.especialidad}")

if __name__ == "__main__":
    unittest.main()