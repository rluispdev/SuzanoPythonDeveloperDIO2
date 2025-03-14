class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
     def voar(self):
       super().voar()
    
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa.")

#FIXME:  Exemplo ruim do uso de herança para "ganhar" o metodo voar.
class Aviao(Passaro):
    def voar(self):
        print("Avião voando...")

def plano_de_voo(obj):
    obj.voar()

p1 = Pardal()
p2 = Avestruz()

plano_de_voo(p1)
plano_de_voo(p2)
plano_de_voo(Aviao())