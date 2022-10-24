import motor.motor_asyncio

def database():
    mongo_atlas = "mongodb+srv://fastapi:studentfinder@cluster0.bqr0cim.mongodb.net/?retryWrites=true&w=majority"
    client = motor.motor_asyncio.AsyncIOMotorClient(mongo_atlas)
    data = client.api_student
    return data