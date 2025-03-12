class Animal:
   def __init__(self, nro_patas):
       self.nro_patas = nro_patas

class Mamifero(Animal):
   def __init__(self, nro_patas):
       self.nro_patas = nro_patas

class Ave(Animal):
    def __init__(self, nro_patas):
       self.nro_patas = nro_patas

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    pass