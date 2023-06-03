#A Herança é um conceito do paradigma da orientação à objetos que determina que uma classe (filha)
# pode herdar atributos e métodos de uma outra classe (pai) e, assim, evitar que haja muita repetição de código.
#Exemplo de código:

class ContaBancaria:
    def _init_(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de {valor} realizado. Saldo atual: {self.saldo}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de {valor} realizado. Saldo atual: {self.saldo}")
        else:
            print("Saldo insuficiente.")

    def exibir_saldo(self):
        print(f"Saldo atual da conta: {self.saldo}")


class ContaPoupanca(ContaBancaria):
    def _init_(self, titular, saldo, limite_saques):
        super()._init_(titular, saldo)
        self.limite_saques = limite_saques
        self.saques_realizados = 0

    def sacar(self, valor):
        if self.saques_realizados < self.limite_saques:
            super().sacar(valor)
            self.saques_realizados += 1
            print(f"Saques realizados: {self.saques_realizados}/{self.limite_saques}")
        else:
            print("Limite de saques atingido.")

    def exibir_saldo(self):
        super().exibir_saldo()
        print(f"Limite de saques restantes: {self.limite_saques - self.saques_realizados}")



conta = ContaBancaria("João", 1000)
conta.depositar(500)
conta.sacar(200)
conta.exibir_saldo()

poupanca = ContaPoupanca("Maria", 2000, 3)
poupanca.depositar(1000)
poupanca.sacar(500)
poupanca.sacar(300)
poupanca.sacar(400)
poupanca.exibir_saldo()