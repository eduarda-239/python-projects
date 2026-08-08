# ==========================================
# DESAFIOS - CLASSES
# ==========================================


# ------------------------------------------
# QUESTÕES 1, 2 e 3 - ContaBancaria
# ------------------------------------------

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False

    def __str__(self):
        return f"Titular: {self.titular} | Saldo: {self.saldo}"

    def ativar_conta(self):
        self._ativo = True


# Criando duas instâncias
conta1 = ContaBancaria("João", 199)
conta2 = ContaBancaria("Maria", 234)

print(conta1)
print(conta2)

# Testando ativação da conta
conta3 = ContaBancaria("Carlos", 200)

print(f"Antes de ativar: Conta ativa? {conta3._ativo}")

conta3.ativar_conta()

print(f"Depois de ativar: Conta ativa? {conta3._ativo}")


# ------------------------------------------
# QUESTÃO 4 - Refatoração com @property
# ------------------------------------------

class ContaBancariaPythonica:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

    def ativar_conta(self):
        self._ativo = True

    def __str__(self):
        return f"Titular: {self.titular} | Saldo: {self.saldo}"


# ------------------------------------------
# QUESTÃO 5 - Acessando a propriedade titular
# ------------------------------------------

conta4 = ContaBancariaPythonica("Fernanda", 1500)

print(f"Titular da conta 4: {conta4.titular}")


# ------------------------------------------
# QUESTÃO 6 - ClienteBanco
# ------------------------------------------

class ClienteBanco:
    def __init__(self, nome, idade, endereco, cpf, profissao):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.profissao = profissao

    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancariaPythonica(titular, saldo_inicial)
        return conta


# Criando três clientes
cliente1 = ClienteBanco(
    "Ana",
    30,
    "Rua A",
    "123.456.789-01",
    "Backend"
)

cliente2 = ClienteBanco(
    "Luiza",
    25,
    "Rua B",
    "987.654.321-01",
    "Estudante"
)

cliente3 = ClienteBanco(
    "Vinny Neves",
    40,
    "Rua C",
    "111.222.333-44",
    "Frontend"
)