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
        "address": university["address"],
        "courses": university["courses"]
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
        "courses": ads["courses"],
        "student": ads["student"],
        "university": ads["university"]

    }

def convert_email(email) -> dict:
    return {
        "id": str(email["_id"]),
        "student": email["student"],
        "ads": email["ads"]
    }
