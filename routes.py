from fastapi import FastAPI, Body
from fastapi.encoders import *
from model import *
from entities.student import *
from entities.university import *

app = FastAPI()


# students
@app.get("/student/{interest}")
async def getStudentByInterest(interest: str):
    student = await findStudentByInterest(interest)
    if student:
        return student
    else:
        return {"status": "Not Found"}

#university
@app.get("/university")
async def getAllUniversity():
    university = await findAllUniversity()
    if university:
        return university
    else:
        return {"status": "Not Found"}

@app.get("/university")
async def getAllUniversity():
    university = await findAllUniversity()
    if university:
        return university
    else:
        return {"status": "Not Found"}


@app.get("/university/{id}")
async def getUniversityById(id: str):
    data = await findUniversityById(id)
    if data:
        return data
    else:
        return {"status": "Not Found"}

@app.post("/university")
async def postUniversity(university : University = Body(...)):
    data = jsonable_encoder(university)
    new = await createUniversity(data)
    return new