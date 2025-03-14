class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
    @classmethod
    def criar_apartir_de_ano_nascimento(cls, nome, mes, dia, ano_nascimento):
        idade = 2025 - ano_nascimento
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_de_idade(idade):
        return idade >= 18


p2 = Pessoa.criar_apartir_de_ano_nascimento("Maria",  12, 3, 1994)
print(p2.nome, p2.idade)


print(Pessoa.e_maior_de_idade(17))
print(Pessoa.e_maior_de_idade(18))
print(Pessoa.e_maior_de_idade(19))