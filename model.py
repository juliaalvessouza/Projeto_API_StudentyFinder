from pydantic import BaseModel, Field

# classe model 
class Student(BaseModel):
    name: str = Field(...)
    email: str = Field(...)
    interest: str = Field(...)

    class Config:
        schema_extra = {
            "exemplo": {
                "name": "Fábio Magalhães",
                "email": "magalhaes@email.com",
                "interest": "tecnologia"
            }
        }
class Courses(BaseModel):
    name: str = Field(...)
    area: str = Field(...)

    class Config:
        schema_extra = {
            "exemplo": {
                "name": "Big Data no Agronegócio",
                "area": "Tecnologia e informação",
            }
        } 


class University(BaseModel):
    name: str = Field(...)
    address: str = Field(...)
    courses: list = Field(...)

    class Config:
        schema_extra = {
            "exemplo": {
                "name": "Fatec Pompeia",
                "address": "Av Fundação Shunji Nishimura - 605 - Distrito Industrial",
                "courses": [
                    {
			            "name": "big data", 
			            "area": "tecnologia"
		            }
                ]
            }
        }        

class Ads(BaseModel):
    total_sutudents: int = Field(...)
    content: str = Field(...)
    courses: Courses = Field(...)

    class Config:
        schema_extra = {
            "exemplo": {
                "total_students": 20,
                "content": "Venha conhecer a Fatec Pompeia!!! Referência em Tecnologia no Agronegócio",
                "courses": "Big Data no Agronegócio"
            }
        }   

class Email(BaseModel):
    student: Student = Field(...)
    ads: Ads = Field(...)

    class Config:
        schema_extra = {
            "exemplo": {
                "student": "Fábio Magalhães",
                "ads": "[Venha Fazer parte da Fatec Pompeia],  [Venha para o Big Data]"
            }
        }  