class Veiculo: 
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def ligar_motor(self):
        print("Motor ligado!")

class Motocicleta(Veiculo):
    def __init__(self, marca, modelo, ano, cor, cilindradas):
        super().__init__(marca, modelo, ano, cor)
        self.cilindradas = cilindradas

    def ligar_motor(self):
        print("Motor da motocicleta ligado!")

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor, potencia):
        super().__init__(marca, modelo, ano, cor)
        self.potencia = potencia

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, cor, carga):
        super().__init__(marca, modelo, ano, cor)
        self.carga = carga

    def ligar_motor(self):
        print("Motor do caminhão ligado!")

    def esta_carregado(self):
        print(f"{'Sim' if self.carga else 'Não'} está carregado")

moto = Motocicleta("Honda", "CB 500", 2020, "Vermelha", 500)
moto.ligar_motor()

carro = Carro("Fiat", "Uno", 2019, "Branco", 1.0)
carro.ligar_motor()

caminhao = Caminhao("Volvo", "FH 540", 2020, "Branco", 49)
caminhao.ligar_motor()
caminhao.esta_carregado()
cam = Caminhao("Volvo", "FH 540", 2020, "Azul", 0)
cam.esta_carregado()