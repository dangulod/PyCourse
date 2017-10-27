class Person:
  
  '''
  La clase persona es un objeto, que tiene 2 atributos (nombre, edad).
  
  Hemos encapsulado el codigo en la clase persona. 
  
  Toda clase tiene un constructor que crea la clase
  '''
  
  # Constructor
  
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
  
  # Metodos (Funciones)
  
  def get_nombre(self):
    return(self.nombre)
  
  def get_edad(self):
    return(self.edad)
  
  def set_edad(self, edad):
    self.edad = edad
  
  def set_nombre(self, nombre):
    self.nombre = nombre
  
  def year(self, ano):
    self.set_edad(self.get_edad() + ano)

