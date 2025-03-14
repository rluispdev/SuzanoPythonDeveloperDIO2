class Estudante:

    #Atributo de classe
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    
    def __str__(self) -> str:
        return f"Nome: {self.nome} \tMatricula: {self.matricula} \tEscola: {self.escola}"

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno_1 = Estudante("João", 123)
aluno_2 = Estudante("Maria", 456)
print(aluno_1)
print(aluno_2)


mostrar_valores(aluno_1, aluno_2)
Estudante.escola = "IFPI"
aluno_1.matricula = 999

mostrar_valores(aluno_1, aluno_2)