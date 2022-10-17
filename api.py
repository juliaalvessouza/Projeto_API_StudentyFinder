from distutils import core
from fastapi import FastAPI, Body
from fastapi.encoders import *
import motor.motor_asyncio
from bson.objectid import ObjectId
from model import *

# variavel de conexão com mongo
mongo_atlas = ""

# variavel para fastapi 
app = FastAPI()

# realizando a conexão
cliente = motor.motor_asyncio.AsyncIOMotorClient(mongo_atlas)
banco = cliente.api
colecao_studenty = banco.get_collection("studentFinder")

# convertendo para um dicionário em python 
def convert_student(student) -> dict:
    return {
        "id": str(student["_id"]),
        "name": student["name"],
        "email": student["email"],
        "interest": student["interest"]
    }

def convert_university(university) -> dict:
    return {
        "id": str(university["_id"]),
        "name": university["name"],
        "address": university["address"]
    }   

def convert_courses(courses) -> dict:
    return {
        "id": str(courses["_id"]),
        "name": courses["name"],
        "area": courses["area"],
        "university": courses["university"]
    }
 
def convert_ads(ads) -> dict:
    return {
        "id": str(ads["_id"]),
        "total_students": ads["total_students"],
        "content": ads["content"],
        "courses": ads["courses"]
    }

def convert_email(email) -> dict:
    return {
        "id": str(email["_id"]),
        "student": email["student"],
        "ads": email["ads"]
    }


# funções que está fazendo as funções dos produtos que estão no mongo..

async def obter_studenty_interest(interest: str) -> dict:
    studenty = await colecao_studenty.find_one({"_interest": ObjectId(interest)})
    if studenty:
        return convert_student(studenty)    








# implementando as rotas
@app.get("/student/{interest}")
async def retorna_um_estudante_por_interesse(interest: str):
    student = await obter_studenty_interest(interest)
    if student:
        return student
    else:
        return {"status": "Not Found"}

