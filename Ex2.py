class ContaBancária:
    def __init__(self, numero_conta, titular, saldo_inicial=0.0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor} realizado com sucesso.')
        else:
            print('Valor de depósito deve ser maior que zero.')

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f'Saque de R${valor} realizado com sucesso.')
            else:
                print('Saldo insuficiente para o saque.')
        else:
            print('Valor de saque deve ser maior que zero.')

    def mostrar_saldo(self):
        print(f'Saldo atual da conta {self.numero_conta}: R${self.saldo}')

#Exemplo de conta
conta = ContaBancária(12345, "João", 1000)
conta.mostrar_saldo()  
conta.depositar(500)  
conta.sacar(200)  
conta.mostrar_saldo() 

        