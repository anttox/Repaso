import sys
import getopt

# Clase para representar un proceso
class Process:
    def __init__(self, instructions):
        self.instructions = instructions  # Lista de instrucciones del proceso
        self.current_instruction = 0  # Índice de la instrucción actual
        self.completed = False  # Indicador de si el proceso ha terminado

    def execute_instruction(self):
        if self.current_instruction < len(self.instructions):
            instruction = self.instructions[self.current_instruction]
            self.current_instruction += 1
            return instruction
        else:
            self.completed = True
            return None

# Clase para representar la CPU
class CPU:
    def __init__(self):
        self.current_process = None  # Proceso actual que está ejecutando la CPU
        self.time = 0  # Tiempo total de la CPU
        self.idle_time = 0  # Tiempo en que la CPU está inactiva

    def run(self, processes, switch_on_io, switch_on_end, io_run_immediate):
        # Ejecuta los procesos hasta que todos estén completados
        while not all(process.completed for process in processes):
            # Selecciona el siguiente proceso si no hay proceso actual o si el proceso actual ha terminado
            if self.current_process is None or self.current_process.completed:
                self.current_process = next((p for p in processes if not p.completed), None)

            if self.current_process:
                # Ejecuta la siguiente instrucción del proceso actual
                instruction = self.current_process.execute_instruction()
                if instruction is not None:
                    if instruction == 'CPU':
                        self.time += 1  # Incrementa el tiempo de la CPU
                    elif instruction == 'IO':
                        if switch_on_io:
                            self.current_process = None  # Cambia de proceso si está esperando E/S
                        if io_run_immediate:
                            self.current_process = None  # Cambia de proceso inmediatamente después de E/S
                else:
                    if switch_on_end:
                        self.current_process = None  # Cambia de proceso al final de la ejecución
            else:
                self.idle_time += 1  # Incrementa el tiempo inactivo de la CPU
                self.time += 1

        return self.time, self.idle_time

# Función para analizar la lista de procesos
def parse_process_list(process_list_str):
    processes = []
    for process_str in process_list_str.split(','):
        instructions = []
        parts = process_str.split(':')
        count = int(parts[0])
        instruction = parts[1]
        instructions.extend([instruction] * count)
        processes.append(Process(instructions))
    return processes

# Función principal
def main(argv):
    process_list_str = ""
    switch_on_io = False
    switch_on_end = False
    io_run_immediate = False

    # Análisis de los argumentos de la línea de comandos
    try:
        opts, args = getopt.getopt(argv, "l:S:I:")
    except getopt.GetoptError:
        print('process-run.py -l <process_list> -S <switch_mode> -I <io_mode>')
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-l':
            process_list_str = arg
        elif opt == '-S':
            if arg == 'SWITCH ON IO':
                switch_on_io = True
            elif arg == 'SWITCH ON END':
                switch_on_end = True
        elif opt == '-I':
            if arg == 'IO RUN IMMEDIATE':
                io_run_immediate = True

    # Creación de los procesos a partir de la lista
    processes = parse_process_list(process_list_str)
    cpu = CPU()
    
    # Ejecución de los procesos en la CPU
    total_time, idle_time = cpu.run(processes, switch_on_io, switch_on_end, io_run_immediate)
    
    # Impresión de los resultados
    print(f"Total time: {total_time}")
    print(f"Idle time: {idle_time}")
    print(f"CPU utilization: {(total_time - idle_time) / total_time * 100:.2f}%")

if __name__ == "__main__":
    main(sys.argv[1:])

