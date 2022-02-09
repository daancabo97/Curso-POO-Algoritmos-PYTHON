# POLIMORFISMO:

# Es la habilidad de tomar varias formas y definirlas de manera distina segun su comportamiento
# En Python, nos permite cambiar el comportamiento de una superclase para adaptarlo a la subclase

            # Herencia: 'copy paste'
            # Polimorfismo: 'edit copy paste'

class Persona:

   def __init__(self, nombre) :
       self.nombre = nombre

   def avanza(self):
       return('Ando caminando')

class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre) 

    def avanza(self):
        return('Ando moviendome en mi bicicleta')


def main():
    persona = Persona('Daniel')
    print(f'{persona.nombre} dice: {persona.avanza()}')
    # persona.avanza()

    ciclista = Ciclista('David')
    print(f'{ciclista.nombre} dice: {ciclista.avanza()}')
    # ciclista.avanza()


if __name__ =='__main__':
    main()


# si usamos otros lenguajes el polimorfismo es algo más complejo,
# pues es cambiar en ejecución la forma del objeto, un ejemplo es 
# en los videojuegos tu llevas un carro pero de la nada quieres cambiar
# a una moto, pues no se crea otra instancia del vehiculo si no se llama
# al polimorfismo para que cambie la forma del objeto es decir que ahora
# en vez de ser un carro va a ser una moto… les dejo un ejemplo aqui abajo.

class Coche():

 	def dezpla(self):
 		print("Voy en 4 ruedas")


class Moto():

 	def dezpla(self):
 		print("Voy en 2 ruedas")



class Camion():

 	def dezpla(self):
 		print("Voy en 6 ruedas")


def dezplazamiento(vechiculo):
 	vechiculo.dezpla()


miVehiculo=Coche()
miVehiculo=Camion()
miVehiculo=Moto()
dezplazamiento(miVehiculo)


