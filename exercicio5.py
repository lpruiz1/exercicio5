class Veiculo:
    veiculos_cadastrados = []
    quantidade_veiculos = 0
    
    def __init__(self, nome:str, ano:int, diaria:float):
        self.__nome = nome
        self.__ano = ano
        self.__diaria = diaria
        Veiculo.veiculos_cadastrados.append(self)
        Veiculo.calcula_quantidade()
    
    def calcula_aluguel(self, dias):
        aluguel_total = self.__diaria * dias
        if dias > 7:
            desconto = 0.10
            aluguel_total *= (1 - desconto)
        return aluguel_total
    
    @classmethod
    def calcula_quantidade(cls):
        cls.quantidade_veiculos = len(Veiculo.veiculos_cadastrados)
        
    @classmethod
    def aumento_percentual(cls, veiculos:list, porcentagem:float):
        for veiculo in veiculos:
            valor_total = veiculo.diaria * (1 + porcentagem)
            veiculo.diaria = valor_total
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def diaria(self):
        return self.__diaria
    
    @nome.setter
    def nome(self, novo_nome:str):
        if type(novo_nome) != str:
            print('Nome inválido.')
        else:
            self.__nome = novo_nome
     
    @ano.setter       
    def ano(self, novo_ano:int):
        if novo_ano < 0:
            print('Ano inválido.')
        else:
            self.__ano = novo_ano
            
    @diaria.setter
    def diaria(self, nova_diaria:float):
        if nova_diaria < 0:
            print('Valor inválido.')
        else:
            self.__diaria = nova_diaria
            
    

class Carro(Veiculo):
    def __init__(self, nome:str, ano:int, diaria:float, combustivel:str):
        Veiculo.__init__(self, nome, ano, diaria)
        self.combustivel = combustivel
        
    def calcula_aluguel(self, dias:int, cupom = 0):
        aluguel_total = super().calcula_aluguel(dias)
        aluguel_total -= cupom
        return aluguel_total
    
        
    
    
class Motocicleta(Veiculo):
    def __init__(self, nome:str, ano:int, diaria:float, combustivel:str, cilindrada:int):
        Veiculo.__init__(self, nome, ano, diaria)
        self.combustivel = combustivel
        self.cilindrada = cilindrada
        
    def calcula_aluguel(self, dias:int, cupom = 0):
        aluguel_total = super().calcula_aluguel(dias)
        taxa = 0
        if self.cilindrada > 200:
            taxa = 0.10
        aluguel_total *= (1 + taxa)
        aluguel_total -= cupom
        return aluguel_total  
    

if __name__ == "__main__":
    menu = """
    *-*-*-*-* ALUGUEL DE VEÍCULOS *-*-*-*-*
    
           1 - Cadastrar veículo
           2 - Calcular aluguel
           3 - Aplicar aumento percentual nas diarias
           4 - Quantidade de veículos cadastrados
           5 - Listar veículos cadastrados
           6 - Sair
    """
    
    while True:
        print(menu)
        escolha = int(input("Digite a sua opção: "))
        match(escolha):
            case 1:
                veiculo = int(input("Que tipo de veículo você deseja cadastrar ?\n1 - Carro\n2 - Motocicleta\n: "))
                match(veiculo):
                    case 1:
                        nome = input("Digite o nome do carro: ")
                        ano = int(input("Digite o ano do carro: "))
                        diaria = float(input("Digite o valor da diária para esse carro: "))
                        combustivel = input("Digite o tipo de combustível desse carro: ")
                        carro = Carro(nome, ano, diaria, combustivel)
                        print(f"\n{carro.nome} cadastrado com sucesso!")
                    case 2:
                        nome = input("Digite o nome da motocicleta: ")
                        ano = int(input("Digite o ano da motocicleta: "))
                        diaria = float(input("Digite o valor da diária para essa motocicleta: "))
                        combustivel = input("Digite o tipo de combustível dessa motocicleta: ")
                        cilindrada = int(input("Digite a cilindrada da motocicleta(somente números): "))
                        motocicleta = Motocicleta(nome, ano, diaria, combustivel, cilindrada)
                        print(f"\n{motocicleta.nome} cadastrado com sucesso!")
                    case _:
                        print("Opção inválida.")
            case 2:
                nome = input("Digite o nome do veiculo que deseja calcular o aluguel: ")
                encontrado = False
                for veiculo in Veiculo.veiculos_cadastrados:
                    if nome == veiculo.nome:
                        dias = int(input("Digite a quantidade de dias que o veículo será alugado: "))
                        aplica_cupom = int(input("Aplicar cupom de redução de custo ?(1 - Sim, 2 - Não): "))
                        if aplica_cupom == 1:
                            cupom = float(input("Digite o valor do cupom em R$: "))
                            valor_aluguel = veiculo.calcula_aluguel(dias, cupom)
                        else:
                            valor_aluguel = veiculo.calcula_aluguel(dias)
                        print(f"Valor do aluguel: R${valor_aluguel:.2f}")
                        encontrado = True
                if not encontrado:
                    print("Veículo não encontrado.")
            case 3:
                percentual = float(input("Quantos % vc deseja aumentar ?: "))
                percentual /= 100
                Veiculo.aumento_percentual(Veiculo.veiculos_cadastrados, percentual)
                print("Percentuais aumentados: ")
                for veiculo in Veiculo.veiculos_cadastrados:
                    print(f"{veiculo.nome}: {veiculo.diaria:.2f}\n")
            case 4:
                print(f"Quantidade: {Veiculo.quantidade_veiculos}")
            case 5:
                for veiculo in Veiculo.veiculos_cadastrados:
                    print(f"Nome: {veiculo.nome}\nAno: {veiculo.ano}\nDiaria: {veiculo.diaria:.2f}\n")
            case 6:
                print("Encerrando sistema...")
                break
            case _:
                print("Opção inválida.")