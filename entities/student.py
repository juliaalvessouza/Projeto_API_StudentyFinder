from db import *
from convert import *

#conectar collection
collectionStudenty = database().get_collection("student")

async def findStudentByInterest(interest: str) -> dict:
    list = []
    students = collectionStudenty.find({"interest": interest})
    async for i in students:
        list.append(convert_student(i))
    return list 