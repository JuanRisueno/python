from fastapi import FastAPI
from pydantic import BaseModel #Hay que importarlo para definir usuarios
app = FastAPI()

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


@app.get("/users") #Así creamos petición para una lista de usuarios
async def users():
    return users_list

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

def search_user(id: int):
    users = filter(lambda user:user.id==id,users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}

#Path
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)

#Query
@app.get("/user/")
async def user(id: int):
    return search_user(id)