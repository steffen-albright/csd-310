from pymongo import MongoClient
 
url = "mongodb+srv://admin:admin@cluster0.7vyzi7i.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

 
Freddie = {
    "student_id": "1007",
    "first_name": "Freddie",
    "last_name": "Krueger"
}
 
Jason = {
    "student_id": "1008",
    "first_name": "Jason",
    "last_name": "Vorhees"
}

Ghost = {
    "student_id": "1009",
    "first_name": "Ghost",
    "last_name": "Face"
}
 
students = db.students
 
Freddie_student_id = students.insert_one(Freddie).inserted_id
Jason_student_id = students.insert_one(Jason).inserted_id
Ghost_student_id = students.insert_one(Ghost).inserted_id


print("\n -- INSERT STATEMENTS --")
print("  Inserted student record Freddie Krueger into the students collection with document_id " + str(Freddie_student_id))
print("  Inserted student record Jason Vorhees into the students collection with document_id " + str(Jason_student_id))
print("  Inserted student record Ghost Face into the students collection with document_id " + str(Ghost_student_id))

input("\n  End of program, press the Enter key to exit... ")
