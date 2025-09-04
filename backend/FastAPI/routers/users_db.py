### Users DB API ###

from fastapi import APIRouter, HTTPException, status
from db.models.user import User #Importamos la entidad User del directorio db/models/user.py
from db.client import db_client
from db.schemas.user import user_schema, users_schema
from bson import ObjectId

router = APIRouter(prefix="/userdb", 
                    tags=["userdb"], 
                    responses={status.HTTP_404_NOT_FOUND: {"message":"No Encontrado"}}) 

users_list = []

def search_user(field: str, key):
    try:
        user = db_client.users.find_one({field:key})
        return User(**user_schema(user))
    except:
        return {"error":"No se ha encontrado el usuario"}
    
### Crear Usuarios
@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user: User):

    if type(search_user("email", user.email)) == User:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El usuario ya existe")
    
    user_dict = dict(user) #Transformarmos el usuario en un diccionario
    del user_dict["id"] #Borramos el campo id ya que es autogenerado por MongoDB. Este campo no interesa traerlo al servidor

    id = db_client.users.insert_one(user_dict).inserted_id #Conexión a la base de datos en local para insertar usuarios
    
    new_user = user_schema(db_client.users.find_one({"_id":id})) #La clave única que crea MongoDB por defecto es _id
    
    return User(**new_user)

### Lista de usuarios
@router.get("/", response_model=list[User])
async def users():
    return users_schema(db_client.users.find())

### Path
@router.get("/{id}")
async def user(id: str):
    return search_user("_id", ObjectId(id))

### Query
@router.get("/")
async def user(id: str):
    return search_user("_id", ObjectId(id))

### Actualizar o modificar Usuarios
@router.put("/", response_model=User)
async def user(user:User):
    
    user_dict = dict(user)
    del user_dict["id"]

    try:
        db_client.users.find_one_and_replace(
            {"_id":ObjectId(user.id)}, user_dict)
    except:
        return {"error":"No se ha actualizado el usuario"}
    
    return search_user("_id",ObjectId(user.id))

### Borrar Usuarios
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def user(id:str):

    found = db_client.users.find_one_and_delete({"_id":ObjectId(id)})
    if not found:
        return {"error":"No se ha borrado el usuario ya que no se ha encontrado"}
    
    return user