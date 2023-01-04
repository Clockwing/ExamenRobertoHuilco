from ejercicio6seccion import Seccion
from ejercicio6categoria import Categoria
from ejercicio6producto import Productot

class Venda(Productot):
  tipo     = str
  total    = str
  producto = ("","","")
  def __init__(self, tipo, total, producto):
    self.tipo       = tipo
    self.total      = total
    self.prproducto = producto
    
if __name__=="__main__":
    
 ejercicio5 = Venda("Tarjeta", "20", Productot("Leche", "02-03-2013", Categoria("Lacteo", Seccion(11111, "Pasillo 3"))))
   
 print(vars(ejercicio5))
 print(vars(ejercicio5.prproducto))
 print(vars(ejercicio5.prproducto.categoria))
 print(vars(ejercicio5.prproducto.categoria.seccion))