# Polimorfismo, em Python, é a capacidade que uma subclasse tem de ter métodos com o mesmo nome de sua superclasse,
# e o programa saber qual método deve ser invocado, especificamente (da super ou sub).
#Ou seja, o objeto tem a capacidade de assumir diferentes formas .

#Exemplo de código

class Super:
 def hello(self):
  print("Olá, sou a superclasse!")


class Sub(Super):
 def hello(self):
  print("Olá, sou a subclasse!")


teste = Sub()
teste.hello()

#Outro exemplo de código


class Forma:
 def calcular_area(self):
  pass


class Retangulo(Forma):
 def _init_(self, comprimento, largura):
  self.comprimento = comprimento
  self.largura = largura

 def calcular_area(self):
  return self.comprimento * self.largura


class Circulo(Forma):
 def _init_(self, raio):
  self.raio = raio

 def calcular_area(self):
  return 3.14 * self.raio ** 2


formas = [Retangulo(5, 10), Circulo(7)]

for forma in formas:
 print(forma.calcular_area())
