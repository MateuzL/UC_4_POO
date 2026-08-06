class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial  # atributo privado

    def get_saldo(self):
        return self.__saldo

    def set_depositar(self, valor): 
        if valor > 0:
            self.__saldo += valor
            print(f"O valor de R$ {valor} foi depositado na sua conta.")
        else:
            print("O valor não pode ser menor que ZERO")

conta1 = ContaBancaria("Wander", 200)
print(f"Titular da conta: {conta1.titular}")
#print(f"Saldo da conta: R$ {conta1.get__saldo():.2f}")
print(f"saldo da conta: R$ {conta1.get_saldo()}")
conta1.set_depositar(1000)
print(f"O novo saldo da conta é: R$ {conta1.get_saldo()}")