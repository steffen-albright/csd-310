from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.7vyzi7i.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

students = db.students

profiles = [
    {
        "first_name": "Freddie",
        "last_name": "Krueger",
        "student_id": "1007"
    },
    {
        "first_name": "Jason",
        "last_name": "Vorhees",
        "student_id": "1008"
    },
    {
        "first_name": "Ghost",
        "last_name": "Face",
        "student_id": "1009"
    }
]

for profile in profiles:
    new_student_Id = students.insert_one(profile).inserted_id
    print(new_student_Id)
    
