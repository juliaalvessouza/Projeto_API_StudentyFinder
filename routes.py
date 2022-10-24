from fastapi import FastAPI, Body
from fastapi.encoders import *
from entities.ads import createAds
from model import *
from entities.student import *
from entities.university import *
from entities.ads import *

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

#ads
@app.get("/ads")
async def getAllAds():
    ads = await findAllAds()
    if ads:
        return ads
    else:
        return {"status": "Not Found"}

@app.get("/ads/{id}")
async def getAdsById(id: str):
    data = await findAdsById(id)
    if data:
        return data
    else:
        return {"status": "Not Found"}

@app.post("/ads")
async def postUniversity(ads : Ads = Body(...)):
    data = jsonable_encoder(ads)
    new = await createAds(data)
    return new
