from fastapi import FastAPI

app = FastAPI() #Instanciamos FastAPI

@app.get("/") #Se hace una petición al servidor. get forma parte de las operaciones http
async def root():   #Una operación asíncrona es aquella que no bloquea la ejecución del programa principal mientras espera que se complete una tarea de larga duración
                    #Orientado a un Backend, piensa que a lo mejor hay muchas personas conectadas al mismo Backend. Con lo que petición se resolverá cuando se pueda. Pero mientras el programa no se detiene.
    return "¡Hola FastAPI!"

# python -m uvicorn main:app --reload <--- Así he conseguido levantar el servidor ya que con el comando del vídeo: uvicorn main:app --reload me daba error en Windows. Seguramente es el comando para usar en Linux.
# El servidor se detiene con ctrl+C

@app.get("/url") 
async def url():
    return {"url_curso":"https://mouredev.com/python"}

# Documentación en Swagger: http://127.0.0.1:8000/docs
# Documentación en ReDocly: http://127.0.0.1:8000/redoc

