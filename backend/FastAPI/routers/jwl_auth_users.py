from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel 
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext #Api para el algoritmo de encriptación
from datetime import datetime, timedelta #para trabajar con tiempos

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1 #1 minuto
SECRET = "d01ed7c42c7fa2b2eeb2048d05e5fb05b7245768a7126754b1e31651320aabeb"

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl = "login")

crypt = CryptContext(schemes=["bcrypt"]) #Algoritmo de encriptación

class User(BaseModel):
    username:str
    full_name:str
    email:str
    disabled:bool

class UserDB(User):
    password: str 

users_db = {
    "JohnyRisu":{
        "username": "JohnyRisu",
        "full_name": "Juan Risueño",
        "email": "risu.profesional@gmail.com",
        "disabled": False,
        "password":"$2a$12$dHloOqWYjRRib3X.ncaJ9uUjSeH2CCUYJz15YsbytOLIItlHseMEm" #He usado https://bcrypt-generator.com/ para generar el código de la contraseña 123456
    },
    "MoureDev":{
        "username": "MoureDev",
        "full_name": "Brais Moure",
        "email": "braismoure@mouredev.com",
        "disabled": True,
        "password":"$2a$12$TxqS7jHLyNM7OVB0nK0x2OirROZ.eLLVbMXCoAx.IuvrOaiussb2a"
    }
}

def search_user_db(username: str): 
    if username in users_db: 
        return UserDB(**users_db[username])
    
def search_user(username: str):
    if username in users_db: 
        return User(**users_db[username])
    
async def auth_user(token:str = Depends(oauth2)):
    exception = HTTPException( #Creamos una variable con la excepción, ya que es un código que vamos a usar varias veces
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Credenciales de autenticación inválidas", 
            headers={"WWW-Authenticate":"Bearer"})

    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub") #Decodificamos el username
        if username is None:
            raise exception
    except JWTError:
        raise exception
    
    return search_user(username)

    
async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Usuario inactivo")
    
    return user

@router.post("/login")
async def login(form:OAuth2PasswordRequestForm = Depends()): 
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario no es correcto")
    
    user = search_user_db(form.username)

    if not crypt.verify (form.password, user.password): #utilizamos el algoritmo de encriptación para comprobar las contraseñas
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La contraseña no es correcta")

    access_token = {"sub":user.username,
                    "exp":datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)} #el tiempo conectado es el momento actual + la duración de la variable ACCESS_TOKEN_DURATION}

    return {"access_token":jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type":"bearer"}

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user