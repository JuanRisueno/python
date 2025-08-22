from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel #Hay que importarlo para definir usuarios
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm    #OAuth2PasswordBearer se encarga de autenticar usuarios/contraseña
                                                                                #OAuth2PasswordRequestForm es lo que usa el backend para recibir el usuario/contraseña desde el cliente y comprobarlo con la BBDD

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl = "login") #Creamos la instancia para OAuth2PasswordBearer. Además tiene que tener un token como parámetro. Este token será el que valide o no la autenticación en el sistema.

class User(BaseModel):
    username:str
    full_name:str
    email:str
    disabled:bool

class UserDB(User):
    password: str #UserDB tiene todos los campos de User más password

users_db = {
    "JohnyRisu":{
        "username": "JohnyRisu",
        "full_name": "Juan Risueño",
        "email": "risu.profesional@gmail.com",
        "disabled": False,
        "password":"123456"
    },
    "MoureDev":{
        "username": "MoureDev",
        "full_name": "Brais Moure",
        "email": "braismoure@mouredev.com",
        "disabled": True,
        "password":"654321"
    }
}

def search_user_db(username: str): #Esta función la vamos a usar para conseguir el token de autenticación.Tenemos que meter como parámetro el username. 
    if username in users_db: #Buscarmos el username en la base de datos de users_db
        return UserDB(**users_db[username]) #nos devuelve el usuario con username de la base de datos users_db como la variable UserDB. Con ** indicamos que le vamos a pasar varios parametros en el post
    
def search_user(username: str): #Esta función la vamos a usar para devolver el usuario SIN LA CONTRASEÑA
    if username in users_db: 
        return User(**users_db[username])
    
async def current_user(token:str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Credenciales de autenticación inválidas", 
            headers={"WWW-Authenticate":"Bearer"})
    
    if user.disabled:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Usuario inactivo")
    
    return user
    
@app.post("/login")
async def login(form:OAuth2PasswordRequestForm = Depends()): #Aquí utilizamos el OAuth2PasswordRequestForm como parámetro para nuestro login. Depends quiere decir que se van a recibir datos, pero no dependen de nadie
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario no es correcto")
    
    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La contraseña no es correcta")
    
    return {"access_token":user.username, "token_type":"bearer"}

@app.get("/users/me")
async def me(user: User = Depends(current_user)): #MUY IMPORTANTE. De los usuarios que tenemos definidos, devolvemos en el get el usuario que NO TIENE la contraseña. POR MOTIVOS DE SEGURIDAD
    return user