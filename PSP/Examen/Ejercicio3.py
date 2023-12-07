
import subprocess
import time


def abrir_editor():
    # Abre el editor de texto del sistema (en Windows, notepad.exe)
    subprocess.run(['notepad.exe'])

def cambiar_prioridad(pid):
    # Espera 5 segundos para cambiar la prioridad
    time.sleep(5)

    try:
        # Cambia la prioridad del proceso
        subprocess.run(['wmic', 'process', 'where', f'ProcessId={pid}', 'CALL', 'setpriority', '64'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al cambiar la prioridad: {e}")

def matar_proceso(pid):
    # Espera 2 segundos
    time.sleep(2)

    try:
        # Lista los procesos y busca el proceso con el PID especificado
        output = subprocess.check_output(['tasklist']).decode('utf-8')
        for line in output.splitlines():
            if str(pid) in line:
                # Obtiene el nombre del proceso y lo mata
                process_name = line.split()[0]
                subprocess.run(['taskkill', '/f', '/im', process_name], check=True)
                print(f"Proceso {process_name} ha sido terminado.")
                break
    except subprocess.CalledProcessError as e:
        print(f"Error al matar el proceso: {e}")

if __name__ == "__main__":
    # P1: Abre el editor 
    abrir_editor()

    # Espera un momento para asegurarse de que el proceso del editor esté en ejecución
    time.sleep(2)

    # Obtiene el PID del proceso del editor
    pid_editor = None
    try:
        # Busca el PID del proceso del editor
        output = subprocess.check_output(['tasklist', '/FI', 'IMAGENAME eq notepad.exe']).decode('utf-8')
        for line in output.splitlines():
            if 'notepad.exe' in line:
                pid_editor = int(line.split()[1])
                break
    except subprocess.CalledProcessError as e:
        print(f"Error al obtener el PID del editor: {e}")

    if pid_editor is not None:
        # P2: Cambia la prioridad de P1 después de 5 segundos
        cambiar_prioridad(pid_editor)

        # P3: Mata a P1 después de 2 segundos de que P2 haya arrancado
        matar_proceso(pid_editor)



