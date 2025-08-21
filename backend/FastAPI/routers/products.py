from fastapi import APIRouter

router = APIRouter(prefix="/products", #Con prefix le indicamos la posición inicial del router
                    tags=["products"], #Con tag marcas un punto en la documentación
                    responses={404: {"message":"No Encontrado"}}) #Con responses podemos indicar el mensaje y el error que mostramos si hay un error

products_list = ["Producto 1","Producto 2","Producto 3","Producto 4","Producto 5"]

@router.get("/") #Utilizamos solo / ya que tenemos una posición inicial en el prefix
async def products():
    return products_list

@router.get("/{id}") 
async def products(id: int):
    return products_list[id]