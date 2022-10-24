from db import *
from convert import *
from bson.objectid import ObjectId

#conectar collection
collectionAds = database().get_collection("ads")

async def findAllAds() -> dict:
    list = []
    ads = collectionAds.find()
    async for i in ads:
        list.append(convert_ads(i))
    return list 

async def findAdsById(id: str) -> dict:
    ads = collectionAds.find_one({"_id": ObjectId(id)})
    if ads:
        return convert_ads(ads) 

async def createAds(data: dict) -> dict:
    ads = await collectionAds.insert_one(data)
    new = await collectionAds.find_one({"_id": ads.inserted_id})  
    return convert_ads(new)

async def UpdateAds(id: str, data: dict):
    ads = await collectionAds.find_one({"_id": ObjectId(id)})
    if ads:
        ads_updated = await convert_ads.update_one(
            {"_id": ObjectId(id)},
            {"$set": data}
        )
        if ads_updated:
            return True
        return False