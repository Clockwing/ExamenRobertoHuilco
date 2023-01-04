# 3 herencia simple
#Padre
class Categoria:
  idCategoria     = int
  nombreCategoria = str
  
  def __init__(self, idCategoria, nombreCategoria):
    self.idCategoria     = idCategoria
    self.nombreCategoria = nombreCategoria
  
  #Hijo
class Producto1(Categoria):
  idProducto     = int
  nombreProducto = str
  def __init__(self, idCategoria, nombreCategoria, idProducto, nombreProducto):
    super().__init__(idCategoria, nombreCategoria)
    self.idProducto     = idProducto
    self.nombreProducto = nombreProducto
    
    #metodo str
    
  def __str__(self):
    return  f'El id de su categoria es: {self.idCategoria} , el nombre de su categoria es {self.nombreCategoria} , el id de su producto es {self.idProducto} , el nombre de su producto es {self.nombreProducto}'

if __name__=="__main__":
  
  Herenciasimple = Producto1(14, "Lacteo", 15, "Leche")
  print(Herenciasimple)
  