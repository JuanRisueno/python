#MUY IMPORTANTE ... CAMBIAR DE ENTORNO VIRTUAL CON: source .venv/bin/activate ... para descativarlo, sencillamente el comando deactivate

#Crear requeriments.txt: desde el entorno virtual: pip freeze > requeriments.txt
#Instalar dependencias desde requeriments.txt: desde el entorno virtual: pip install -r requeriments.txt
#Pasos para trasladar el proyecto:
#entorno virtual -> creas requeriments.txt --> subes el proyecto a la nube --> Linux --> Bajas --> entorno virtual --> instalas dependencias con pip

#Instalar FastAPI: pip install "fastapi[all]"

from fastapi import FastAPI
from routers import products, users, basic_auth_users, jwl_auth_users, users_db #MUY IMPORTANTE importar todos los routers
from fastapi.staticfiles import StaticFiles #Importar para recursos estáticos


app = FastAPI() #Instanciamos FastAPI

# Routers
app.include_router(products.router) #Así llamamos al router y lo incluimos en nuestra api principal
app.include_router(users.router)
app.include_router(basic_auth_users.router)
app.include_router(jwl_auth_users.router)
app.include_router(users_db.router)


# Recursos Estáticos
app.mount("/static",StaticFiles(directory="static"),name="static")

@app.get("/") #Se hace una petición al servidor. get forma parte de las operaciones http
async def root():   #Una operación asíncrona es aquella que no bloquea la ejecución del programa principal mientras espera que se complete una tarea de larga duración
                    #Orientado a un Backend, piensa que a lo mejor hay muchas personas conectadas al mismo Backend. Con lo que petición se resolverá cuando se pueda. Pero mientras el programa no se detiene.
    return "¡Hola FastAPI!"

# python -m uvicorn main:app --reload <--- Así he conseguido levantar el servidor ya que con el comando del vídeo: uvicorn main:app --reload me daba error en Windows. Seguramente es el comando para usar en Linux.
# El servidor se detiene con ctrl+C

@app.get("/url") 
async def url():
    return {"url_curso":"https://mouredev.com/python"}

# Url Local: http://127.0.0.1:8000
# Url Local: http://127.0.0.1:8000/url
# Documentación en Swagger: http://127.0.0.1:8000/docs
# Documentación en ReDocly: http://127.0.0.1:8000/redoc

