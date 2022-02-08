# HERENCIA:

class Rectangulo:

    def __init__(self, base, altura):              # -> El rectangulo requiere una base y una altura que es ogual a nuestro lado
        self.base = base                           # -> Generar instancia
        self.altura = altura

    def area(self): # HERENCIA                    # Se Genera un metodo en la clase que calcula el area = base * altura
        return self.base * self.altura

class Cuadrado(Rectangulo):

    def __init__(self, lado):                      # -> No se ncesita definir base y altura
        super().__init__(lado, lado)               # -> Generamos un cuadro en donde a su constructor llamamos a super que nos permite tener acceso directo a la super clase: Rectangulo(), declarando ambos lados del cuadrado y llamando el metodo init que es su constructor


if __name__ =='__main__':
    rectangulo = Rectangulo(base=4 , altura=3 )    # -> Se genera un instancia de rectangulo y definimos base y altura
    print(rectangulo.area())                       # -> imprimir el area del rectangulo           

    cuadrado = Cuadrado(lado=5)                    #  -> Se genera un instancia de cuadrado, definir valor del lado , cuando llamamos al rectangulo simplemente con un lado inicializamos tambien una instancia de rectangulo con ambos lados diciendo que la base es igual a 5 
    print(cuadrado.area()) # HERENCIA de area            y la altura es igual a 5 y heredamos el metodo de area para que lo podamos ejecutar directamente en el cuadrado
    