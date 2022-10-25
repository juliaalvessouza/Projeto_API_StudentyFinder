from db import *
from convert import *
from bson.objectid import ObjectId

from model import University

#conectar collection
collectionAds = database().get_collection("ads")

async def findAllAds() -> dict:
    list = []
    ads = collectionAds.find()
    async for i in ads:
        list.append(convert_ads(i))
    return list 

async def findAdsById(id: str) -> dict:
    ads =  await collectionAds.find_one({"_id": ObjectId(id)})
    if ads:
        return convert_ads(ads) 

async def findAdsUniversityByName(name: str) -> dict:
    list = []
    # {items: {$elemMatch: {value: {$regex : "text"}}}}
    # ads = collectionAds.find({"university.0.name": name})
    ads = collectionAds.find({"university": {"$elemMatch": {"name": name}}})
    print(ads)
    if ads:
        async for i in ads:
            list.append(convert_ads(i))
        return list

async def createAds(data: dict) -> dict:
    ads = await collectionAds.insert_one(data)
    new = await collectionAds.find_one({"_id": ads.inserted_id})  
    return convert_ads(new)
