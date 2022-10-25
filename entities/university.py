from db import *
from convert import *
from bson.objectid import ObjectId

#conectar collection
collectionUniversity = database().get_collection("university")

async def findAllUniversity() -> dict:
    list = []
    university = collectionUniversity.find()
    async for i in university:
        list.append(convert_university(i))
    return list 

async def findUniversityById(id: str) -> dict:
    university = await collectionUniversity.find_one({"_id": ObjectId(id)})
    if university:
        return convert_university(university)
        

async def createUniversity(data: dict) -> dict:
    university = await collectionUniversity.insert_one(data)
    new = await collectionUniversity.find_one({"_id": university.inserted_id})  
    return convert_university(new)

async def UpdateUniversity(id: str, data: dict):
    university = await collectionUniversity.find_one({"_id": ObjectId(id)})
    if university:
        university_updated = await convert_university.update_one(
            {"_id": ObjectId(id)},
            {"$set": data}
        )
        if university_updated:
            return True
        return False

async def DeleteUniversity(id: str):
    university = await collectionUniversity.find_one({"_id": ObjectId(id)})
    if university:
        await collectionUniversity.delete_one({"_id": ObjectId(id)})
        return True