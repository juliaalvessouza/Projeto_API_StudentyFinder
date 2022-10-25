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
    email: str = Field(...)
    senha: str = Field(...)
    address: str = Field(...)
    courses: list = Field(...)

    class Config:
        schema_extra = {
            "exemplo": {
                "name": "Fatec Pompeia",
                "email": "fatec.pompeia@gov.com.br",
                "senha": "1234",
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
    courses: list = Field(...)
    students: list = Field(...)
    university: list = Field(...)

    class Config:
        schema_extra = {
            "exemplo": {
                "total_students": 20,
                "content": "Venha conhecer a Fatec Pompeia!!! Referência em Tecnologia no Agronegócio",
                "courses": [
                    {
			            "name": "big data", 
			            "area": "tecnologia"
		            }
                ],
                "student": [
                    {
			           "name": "Fábio Magalhães",
                        "email": "magalhaes@email.com",
                        "interest": "tecnologia"
		            }
                ],
                "university": [
                    {
                        "name": "Fatec Pompeia",
                        "email": "fatec.pompeia@gov.com.br"                     
                    }
                ]
            }
        }   
