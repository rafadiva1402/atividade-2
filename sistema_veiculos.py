# sistema_veiculos.py

# Classe base
class Veiculo:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    def acelerar(self):
        print(f"{self.modelo} está acelerando.")

    def realizar_manutencao(self):
        print(f"{self.modelo} está em manutenção genérica.")

# Subclasse - Carro
class Carro(Veiculo):
    def acelerar(self):
        print(f"{self.modelo} acelera rapidamente.")

    def realizar_manutencao(self):
        print(f"{self.modelo} faz troca de óleo e revisão básica.")

# Subclasse - Caminhão
class Caminhao(Veiculo):
    def acelerar(self):
        print(f"{self.modelo} acelera lentamente devido ao peso.")

    def realizar_manutencao(self):
        print(f"{self.modelo} passa por manutenção pesada de motor e freios.")

# Subclasse - Moto
class Moto(Veiculo):
    def acelerar(self):
        print(f"{self.modelo} acelera com agilidade.")

    def realizar_manutencao(self):
        print(f"{self.modelo} faz revisão de freios e corrente.")

# Testando
veiculos = [
    Carro("Fiat Argo", 2021),
    Caminhao("Volvo FH", 2020),
    Moto("Honda CG", 2022)
]

for v in veiculos:
    print(f"Veículo: {v.modelo}, Ano: {v.ano}")
    v.acelerar()
    v.realizar_manutencao()
    print("-" * 30)
