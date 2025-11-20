# Agregation no Python

class Motor:
    def __init__(self, marca, potencia):
        self.marca = marca
        self.potencia = potencia

class Carro:
    def __init__(self):
        self.motores = []
    def adicionar_motor(self, motor):
        self.motores.append(motor)

    def listar_motores(self):
        for motor in self.motores:
            print(f"Motor: {motor.marca}, Potência: {motor.potencia}cv")
    

# Criando motores
motor1 = Motor("V8", 400)
motor2 = Motor("Mustang", 600)
motor3 = Motor("Maverick", 150)
motor4 = Motor("Impala", 250)


# Criando carro e adicionando motores
carro = Carro()
carro.adicionar_motor(motor1)
carro.adicionar_motor(Motor("V6", 300))
carro.adicionar_motor(motor2)
carro.adicionar_motor(motor3)
carro.adicionar_motor(motor4)


# Listando motores do carro
carro.listar_motores()
