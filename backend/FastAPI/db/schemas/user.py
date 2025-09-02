def user_schema(user) -> dict: #El schema del usuario de MongoDB lo vamos a transformar en un diccionario de python
    return {"id":str(user["_id"]),
            "username":user["username"],
            "email":user["email"]}

def users_schema(users) -> list:
    return [user_schema(user) for user in users]