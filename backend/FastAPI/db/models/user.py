from pydantic import BaseModel #Hay que importarlo para definir usuarios
from typing import Optional

#Entidad Usuario
class User(BaseModel):
    id: Optional[str] = None #Con None indicamos que este campo es opcional
    username:str
    email:str