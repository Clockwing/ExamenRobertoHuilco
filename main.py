# 1.-Clase con metodos str
class Vendedor:
  nombre    = str
  apellido  = str
  edad      = int
  
  def __init__(self, nombre, apellido, edad):
    self.nombre   = nombre
    self.apellido = apellido
    self.edad     = edad
    
  def __str__(self):
    return  f'Hola vendedor {self.nombre} {self.apellido}, tu edad es {self.edad}'
  
#2 CREACION DE UNA CLASE QUE CONTENGA UN METODO Y SU OBJETO IMPRESO EJECUTANDO EL METODO.
class Cliente:
  nombre    = str
  apellido  = str
  direccion = str
  
  def __init__(self, nombre, apellido, direccion):
    self.nombre    = nombre
    self.apellido  = apellido
    self.direccion = direccion
    
if __name__=="__main__":
  
  metodostr = Vendedor("Roberto", "Huilco", 24)
  print(metodostr)

