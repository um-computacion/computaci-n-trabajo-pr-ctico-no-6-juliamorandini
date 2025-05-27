from clase_clinica import Clinica
from clase_paciente import Paciente
from clase_medico import Medico
from clase_turno import Turno
from excepciones import MedicoNoExisteError, PacienteNoExisteError, TurnoDuplicadoError

def menu():
    clinica = Clinica()
    while True:
        print("menu: 1 agregar paciente, 2 agregar medico, 3 agregar turno, 4 emitir receta, 5 ver historia clinica, 6 ver todos los turnos, 7 ver todos los pacientes, 8 ver todos los medicos, 9 salir")
        opcion = input("tu opcion: ")
        if opcion == "1":
            dni = input("DNI: ")
            nombre = input("nombre: ")
            fc_nacimiento = input("fcha de nacimiento: ")
            paciente = Paciente(dni, nombre, fc_nacimiento)
            clinica.agregar_paciente(paciente)
            print("se agrego el paciente!!")
        
        elif opcion == "2":
            matricula = input("matricula del medico: ")
            nombre = input("nombre: ")
            especialidad = input("especialidad: ")
            medico = Medico(matricula, nombre, especialidad)
            clinica.agregar_medico(medico)
            print("se agrego el medico!")
        elif opcion == "3":
            dni = input("DNI del paciente: ")
            matricula = input("matricula del medico: ")
            fecha_hora = input("fecha y hora del turno: ")
            try:
                clinica.agendar_turno(dni, matricula, fecha_hora)
                print("turno agendado!")
            except PacienteNoExisteError:
                print("paciente no encontrado.")
            except MedicoNoExisteError:
                print("el medico no se encuentra.")
            except TurnoDuplicadoError:
                print("Ese turno ya existe.")
        elif opcion == "4":
            dni = input("DNI del paciente: ")
            matricula = input("matricula del medico: ")
            medicamentos = input("Ingrese medicamentos recetados separados por una coma: ").split(",")
            try:
                clinica.emitir_receta(dni, matricula, [m.strip() for m in medicamentos])
                print("se emitio la receta y se agrego a la historia clinica")
            except PacienteNoExisteError:
                print("el paciente no se encuentra")
            except MedicoNoExisteError:
                print("el medico no se encuentra")
        elif opcion == "5":
            dni = input("DNI del paciente: ")
            historia = clinica.obtener_historia_clinica(dni)
            if historia:
                print(historia)
            else:
                print("no se pudo encontrar la historia clinica para ese paciente.")
        elif opcion == "6":
            for turno in clinica.turnos:
                print(f"paciente: {turno.paciente.nombre}, medico: {turno.medico.nombre}, fecha y hora: {turno.fecha_hora}")
        elif opcion == "7":
            if not clinica.pacientes:
                print("no hay pacientes registrados")
            for p in clinica.pacientes.values():
                print(f"DNI: {p.dni}, nombre: {p.nombre}")
        elif opcion == "8":
            if not clinica.medicos:
                print("no hay medicos registrados.")
            for m in clinica.medicos.values():
                print(f"matricula: {m.matricula}, nombre: {m.nombre}, especialidad: {m.especialidad}")
        elif opcion == "9":
            print("chau")
            break
        else:
            print("opcion invalida")

if __name__ == "__main__":
    menu()