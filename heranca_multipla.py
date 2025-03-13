class Animal:
   def __init__(self, nro_patas):
       self.nro_patas = nro_patas

       #Esquema str
   def __str__(self):
       return f"{self.__class__.__name__}: {', '.join
       ([f'{chave} = {valor}' for chave, valor in self.
       __dict__.items()])}"
       

class Mamifero(Animal):
   def __init__(self, cor_pelo, **kw):
       self.cor_pelo = cor_pelo
       super().__init__(**kw)

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
       super().__init__(**kw)
 

class Gato(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
   def __init__(self, cor_bico, cor_pelo, nro_patas):
       print(Ornitorrinco.__mro__)
       super().__init__(cor_bico=cor_bico, cor_pelo=cor_pelo, nro_patas=nro_patas)

#Instanciando
# gato = Gato(4, "Preto")
# print(gato)

ornitorrinco = Ornitorrinco(nro_patas=4, cor_pelo="Vermelho", cor_bico="Laranja")
print(ornitorrinco)

