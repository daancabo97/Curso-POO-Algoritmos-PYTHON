# ABSTRACCION:

 # Es enfocarnos en la informacion relevante, generar una interfaz de cualquier tipo de objeto sin resaltar los detalles tecnicos de como funciona el objeto
 # Ejm: Cuando estoy manejando mi carro no me estoy preocupando de la forma en que funciona el motor, como quema la gasolina o genera el movimiento de los pistones
 # Ejm2: Cuando voy en el ascensor pero no me preocupo por el funcionamiento interno del movimiento que hacen las poleas
 # Ejm3: Cuando hablamos con otras personas no nos estamos preocupando de como funcionan las neuronas de otras personas cuando tratamos de comunicarnos

 #1 Enfocarnos en la informacion relevante

 #2 Separar la informacion central de los detalles secundarios
 
 #3 Podemos utilizar variables y metodos ( privados o publicos)

class Lavadora:
    pass

    def __init__(self):
        pass

    def lavar (self, temperatura='caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._añadir_jabon()
        self._añadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_de_agua(self,temperatura):
       print(f'añadir el tanque con agua : {temperatura}')

    def _añadir_jabon(self):
        print('Añadiendo jabon')

    def _lavar(self):
        print('lavar ropa')

    def _centrifugar(self):
        print('Centrifugando la ropa')

if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()


    