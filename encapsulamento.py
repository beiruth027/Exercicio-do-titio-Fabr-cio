#Encapsulamento é a proteção dos atributos ou métodos de uma classe, em Python existem somente o public e o private e eles são definidos no próprio nome do atributo ou método.
#Atributos ou métodos iniciados por no máximo dois sublinhados e terminados por um sublinhado são privados e todas as
#outras formas são públicas.

class ContaBancaria:
    def _init_(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor
        print(f"Depósito de {valor} realizado. Saldo atual: {self.__saldo}")

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            print(f"Saque de {valor} realizado. Saldo atual: {self.__saldo}")
        else:
            print("Saldo insuficiente.")

    def exibir_saldo(self):
        print(f"Saldo atual da conta: {self.__saldo}")

    def get_titular(self):
        return self.__titular

    def set_titular(self, novo_titular):
        self.__titular = novo_titular


# Exemplo de uso
conta = ContaBancaria("João", 1000)
conta.depositar(500)
conta.sacar(200)
conta.exibir_saldo()

titular_atual = conta.get_titular()
print(f"Titular atual da conta: {titular_atual}")

conta.set_titular("Maria")
titular_atualizado = conta.get_titular()
print(f"Titular atualizado da conta: {titular_atualizado}")