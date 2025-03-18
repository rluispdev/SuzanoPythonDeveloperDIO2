
from abc import ABC, abstractmethod


class ControleRemote(ABC):
    @abstractmethod
    def ligar(self):
        pass

    
    @abstractmethod
    def desligar(self):
        pass


    #Forcar a implementação do método marca
    @property
    @abstractmethod
    def marca(self):
        pass




class ControleTV(ControleRemote):
   def ligar(self):
         print("TV ligada")

   def desligar(self):
           print("Desligando...")     
           print("TV desligada")

   @property
   def marca(self):
        return "Samsung"
        

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

class ControleArCondicionado(ControleRemote):
    def ligar(self):
        print("Ar condicionado ligado")

    def desligar(self):
        print("Desligando...")
        print("Ar condicionado desligado")
    
    @property
    def marca(self):
        return "LG"


controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)

