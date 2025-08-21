from fastapi import APIRouter, HTTPException
from pydantic import BaseModel #Hay que importarlo para definir usuarios

router = APIRouter(prefix="/users", #Con prefix le indicamos la posición inicial del router
                    tags=["users"], #Con tag marcas un punto en la documentación
                    responses={404: {"message":"No Encontrado"}}) #Con responses podemos indicar el mensaje y el error que mostramos si hay un error)

# python -m uvicorn users:app --reload <--- para inicializar el servidor

#Entidad Usuario
class User(BaseModel):
    id:int
    name:str
    surname:str
    age:int
    url:str

users_list = [User(id=0,name="Juan",surname="Risueño",age=45,url="https://mouredev.com/python"),
                User(id=1,name="Tina",surname="Navarro",age=47,url="https://mouredev.com/redes"),
                User(id=2,name="Jon",surname="Risueño",age=19,url="https://mouredev.com/JS"),
                User(id=3,name="Noa",surname="Risueño",age=11,url="https://mouredev.com/BlackPink")]

'''@app.get("/usersjson") 
async def usersjson():
    return [{"name":"Juan","surname":"Risueño","age":45,"url":"https://mouredev.com/python"},
            {"name":"Tina","surname":"Navarro","age":47,"url":"https://mouredev.com/redes"},
            {"name":"Jon","surname":"Risueño","age":19,"url":"https://mouredev.com/JS"},
            {"name":"Noa","surname":"Risueño","age":11,"url":"https://mouredev.com/BlackPink"}]

@app.get("/user/{id}") #Creamos una petición para un usuario en concreto - llamando por path
async def user(id:int):
    users = filter(lambda user:user.id==id,users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}
    
@app.get("/userquery") #Creamos una petición para un usuario en concreto - llamando por query
async def user(id:int):
    users = filter(lambda user:user.id==id,users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}
'''

@router.get("/") #Así creamos petición para una lista de usuarios
async def users():
    return users_list

def search_user(id: int):
    users = filter(lambda user:user.id==id,users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}

#Path
@router.get("/{id}")
async def user(id: int):
    return search_user(id)

#Query
@router.get("/")
async def user(id: int):
    return search_user(id)

### Crear Usuarios
@router.post("/", response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    users_list.append(user)
    return user

### Actualizar o modificar Usuarios
@router.put("/")
async def user(user:User):
    found = False
    for index, saved_user in enumerate(users_list): # enumerate agrega un contador a un iterable, como una lista o un string y devuelve un objeto que genera pares de índices y valores.
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error":"No se ha actualizado el usuario ya que no se ha encontrado"}
    
    return user

### Borrar Usuarios
@router.delete("/{id}")
async def user(id:int):
    found = False
    for index, saved_user in enumerate(users_list): # enumerate agrega un contador a un iterable, como una lista o un string y devuelve un objeto que genera pares de índices y valores.
        if saved_user.id == id:
            del users_list[index]
            found = True
    
    if not found:
        return {"error":"No se ha borrado el usuario ya que no se ha encontrado"}
    
    return user