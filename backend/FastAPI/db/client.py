from pymongo import MongoClient

#db_client = MongoClient().local #Conexión BBDD Local

#Base de Datos Remota
#Usamos MongoDB Atlas en esta irl: https://cloud.mongodb.com/v2/68b6a73ee3b548170bc225a0#/metrics/replicaSet/68b9527d0b9494308dbb0d24/explorer/test/users/find
#Usuario: Johnyrisu Password: test
db_client = MongoClient("mongodb+srv://JohnyRisu:test@cluster0.7l8a6dc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0").test