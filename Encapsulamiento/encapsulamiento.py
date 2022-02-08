# ENCAPSULACION:

# Permite agrupar datos y su comportamiento
# Controla el acceso a dichos datos 
# Previene modificaciones no autorizadas

#Encapsulacion getters and setters EJM 1

class PersonalData:
    def __init__(self,name, surname,age,height,nationality):
        self._name = name
        self._surname = surname
        self._age = age
        self._height = height
        self._nationality = nationality
    
    #Decorador getter  y primer setter para la propiedad name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name

    #Decorador getter y primer setter para la propiedad surname
    @property
    def surname(self):
        return self._surname
    @surname.setter
    def surname(self,surname):
        self._surname = surname
    
    #Decorador getter y primer setter para la propiedad age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,age):
        self._age = age
    
    #Decorador getter y primer setter para la propiedad height
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,height):
        self._height = height

    #Decorador getter y primer setter para la propiedad nationality
    @property
    def nationality(self):
        return self._nationality  
    @nationality.setter
    def nationality(self,nationality):
        self._nationality = nationality


if __name__ == '__main__':
    persona1 = PersonalData("Juanito","Alimaña",29,170,"Colombian")

    persona1.name = input("Ingrese su nombre: ")
    persona1.surname = input("Ingrese su apellido: ")
    persona1.age = int(input("Ingrese la edad: "))
    persona1.height = int(input("Ingrese su estatura: "))
    persona1.nationality = input("Ingrese su nacionalidad: ")

    print("Nombre: "+persona1.name)
    print("Apellido:"+persona1.surname)
    print("Edad: "+str(persona1.age))
    print("Altura: "+str((persona1.height)/100)+" mts")
    print("Nacionalidad :"+persona1.nationality)



#Encapsulacion getters and setters EJM 2

class CasillaDeVotacion:
    
    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        if region in self._pais:
            self._region = region
        else:
            raise ValueError(f'La region {region} no esta en la lista')


casilla = CasillaDeVotacion(123,['Mexico','Morelos'])
print(casilla.region)
casilla.region = 'Mexico'
print(casilla.region)