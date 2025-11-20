# Classes Aninhadas em Python
# Exemplo: Classe Computador com classes aninhadas GPU e CPU

class Computador:  # Classe principal
    def __init__(self, modelo, gpu_nome, gpu_memoria, cpu_nome=None, cpu_cores=None, cpu_clock=None):
        self.modelo = modelo  # Atributo do computador
        # Instancia a classe aninhada GPU
        self.gpu = self.GPU(gpu_nome, gpu_memoria)
        
        # Instancia a classe aninhada CPU (opcional)
        if cpu_nome and cpu_cores and cpu_clock:
            self.cpu = self.CPU(cpu_nome, cpu_cores, cpu_clock)
        else:
            self.cpu = None

    def mostrar_configuracao(self):
        print(f"\nComputador Modelo: {self.modelo}")
        self.gpu.mostrar_gpu()
        if self.cpu:
            self.cpu.mostrar_cpu()
        else:
            print("CPU: Não configurada")

    # Classe aninhada GPU
    class GPU:
        def __init__(self, nome, memoria_gb):
            self.nome = nome
            self.memoria_gb = memoria_gb

        def mostrar_gpu(self):
            print(f"GPU: {self.nome}, Memória: {self.memoria_gb}GB")

    # Classe aninhada CPU
    class CPU:
        def __init__(self, nome, cores, clock_ghz):
            self.nome = nome
            self.cores = cores
            self.clock_ghz = clock_ghz

        def mostrar_cpu(self):
            print(f"CPU: {self.nome}, Cores: {self.cores}, Clock: {self.clock_ghz}GHz")


# -----------------------
# Parte de utilização da classe
# -----------------------

# Criar um computador completo (com GPU e CPU)
pc1 = Computador(
    "Dell XPS",           # Modelo
    "NVIDIA RTX 3080",    # GPU nome
    10,                   # GPU memória
    "Intel i9-12900K",    # CPU nome
    16,                   # CPU cores
    3.7                   # CPU clock GHz
)

pc1.mostrar_configuracao()

# Criar um computador apenas com GPU (sem CPU configurada)
pc2 = Computador(
    "MacBook Air",
    "Apple M1 GPU",
    8
)

pc2.mostrar_configuracao()
